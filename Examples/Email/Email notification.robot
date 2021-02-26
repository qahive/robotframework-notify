*** Settings ***
Library    NotifyLibrary


*** Test Cases ***
Notify test result via email
    Init Email Notifier
    Send Notify Msg    Hello world
