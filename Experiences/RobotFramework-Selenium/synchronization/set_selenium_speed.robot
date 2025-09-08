*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
set selenium speed demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    set selenium speed    2   #before exceution of every command coming next, the selenium will wait for specified time
    select checkbox    //input[@id='bmwcheck']
    select checkbox    //input[@id='hondacheck']
    close browser

# disadvantages : before exceution of every command coming next, the selenium will wait for specified time, so it will unnecessarily increase the execution time.

# Note:
# By default selenuim speed will wait for 0 secs before exceuting the command.