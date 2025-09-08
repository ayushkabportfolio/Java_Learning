*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
get title demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    ${title}=     get title      # title of page or win or tab
    log    ${title}