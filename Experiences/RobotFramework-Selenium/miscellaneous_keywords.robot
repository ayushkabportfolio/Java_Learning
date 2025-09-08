*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
handle links
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    ${links_count}=    get element count    //a
    log    ${links_count}
    sleep    2
    close browser