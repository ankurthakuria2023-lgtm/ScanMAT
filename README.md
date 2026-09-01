# ScanMAT Flask App

This project wraps the supplied ScanMAT HTML application in Flask and adds a
mobile-friendly layout for phones.

## 1. Install

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Then:
```bash
pip install -r requirements.txt
```

## 2. Run

```bash
python app.py
```

Open on the same computer:
- https://127.0.0.1:5000

To open it from a phone on the same Wi-Fi:
1. Find the computer's local IP address (for example, 192.168.1.20).
2. On the phone open:
   https://192.168.1.20:5000
3. Because this development server uses a self-signed certificate, the browser
   will show a certificate warning. Proceed to the site for local testing.
4. Allow camera permission when using the Scan button.

If Windows Firewall asks for permission, allow Python/port 5000 on your
private network.

## Important data note

The supplied HTML stores material records and issue transactions in
browser `localStorage`. That means Flask serves the same application to
phone and desktop, but the stored records are NOT automatically shared
between devices.

If you want phone + desktop to use one shared warehouse database, the next
step is to move records/issues from browser localStorage into a Flask API
with SQLite (or PostgreSQL). The UI can remain largely the same.
