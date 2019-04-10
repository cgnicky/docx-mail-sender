import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email import encoders


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

    mime = MIMEBase('docx', 'docx', filename=file)
    mime.add_header('Content-Disposition', 'attachment', filename=("big5", "", str(file).split("/")[4]))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(open(file, "rb").read())
    encoders.encode_base64(mime)
    msg.attach(mime)

    for i in attachments:
        item = i.split(",")
        mime = MIMEBase('pdf', 'pdf', filename=item[0])
        mime.add_header('Content-Disposition', 'attachment', filename=("big5", "", item[1]))
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        mime.set_payload(open(item[0], "rb").read())
        encoders.encode_base64(mime)
        msg.attach(mime)

    server = smtplib.SMTP("smtp.gmail.com:587")
    server.ehlo()
    server.starttls()
    server.login(sender, password)

    server.sendmail(msg['From'], emaillist, msg.as_string())
