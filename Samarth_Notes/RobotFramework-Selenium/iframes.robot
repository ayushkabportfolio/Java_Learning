# page within main page is called as iframe or frame

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
handle iframe
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    # here control will be on webpage not on iframe in it
    select frame   //iframe[@id='courses-iframe']
    # control will switch to iframe
    input text    //input[@id='search']    SAM
    sleep    3
    unselect frame
    # control will switch to main frame or it basically cancles the previous 'select frame'