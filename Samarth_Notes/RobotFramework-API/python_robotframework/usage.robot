*** Settings ***
Library    keywords.py

*** Variables ***
${end_point}    /posts

*** Test Cases ***
post with python & robotframework
    ${id}=    create new user    ${end_point}    FUCK
    log    ${id}
