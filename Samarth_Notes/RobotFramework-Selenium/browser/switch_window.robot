# window==tab

*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
switch window demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    click element    //a[@id='opentab']    # This will open a new tab, but it will not wait until the page in the new tab is opened completely, immidiately next commamd will be executd so I need to handle it.
    # now still the control will be in first window
    switch window    NEW
    # next commamds should be executed after hanling the page load.
    wait until element is visible    //a[.='Sign In']
    click element    //a[.='Sign In']
    sleep    4
    switch window    MAIN
    click element    //input[@id='bmwcheck']
    sleep    3
    reload page
    close browser

# Note : similarily there a 'switch browser' keyword.
   frame should contain