import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from config import EMAIL_HOST, EMAIL_PORT, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_USE_TLS


def send_email():
    with open('report.txt', 'r') as f:
        report = f.read()

    msg = MIMEMultipart()
    msg['From'] = EMAIL_HOST_USER
    msg['To'] = 'recipient@example.com'
    msg['Subject'] = 'Daily Twitter Report'

    msg.attach(MIMEText(report, 'plain'))

    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls() if EMAIL_USE_TLS else None
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(EMAIL_HOST_USER, 'recipient@example.com', msg.as_string())
    server.quit()


if __name__ == '__main__':
    send_email()
