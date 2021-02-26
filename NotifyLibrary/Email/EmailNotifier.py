from NotifyLibrary.notify import iNotifier
from smtplib import SMTP, ssl


class EmailNotifier(iNotifier):

    def __init__(self):
        self.PORT = 465  # For SSL

    def send_notify(self):
        #fromaddr = ''
        toaddrs = ''
        msg = ''
        context = ssl.create_default_context()
        # with SMTP("domain.org", self.PORT, context=context) as server:
        #     server.login("my@gmail.com", 'password')
        #     server.sendmail(fromaddr, toaddrs, msg)

