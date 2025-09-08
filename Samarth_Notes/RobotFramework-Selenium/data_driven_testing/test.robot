# Testing the same set of steps or say test case with different sets of data derived from some data source like excel or csv file.
# Ex : Login

*** Settings ***
Library    SeleniumLibrary
#Library    DataDriver    file=../data_driven_testing/data_excel.xlsx    sheet_name=Sheet1    # if this is not provided, by default sheet1 will be considered.
Library    DataDriver    file=../data_driven_testing/data_csv.csv    encoding=utf_8    dialect=unix
# encoding here represents that in the text in the csv file is encoded/stored in utf_8 format
# dialect here represents that in which foramt the csv file is structured.
# dialect will be enough, but sometimes encoding is needed, so better to add both
# if dialect is not provided then tests will not run, it will show testcases cannot be empty,
Test Template    Login to GitHub with invalid credentials
# Note that the Keyword & Test template name should be same, else I will get test cannot be empty, because it will try to execute the test cases section which will be empty.
# The DataDriver lib & test template can be anywhere in settings section, but std is adding at last

*** Test Cases ***
Checking scenarios for Login functionality with invalid credentials
# Here TC doesn't have any role so it can be anuthing, it will be added simply, since it's mandatory to execute robot file.
# here only keyword will be executed with different data sets from CSV file.

*** Keywords ***
Login to GitHub with invalid credentials
    [Arguments]    ${pass}    ${user}   ${polarity}  # order need not to be same as in data source file
    set tags    ${polarity}
    open browser    https://github.com/    chrome
    maximize browser window
    click link    (//a[@href='/login'])[2]
    wait until element is visible    //input[@id='login_field']
    input text  //input[@id='login_field']    ${user}
    input password    //input[@id='password']    ${pass}
    click element    //input[@value='Sign in']
    element should be visible    //div[@role='alert' and contains(.,'Incorrect username or password')]
    close browser