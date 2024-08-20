import smtplib, ssl
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = os.getenv("M_B_GMAIL_MAIL")
    password = os.getenv("M_B_GMAIL_APP_PASSWORD")

    receiver = os.getenv("M_B_GMAIL_MAIL")
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
