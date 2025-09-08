*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
run
    run keyword    log    samarth
    run keywords    open browser    https://www.letskodeit.com/practice    chrome
    ...    AND    maximize browser window
    ...    AND    close browser
 
