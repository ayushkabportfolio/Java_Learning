# explicitily waiting for certain condition to be true.

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
set selenium speed demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    # Note : I can set a global timeout time using 'set selemiun timeout'.

    wait until page contains element    //input[@id='autosuggest']    # element should be in HTML DOM
    wait until element is visible     //input[@id='autosuggest']    # element should be visible on web-page

    wait until page does not contain element    //input[@id='autsuggest']
    wait until element is not visible    //input[@id='autsuggest']

    # I can specify the timeout as arguments seperately for each explicit wait
    wait until page contains element    //input[@id='autosuggest']    10
    wait until element is not visible    //input[@id='autsuggest']    10


# Note : By default the timeouts in selenium is 5 secs
    close browser

