*** Settings ***
Library    NotifyLibrary


*** Test Cases ***
Notify test result via email
    Log    Email
    NotifyLibrary.Testing
