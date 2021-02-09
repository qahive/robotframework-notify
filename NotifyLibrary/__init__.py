# Get the version from the _version.py versioneer file. For a git checkout,
# this is computed based on the number of commits since the last tag.
from ._version import get_versions
__version__ = str(get_versions()['version']).split('+')[0]
del get_versions

class NotifyLibrary():

    def __init__(self):
        print('Init NotifyLibrary')

    def testing(self):
        print('xxx')
