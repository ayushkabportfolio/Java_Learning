*** Settings ***
Library    SeleniumLibrary
Resource    resources/keywords.robot
# Resourse is for importing the user defined robotfiles in the project
# By default the control will be on the current file dir
# ../ for moving to immediate parent dir & / for moving to immediate child dir/file

*** Variables ***
${url}    https://github.com/
${browser}    chrome
${user}    samarthkulkarni777@gmail.com
${password}    Git@1234

*** Test Cases ***
user defined keywords demo
    launch browser
    ${page_title}=    sign-in    ${user}    ${password}    # order of arguments should be same as order of arguments expected in keyword, else data will not go to proper elements
    should be equal as strings    ${page_title}    GitHub

*** Keywords ***
launch browser    # without any arguments
    open browser    ${url}    ${browser}
    maximize browser window