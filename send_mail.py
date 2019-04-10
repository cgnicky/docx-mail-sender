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

    #    part = MIMEApplication(open(file, "rb").read())
    #    part.add_header('Content-Disposition', 'attachment', filename=str(file).split("/")[4])
    #    msg.attach(part)

    #    part = MIMEApplication(open(file, 'rb').read(),
    #    'application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    # 'octet-stream': binary data
    #    part["Content-Type"] = "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
    #    part.add_header('Content-Disposition', 'attachment', filename=("big5", "",str(file).split("/")[4]))
    #    msg.attach(part)

    mime = MIMEBase('docx', 'docx', filename=file)
    mime.add_header('Content-Disposition', 'attachment', filename=("big5", "", str(file).split("/")[4]))
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(open(file, "rb").read())
    encoders.encode_base64(mime)
    msg.attach(mime)

    #    part = MIMEApplication(open(file2, "rb").read())
    #    part.add_header('Content-Disposition', 'attachment', filename=str(file2).split("/")[4])
    #    msg.attach(part)

    for i in attachments:
        item = i.split(",")
        #        part = MIMEApplication(open(item[0], "rb").read())
        #        part.add_header('Content-Disposition', 'attachment', filename=item[1])
        #        msg.attach(part)
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