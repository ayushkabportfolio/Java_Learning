*** Settings ***
Library    SeleniumLibrary


*** Keywords ***

${search}        



*** Test Cases ***

1.Login to the url
    open browser    https://example.com    chrome
    Maximize Browser Window
    Set Selenium Implicit Wait    5


*** Keywords ***
