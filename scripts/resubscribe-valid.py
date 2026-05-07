"""
resubscribe-valid.py — Re-subscribe confirmed-valid contacts from cleaned status

Usage:
    python scripts/resubscribe-valid.py          # dry run
    python scripts/resubscribe-valid.py --apply  # re-subscribes for real
"""

import os, re, sys, json, hashlib, base64, urllib.request, urllib.error

LIST_ID = '9d174b3762'

VALID_EMAILS = [
    'jamese@plantco.com',
    'stsang.lai@gmail.com',
    'scott@coastharboreng.com',
    'mstevens@nps.edu',
    'dlalders@nps.edu',
    'thart@sheedycrane.com',
    'gcass@sca-enviro.com',
    'cs@bcschmidt.com',
]


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

    def _request(self, method, endpoint, body=None):
        url = f'https://{self.dc}.api.mailchimp.com/3.0/{endpoint}'
        data = json.dumps(body).encode() if body else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header('Authorization', f'Basic {self.creds}')
        req.add_header('Content-Type', 'application/json')
        try:
            with urllib.request.urlopen(req) as r:
                raw = r.read()
                return r.status, json.loads(raw) if raw else {}
        except urllib.error.HTTPError as e:
            raw = e.read()
            return e.code, json.loads(raw) if raw else {}

    def get_member(self, email):
        h = subscriber_hash(email)
        status, data = self._request('GET', f'lists/{self.list_id}/members/{h}')
        return data if status == 200 else None

    def resubscribe(self, email):
        h = subscriber_hash(email)
        status, data = self._request('PUT', f'lists/{self.list_id}/members/{h}',
            {'email_address': email, 'status': 'subscribed'})
        return status in (200, 201), data


def run(apply=False):
    print(f"{'[DRY RUN] ' if not apply else ''}Re-subscribing confirmed-valid contacts\n")
    mc = MailchimpClient(load_api_key(), LIST_ID)

    for email in VALID_EMAILS:
        member = mc.get_member(email)
        if member:
            name = member.get('full_name', '').strip() or '—'
            current = member.get('status', 'unknown')
            print(f"  {email}")
            print(f"    Name: {name}  |  Current status: {current}")
            if not apply:
                print(f"    Would re-subscribe")
            else:
                ok, data = mc.resubscribe(email)
                if ok:
                    print(f"    Re-subscribed")
                else:
                    print(f"    FAILED: {data.get('detail', '')}")
        else:
            print(f"  {email} — not found in Mailchimp")
        print()

    if not apply:
        print("Run with --apply to re-subscribe these contacts.")


if __name__ == '__main__':
    apply = '--apply' in sys.argv
    run(apply=apply)
