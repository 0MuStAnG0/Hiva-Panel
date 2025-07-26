import smtplib
from email.mime.text import MIMEText

def send_notification_email(to_email, subject, content):
    msg = MIMEText(content)
    msg["Subject"] = subject
    msg["From"] = "noreply@hivapanel.local"
    msg["To"] = to_email

    try:
        server = smtplib.SMTP("localhost")
        server.send_message(msg)
        server.quit()
        return True
    except Exception as e:
        print(f"Email Error: {e}")
        return False
