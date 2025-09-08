*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Navigational commands
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    go to    https://github.com/
    ${new_url}=     get location
    log to console      ${new_url}

    go back
    ${new_url}=     get location
    log to console      ${new_url}

    reload page
    catenate
    close browser