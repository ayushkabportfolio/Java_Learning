*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
close browser(s) demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    # close browser

    open browser    https://github.com/   chrome
    maximize browser window
    # close browser # In this case this keyword will only close the recently opened browser.

    close all browsers


