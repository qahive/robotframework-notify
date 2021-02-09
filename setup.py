import re
from os.path import abspath, dirname, join
from setuptools import setup, find_packages


CURDIR = dirname(abspath(__file__))

with open("README.md", "r", encoding='utf-8') as fh:
    LONG_DESCRIPTION = fh.read()

# Get the version from the _version.py versioneer file. For a git checkout,
# this is computed based on the number of commits since the last tag.
from NotifyLibrary._version import get_versions
VERSION = str(get_versions()['version']).split('+')[0]
del get_versions

setup(
    name="robotframework-NotifyLibrary",
    version=VERSION,
    author="QA Hive Co.,Ltd",
    author_email="support@qahive.com",
    description="Send notification to variant receiver (Slack, MS Team, Line, Whatsapp and Email)",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    license="Apache License 2.0",
    url='https://qahive.github.io/robotframework-notify.github.io/',
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "License :: OSI Approved :: MIT Software License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Testing :: Acceptance",
        "Framework :: Robot Framework",
    ],
    keywords='robotframework puppeteer web-testing automation',
    platforms='any',
    install_requires=[
        'robotframework>=3.2.1'
    ],
    zip_safe=False,
)
