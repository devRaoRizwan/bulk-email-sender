# gmail-bulk-sender

A Selenium script that logs into Gmail in a real Chrome browser and sends the same email to every address listed in a CSV.

Uses `undetected-chromedriver` and randomized delays / character-by-character typing to mimic human behavior.

## Setup

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Create a `.env` file:

```
GMAIL_USER=you@gmail.com
GMAIL_PASS=your_password
```

Add recipients to `emails.csv`, one per line (first column, header row is skipped automatically since it lacks `@`):

```
email
someone@example.com
another@example.com
```

## Usage

Edit `SUBJECT` and `BODY` in [send_emails.py](send_emails.py#L17-L18), then run:

```bash
python send_emails.py
```

Chrome opens, logs in, and composes/sends one message per address with an 8–14 s pause between sends. The script pauses 12 s after login so you can complete 2FA manually.

## Notes

- `version_main=151` in [send_emails.py:22](send_emails.py#L22) must match your installed Chrome version.
- Requires a visible display — no headless mode.
- Relies on Gmail's current DOM selectors; UI changes will break it.
- Don't commit `.env` — it holds plaintext credentials.
- Only send to recipients who have agreed to hear from you; bulk sending can get the account rate-limited or suspended.
- so we need to ensure that spam is not triggered
