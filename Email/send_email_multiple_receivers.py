import os
import smtplib
import ssl
from email.message import EmailMessage
from email.mime.base import MIMEBase
from email import encoders
import pandas as pd
import myEnvVal as myEnvVal

myEnvVal.setVar()

# Define email sender and receiver
email_sender = 'panupong.intern.work@gmail.com'
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'panupong.intern.work@gmail.com'

# Set the subject and body of the email
subject = 'Check out my new video!'
body = "I've just published a new video on YouTube: https://youtu.be/2cZzP9DLlkg"

# Reading the CSV file
csv_path = r'C:\Users\Panupong Jindarat\Documents\GitHub\automation\datasets\multiple_emails.csv'
emails_df = pd.read_csv(csv_path)

# Looping through the CSV file and sending emails with attachments
for index, row in emails_df.iterrows():
    email_receiver = row['Receiver']
    attachment_file_name = row['Attatchment']

    # Define email parameters
    em = EmailMessage()
    em['From'] = email_sender
    em['To'] = email_receiver
    em['Subject'] = subject
    em.set_content(body)

    # Make the message multipart
    em.add_alternative(body, subtype='html')

    attachment_file_name = fr'C:\Users\Panupong Jindarat\Documents\GitHub\automation\datasets\{attachment_file_name}'

    # Attach the image file
    with open(attachment_file_name, 'rb') as attachment_file:
        file_data = attachment_file.read()
        file_name = attachment_file.name.split('\\')[-1]

    attachment = MIMEBase('application', 'octet-stream')
    attachment.set_payload(file_data)
    encoders.encode_base64(attachment)
    attachment.add_header('Content-Disposition', f'attachment; filename="{file_name}"')
    em.attach(attachment)

    # Add SSL (layer of security)
    context = ssl.create_default_context()

    # Log in and send the email
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receiver, em.as_string())
