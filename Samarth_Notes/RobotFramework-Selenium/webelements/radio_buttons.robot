*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${radio_button}

*** Test Cases ***
Handle Radiobuttons
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    # 1
    page should contain radio button    //input[@id='benzradio']
    # not contain keyword is also there

    # 2
    radio button should not be selected   cars

    # 3
    select radio button    cars    benz

    # 4
    radio button should be set to    cars    benz

    sleep    3

    close browser