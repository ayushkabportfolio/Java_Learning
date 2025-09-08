*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
sleep demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    select checkbox    //input[@id='bmwcheck']
    sleep    3     # by default the sleep will be in seconds.
    select checkbox    //input[@id='hondacheck']
    close browser
    # disadvantages :
    # It pauses the execution for the specified time, even though the web element is visible withing that time, so it increases execution time unnecessarily.