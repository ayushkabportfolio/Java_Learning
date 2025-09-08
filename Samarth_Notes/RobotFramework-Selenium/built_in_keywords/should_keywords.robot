# all 'should ...' keywords are w.r.t variables


*** Test Cases ***
practice
    ${ss}=    set variable    12

    # should be
     should not be empty    ${ss}




