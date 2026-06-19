import requests
import smtplib
import os
from email.mime.text import MIMEText

URL = "https://results.bmsce.contineo.in/"

try:
    html = requests.get(URL, timeout=20).text
except requests.RequestException as e:
    print(f"Request failed: {e}")
    exit(1)

if "The Site is Currently Down" not in html:

    msg = MIMEText(
        "BMSCE Results website appears to be LIVE.\n\n"
        "Open: https://results.bmsce.contineo.in/"
    )

    msg["Subject"] = "🎓 BMSCE Results Available!"
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["EMAIL_TO"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.environ["EMAIL_USER"],
            os.environ["EMAIL_PASSWORD"]
        )
        server.send_message(msg)

    print("EMAIL SENT - Results site is LIVE!")

else:
    print("Site still down - will check again next run")