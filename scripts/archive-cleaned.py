"""
archive-cleaned.py — Archive confirmed dead-domain contacts from Mailchimp

Reads scripts/cleaned-dead-domains.md, extracts email addresses,
and archives them in Mailchimp (removes from contact count, keeps history).

Usage:
    python scripts/archive-cleaned.py          # dry run — shows what would be archived
    python scripts/archive-cleaned.py --apply  # archives for real
"""

import os, re, sys, json, hashlib, base64, urllib.request, urllib.parse

LIST_ID = '9d174b3762'
DEAD_DOMAINS_FILE = os.path.join(os.path.dirname(__file__), 'cleaned-dead-domains.md')


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

    def _request(self, method, endpoint):
        url = f'https://{self.dc}.api.mailchimp.com/3.0/{endpoint}'
        req = urllib.request.Request(url, method=method)
        req.add_header('Authorization', f'Basic {self.creds}')
        try:
            with urllib.request.urlopen(req) as r:
                raw = r.read()
                return r.status, json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read()
            return e.code, json.loads(raw) if raw else {}

    def archive(self, email):
        """Archive a contact — removes from count, keeps history. Reversible."""
        h = subscriber_hash(email)
        status, _ = self._request('DELETE', f'lists/{self.list_id}/members/{h}')
        return status == 204

    def get_member_status(self, email):
        """Check current status of a contact."""
        h = subscriber_hash(email)
        status, data = self._request('GET', f'lists/{self.list_id}/members/{h}')
        if status == 200:
            return data.get('status', 'unknown')
        return None  # not found


def load_dead_emails():
    """Parse email addresses from cleaned-dead-domains.md (table rows only, skip notes)."""
    emails = []
    in_false_positives = False
    with open(DEAD_DOMAINS_FILE) as f:
        for line in f:
            if 'False Positives' in line:
                in_false_positives = True
            if in_false_positives:
                continue
            m = re.match(r'\|\s*([^\s|]+@[^\s|]+)\s*\|', line)
            if m:
                emails.append(m.group(1).strip())
    return emails


def run(apply=False):
    print(f"{'[DRY RUN] ' if not apply else ''}Archiving dead-domain contacts\n")

    emails = load_dead_emails()
    print(f"Addresses in dead-domains file: {len(emails)}")

    mc = MailchimpClient(load_api_key(), LIST_ID)

    # Check current status of each before acting
    to_archive = []
    not_found = []
    skipped = []

    for email in emails:
        status = mc.get_member_status(email)
        if status is None:
            not_found.append(email)
        elif status == 'cleaned':
            to_archive.append(email)
        else:
            skipped.append((email, status))

    print(f"Cleaned (will archive): {len(to_archive)}")
    print(f"Not found in Mailchimp: {len(not_found)}")
    print(f"Skipped (not cleaned):  {len(skipped)}")

    if skipped:
        print("\nSkipped (unexpected status):")
        for e, s in skipped:
            print(f"  {e} — {s}")

    if not to_archive:
        print("\nNothing to archive.")
        return

    print(f"\nWill archive:")
    for e in to_archive:
        print(f"  {e}")

    if not apply:
        print(f"\nRun with --apply to archive these {len(to_archive)} contacts.")
        return

    print(f"\nArchiving...")
    archived = failed = 0
    for email in to_archive:
        if mc.archive(email):
            print(f"  OK  {email}")
            archived += 1
        else:
            print(f"  FAIL {email}")
            failed += 1

    print(f"\nDone. Archived: {archived}  Failed: {failed}")


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    run(apply=apply)
