*** Keywords ***
sign-in
    [Arguments]    ${user}    ${password}    # with arguments
    click element    (//a[contains(.,'Sign in')])[last()]
    wait until element is visible    //input[@id='login_field']
    input text    //input[@id='login_field']    ${user}
    input password    //input[@id='password']    ${password}
    click element    //input[@value='Sign in']
    ${title}=    get title
    RETURN    ${title}