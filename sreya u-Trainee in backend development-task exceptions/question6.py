"""6.Write a Python program that reads email details (sender, recipient, subject, and body)
from user input and sends the email using Mailtrap as the SMTP server."""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

EMAIL_HOST = 'sandbox.smtp.mailtrap.io'
EMAIL_HOST_USER = 'f8291bf2461890'
EMAIL_HOST_PASSWORD = '2bf878152cb759'
EMAIL_PORT = '2525'

sender_email = input("Enter sender email: ")
recipient_email = input("Enter recipient email: ")
subject = input("Enter email subject: ")
body = input("Enter email body: ")

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message['Subject'] = subject
message.attach(MIMEText(body, 'plain'))

try:
    server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
    server.starttls()
    server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
    server.sendmail(sender_email, recipient_email, message.as_string())
    print("Email sent successfully!")
except smtplib.SMTPException as e:
    print("SMTP error occurred:", e)
except Exception as e:
    print("An error occurred:", e)
finally:
    server.quit()

