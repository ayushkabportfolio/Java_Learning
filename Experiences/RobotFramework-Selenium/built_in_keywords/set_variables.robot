*** Settings ***
Library    SeleniumLibrary


*** Test Cases ***
variables demo1
    ${browser}=    set variable    chrome
    open browser    https://www.letskodeit.com/practice   ${browser}
    maximize browser window
    ${status}=    run keyword and return status    element should be visible    //input[@id='bmwradio']
    log    ${status}
#    set test variable     ${status}
#    set suite variable   ${status}
    set global variable    ${status}

variables demo2
   log    ${status}    # as of now it will be highlighted in red but in runtime it will be sorted.

