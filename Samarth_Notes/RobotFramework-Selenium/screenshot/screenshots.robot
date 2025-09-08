*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
screentshot demo
    open browser    https://github.com/    chrome
    maximize browser window
    click element    (//a[contains(.,'Sign in')])[last()]
    wait until element is visible    //input[@id='login_field']
    input text    //input[@id='login_field']    sam@comviva.com
    input password    //input[@id='password']    ssd
    click element    //input[@value='Sign in']
    capture page screenshot    C:/Users/samarth.kulkarni/PycharmProjects/RobotFramework-Selenium/screenshot/pagescreen.png
    close browser

    # Note:
    # screenshots images should be saved with .png extension.
    # path specified should be abs path with '/'
    # if i don;t specify path then screenshot will be stored in project directory by default.
    # if exiting file name is given, then override will happen