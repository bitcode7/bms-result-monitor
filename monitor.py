import requests
import smtplib
import os
from email.mime.text import MIMEText

URL = "https://youtube.com/"

html = requests.get(URL, timeout=20).text

if "The Site is Currently Down" not in html:

    msg = MIMEText(
        "BMSCE Results website appears to be LIVE.\n\n"
        "Open: https://results.bmsce.contineo.in/"
    )

    msg["Subject"] = "BMSCE Results Available"
    msg["From"] = os.environ["EMAIL_USER"]
    msg["To"] = os.environ["EMAIL_TO"]

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.environ["EMAIL_USER"],
            os.environ["EMAIL_PASSWORD"]
        )
        server.send_message(msg)

    print("EMAIL SENT")

else:
    print("Site still down")