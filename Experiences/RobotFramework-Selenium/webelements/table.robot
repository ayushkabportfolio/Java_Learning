*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
handle table
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    # handleing table all depends on locators we provide.

    # row & column count
    ${rows}=    get element count    //table/tbody/tr
    ${columns}=    get element count    (//table/tbody/tr)[1]/th     # number of elements in a row == columns in a table.
    log to console    ${rows}
    log     ${columns}

    # get table data
    ${ele_text}=    get text    ((//table/tbody/tr)[3]/td)[2]
    log to console   ${ele_text}

    ${class_value}=    get element attribute    ((//table/tbody/tr)[3]/td)[2]    class
    log   ${class_value}

    # validations
    table header should contain    //table[@id='product']    Course
    table column should contain    //table[@id='product']    2    Course
    table row should contain    //table[@id='product']    3    30
    table cell should contain   //table[@id='product']    4    3    25
    close browser

# here index starst from 1