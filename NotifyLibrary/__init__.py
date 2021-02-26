# Get the version from the _version.py versioneer file. For a git checkout,
# this is computed based on the number of commits since the last tag.
from NotifyLibrary.notify import iNotifier
from NotifyLibrary.email import EmailNotifier
from ._version import get_versions
__version__ = str(get_versions()['version']).split('+')[0]
del get_versions

class NotifyLibrary():

    notifier: iNotifier

    def __init__(self):
        print('Init NotifyLibrary')

    def init_email_notifier(self):
        self.notifier = EmailNotifier()

    def send_notify_msg(self, text):
        self.notifier.send_notify()
