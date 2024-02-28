
"""8.write a python program to handle exceptions when sending emails using Python's smtplib library."""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, recipient_email, subject, body, smtp_host, smtp_port, smtp_username, smtp_password):
    try:
        message = MIMEMultipart()
        message['From'] = sender_email
        message['To'] = recipient_email
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP(smtp_host, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)

        server.sendmail(sender_email, recipient_email, message.as_string())
        print("Email sent successfully!")

    except (smtplib.SMTPException, Exception) as e:
        print("An error occurred while sending the email:", e)

    finally:
        if 'server' in locals():
            server.quit()


smtp_host = 'sandbox.smtp.mailtrap.io'
smtp_port = 2525
smtp_username = 'f8291bf2461890'
smtp_password = '2bf878152cb759'

sender_email = input("Enter sender email: ")
recipient_emails = input("Enter recipient emails (separated by commas): ").split(',')
subject = input("Enter email subject: ")
body = input("Enter email body: ")

send_email(sender_email, recipient_emails, subject, body, smtp_host, smtp_port, smtp_username, smtp_password)
