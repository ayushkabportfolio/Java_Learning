*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
mouse opetaions demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    # 1. right click
    # usually when i right-click on any elemnt, context menu will open, so I can use the below keyword for right click action
    open context menu    //h1[.='Practice Page']
    sleep    3
    click element    (//div[@id='page'])[1]

    # 2. double click element
    double click element    //h1[.='Practice Page']
    sleep     3

    # drag and drop
    go to    http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    wait until element is visible    //div[@id='box6']
    drag and drop    //div[@id='box6']    //div[.='Italy']
    sleep    3

    # mouse over
    go back
    mouse over    //button[@id='mousehover']
    sleep    2
    click element    //a[.='Top']
    sleep    2

    close browser

# There are some other mouse related keyword, which can be explored.