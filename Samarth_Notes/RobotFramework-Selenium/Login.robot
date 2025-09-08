*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}         https://github.com/
${username}    samarthkulkarni777@gmail.com
${password}    Github@1029

*** Test Cases ***
Login with valid credentials
    open browser    ${url}    chrome
    maximize browser window
    click link    (//a[@href='/login' and contains(.,'Sign in')])[2]
    wait until element is visible    //input[@id='login_field']
    login
    close browser

*** Keywords ***
login
    input text    //input[@id='login_field']    ${username}
    input text    //input[@id='password']    ${password}
    click element    //input[@type='submit']
    wait until element is visible   //h2[.='Home']