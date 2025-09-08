*** Variables ***
${result}    as

*** Test Cases ***
conditions demo
    run keyword if    '${result}'=='pass'    log    pass
    ...    ELSE IF    '${result}'=='fail'    log    fail
    ...    ELSE      log    NA

# ELSE IF & ELSE should be in caps
