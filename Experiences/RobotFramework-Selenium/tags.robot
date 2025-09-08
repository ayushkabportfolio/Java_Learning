*** Test Cases ***
TC1
    [Tags]    smoke    negative
    log    TC1

TC2
    [Tags]    sanity    negative
    fail


TC3
    [Tags]    smoke    positive
    log    TC3

TC4
    [Tags]    regression    negative
    log    TC4

TC5
    [Tags]    sanity    positive
    log    TC5

# include
# robot -i smoke tags.robot
# robot -i smokeORsanity tags.robot
# robot -i smokeANDpositive tags.robot

# exclude
# robot -e smoke tags.robot
# robot -e smokeORsanity tags.robot
# robot -e smokeANDpositive tags.robot