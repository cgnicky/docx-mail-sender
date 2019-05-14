import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.header import Header
import os


def send_gmail(file, attachments, sender, receiver, password, subject, content):
    recipients = [receiver]
    emaillist = [elem.strip().split(',') for elem in recipients]
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    #    msg['Reply-to'] = ''

    msg.preamble = 'Multipart massage.\n'

    part = MIMEText(content)
    msg.attach(part)

    part = MIMEApplication(open(file, "rb").read())
    part.add_header('Content-Disposition', 'attachment', filename=(Header(os.path.basename(file), 'utf-8').encode()))
    msg.attach(part)

    for i in attachments:
        item = i.split(",")
        part = MIMEApplication(open(item[0], "rb").read())
        part.add_header('Content-Disposition', 'attachment', filename=(Header(item[1], 'utf-8').encode()))
        msg.attach(part)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(sender, password)

    server.sendmail(msg['From'], emaillist, msg.as_string())
