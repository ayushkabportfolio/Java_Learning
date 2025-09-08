*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
handle alert demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    click element    //input[@id='confirmbtn']
    sleep    2
    # alert will open
    # alert cannot be inspected since it will be develpoed using javascript
    # once alerts appears on screen the control automatically switchs to alerts & until it is closed, I cannot access the web page elements.
    # only click operation can be performed on alerts i.e. ok & cancel

    # handle alert    ACCEPT    # by default
    # handle alert    DISMISS
    # handle alert    LEAVE

#    alert should be present    #Hello , Are you sure you want to confirm?
    sleep    2

    alert should not be present    #Hello , Are you sure you want to confirm?
    # here timeout is 0 secs

    sleep    4

    close browser



