*** Settings ***
Library    SeleniumLibrary
Suite Setup    log    opening browser    # these keyword(s) are executed in begining only once
Suite Teardown    log    closing browser     # these keyword(s) are executed at the end only once

Test Setup    log    login into application     # these keyword(s) are  executed before execution of each test case
Test Teardown    log    logout from application    # these keyword(s) are executed after the execution of each test case

*** Test Cases ***
setups and teardowns demo1
    log    setups and teardowns demo1

setups and teardowns demo2
    log    setups and teardowns demo2