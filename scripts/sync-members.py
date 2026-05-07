"""
sync-members.py — SAME SF Mailchimp member list sync

Usage:
    python scripts/sync-members.py <path-to-roster.xls> [--apply]

Without --apply: dry run — shows what would change (adds, removals, skips).
With --apply:    makes the changes (subscribe new, tag/untag, report errors).

Future: swap read_roster() for a BillHighway API call when that becomes available.
"""

import sys
import os
import re
import json
import hashlib
import base64
import urllib.request
import urllib.error
import urllib.parse
import subprocess

# ── Install xlrd if needed ──────────────────────────────────────────────────
try:
    import xlrd
except ImportError:
    subprocess.run([sys.executable, '-m', 'pip', 'install', 'xlrd', '-q'])
    import xlrd


BILLHIGHWAY_PLACEHOLDER = 'emailnotprovided@billhighway.com'
LIST_ID = '9d174b3762'
MEMBER_TAG = 'Members'


# ── Roster ──────────────────────────────────────────────────────────────────

def read_roster(path):
    """
    Returns list of dicts with keys: name, fname, lname, email.
    Skips BillHighway placeholder emails.
    Replace this function body with a BillHighway API call when available.
    """
    wb = xlrd.open_workbook(path)
    ws = wb.sheet_by_index(0)

    # Find header row (contains 'Email' column)
    header_row = None
    for r in range(min(20, ws.nrows)):
        row = [str(ws.cell_value(r, c)).strip() for c in range(ws.ncols)]
        if 'Email' in row:
            header_row = r
            headers = row
            break

    if header_row is None:
        raise ValueError("Could not find header row with 'Email' column")

    members = []
    for r in range(header_row + 1, ws.nrows):
        row = {headers[c]: str(ws.cell_value(r, c)).strip() for c in range(ws.ncols)}
        name = row.get('Name', '').strip()
        email = row.get('Email', '').strip().lower()

        if not email or email == BILLHIGHWAY_PLACEHOLDER:
            continue

        # Roster format: "Last, First"
        parts = name.split(',', 1)
        lname = parts[0].strip()
        fname = parts[1].strip() if len(parts) > 1 else ''

        members.append({'name': name, 'fname': fname, 'lname': lname, 'email': email})

    return members


# ── Mailchimp API ────────────────────────────────────────────────────────────

def load_api_key():
    env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
    with open(env_path) as f:
        for line in f:
            m = re.match(r'MAILCHIMP_API_KEY\s*=\s*(.+)', line.strip())
            if m:
                return m.group(1).strip().strip('"\'')
    raise ValueError("MAILCHIMP_API_KEY not found in .env")


def subscriber_hash(email):
    return hashlib.md5(email.lower().encode()).hexdigest()


class MailchimpClient:
    def __init__(self, api_key, list_id):
        self.list_id = list_id
        self.dc = api_key.split('-')[-1]
        self.creds = base64.b64encode(f'user:{api_key}'.encode()).decode()

    def _request(self, method, endpoint, body=None, params=None):
        url = f'https://{self.dc}.api.mailchimp.com/3.0/{endpoint}'
        if params:
            url += '?' + urllib.parse.urlencode(params)
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Authorization', f'Basic {self.creds}')
        req.add_header('Content-Type', 'application/json')
        try:
            with urllib.request.urlopen(req) as resp:
                raw = resp.read()
                return resp.status, json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read()
            return e.code, json.loads(raw) if raw else {}

    def get_tagged_members(self):
        """Returns set of emails currently tagged as Members."""
        emails = set()
        offset = 0
        while True:
            status, data = self._request('GET', f'lists/{self.list_id}/segments',
                params={'count': 200, 'offset': offset, 'type': 'static'})
            segments = data.get('segments', [])
            member_seg = next((s for s in segments if s['name'] == MEMBER_TAG), None)
            if member_seg:
                break
            if not segments:
                break
            offset += 200

        if not member_seg:
            return set()

        seg_id = member_seg['id']
        offset = 0
        while True:
            status, data = self._request('GET',
                f'lists/{self.list_id}/segments/{seg_id}/members',
                params={'count': 1000, 'offset': offset, 'fields': 'members.email_address'})
            page = data.get('members', [])
            if not page:
                break
            for m in page:
                emails.add(m['email_address'].lower())
            offset += 1000

        return emails

    def get_subscribed_emails(self):
        """Returns set of all subscribed emails."""
        emails = set()
        offset = 0
        while True:
            status, data = self._request('GET', f'lists/{self.list_id}/members',
                params={'count': 1000, 'offset': offset,
                        'fields': 'members.email_address', 'status': 'subscribed'})
            page = data.get('members', [])
            if not page:
                break
            for m in page:
                emails.add(m['email_address'].lower())
            offset += 1000
        return emails

    def batch_subscribe(self, members):
        """Subscribe a list of member dicts. Returns (added, errors)."""
        payload = [{
            'email_address': m['email'],
            'status': 'subscribed',
            'merge_fields': {'FNAME': m['fname'], 'LNAME': m['lname']}
        } for m in members]
        status, data = self._request('POST', f'lists/{self.list_id}',
            {'members': payload, 'update_existing': False})
        return data.get('new_members', []), data.get('errors', [])

    def set_tag(self, email, active=True):
        """Apply or remove the Members tag for a single email."""
        h = subscriber_hash(email)
        tag_status = 'active' if active else 'inactive'
        status, _ = self._request('POST',
            f'lists/{self.list_id}/members/{h}/tags',
            {'tags': [{'name': MEMBER_TAG, 'status': tag_status}]})
        return status == 204

    def get_cleaned_members(self):
        """Returns list of cleaned (hard-bounced) member dicts."""
        members = []
        offset = 0
        while True:
            status, data = self._request('GET', f'lists/{self.list_id}/members',
                params={'status': 'cleaned', 'count': 1000, 'offset': offset,
                        'fields': 'members.email_address,members.full_name,members.last_changed'})
            page = data.get('members', [])
            if not page:
                break
            members.extend(page)
            offset += 1000
        return members

    def archive_member(self, email):
        """Archive a single contact (removes from contact count)."""
        h = subscriber_hash(email)
        status, _ = self._request('DELETE', f'lists/{self.list_id}/members/{h}')
        return status == 204


# ── Sync logic ───────────────────────────────────────────────────────────────

def check_plan(mc):
    """Warn if account has moved off the grandfathered forever_free plan."""
    status, data = mc._request('GET', 'account-exports' if False else '')
    # Use root API endpoint for account info
    import urllib.request, urllib.parse
    url = f'https://{mc.dc}.api.mailchimp.com/3.0/'
    req = urllib.request.Request(url)
    req.add_header('Authorization', f'Basic {mc.creds}')
    with urllib.request.urlopen(req) as r:
        info = __import__('json').loads(r.read())
    plan = info.get('pricing_plan_type', 'unknown')
    if plan != 'forever_free':
        print(f"\n⚠️  MAILCHIMP PLAN CHANGED: now on '{plan}' (was forever_free)")
        print(f"   Check samesanfrancisco@gmail.com for Mailchimp notices.")
        print(f"   Review contact limits and template compatibility immediately.\n")
    else:
        print(f"Mailchimp plan: {plan} ✓")


def run_sync(roster_path, apply=False):
    print(f"{'[DRY RUN] ' if not apply else ''}Syncing SAME SF member roster → Mailchimp\n")

    roster = read_roster(roster_path)
    roster_emails = {m['email'] for m in roster}
    roster_by_email = {m['email']: m for m in roster}

    print(f"Roster members (valid emails): {len(roster)}")

    mc = MailchimpClient(load_api_key(), LIST_ID)
    check_plan(mc)

    subscribed = mc.get_subscribed_emails()
    tagged = mc.get_tagged_members()

    print(f"Mailchimp subscribed:          {len(subscribed)}")
    print(f"Mailchimp tagged as Members:   {len(tagged)}\n")

    # New members not in Mailchimp at all
    to_subscribe = [roster_by_email[e] for e in roster_emails if e not in subscribed]

    # In Mailchimp but not tagged
    to_tag = [e for e in roster_emails if e in subscribed and e not in tagged]

    # Tagged but no longer on roster (lapsed)
    to_untag = [e for e in tagged if e not in roster_emails]

    print(f"── Changes ────────────────────────────────")
    print(f"New members to subscribe + tag: {len(to_subscribe)}")
    print(f"Existing members to tag:        {len(to_tag)}")
    print(f"Lapsed members to untag:        {len(to_untag)}")

    if to_subscribe:
        print(f"\nNew subscriptions:")
        for m in to_subscribe:
            print(f"  {m['name']} <{m['email']}>")

    if to_tag:
        print(f"\nNeed Members tag:")
        for e in to_tag:
            print(f"  {e}")

    if to_untag:
        print(f"\nLapsed (will untag):")
        for e in to_untag:
            print(f"  {e}")

    if not apply:
        print(f"\nRun with --apply to make these changes.")
        return

    # ── Apply ────────────────────────────────────────────────────────────────
    print(f"\n── Applying ───────────────────────────────")

    if to_subscribe:
        added, errors = mc.batch_subscribe(to_subscribe)
        print(f"Subscribed: {len(added)}  Errors: {len(errors)}")
        for e in errors:
            print(f"  ❌ {e.get('email_address')} — {e.get('error')}")
        # Tag the ones that succeeded
        added_emails = [m['email_address'].lower() for m in added]
        for email in added_emails:
            mc.set_tag(email, active=True)
        print(f"Tagged {len(added_emails)} new subscribers")

    tag_ok = tag_fail = 0
    for email in to_tag:
        if mc.set_tag(email, active=True):
            tag_ok += 1
        else:
            tag_fail += 1
            print(f"  ❌ Could not tag {email}")
    if to_tag:
        print(f"Tagged existing members: {tag_ok}  Failed: {tag_fail}")

    untag_ok = untag_fail = 0
    for email in to_untag:
        if mc.set_tag(email, active=False):
            untag_ok += 1
        else:
            untag_fail += 1
            print(f"  ❌ Could not untag {email}")
    if to_untag:
        print(f"Untagged lapsed members: {untag_ok}  Failed: {untag_fail}")

    # ── Bounce cleanup ───────────────────────────────────────────────────────
    print(f"\n── Bounce Cleanup ─────────────────────────")
    cleaned = mc.get_cleaned_members()
    print(f"Cleaned (hard-bounced) contacts: {len(cleaned)}")

    if cleaned:
        # Write list to file for records
        import datetime
        today = datetime.date.today().isoformat()
        out_path = os.path.join(os.path.dirname(__file__), f'cleaned-contacts-{today}.md')
        with open(out_path, 'w') as f:
            f.write(f'# Cleaned Contacts — {today} ({len(cleaned)} total)\n\n')
            f.write('| Name | Email | Last Changed |\n|---|---|---|\n')
            for m in sorted(cleaned, key=lambda x: x.get('last_changed', '')):
                name = m.get('full_name', '').strip() or '—'
                f.write(f"| {name} | {m['email_address']} | {m.get('last_changed','')[:10]} |\n")
        print(f"List saved to {out_path}")

        print(f"No action taken — cleaned contacts left in place (not hitting contact limit).")
        print(f"To archive all cleaned contacts if limit pressure increases, run: python scripts/archive-cleaned.py")

    print(f"\nDone.")


# ── Entry point ──────────────────────────────────────────────────────────────

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/sync-members.py <path-to-roster.xls> [--apply]")
        sys.exit(1)

    roster_path = sys.argv[1]
    apply = '--apply' in sys.argv

    run_sync(roster_path, apply=apply)
