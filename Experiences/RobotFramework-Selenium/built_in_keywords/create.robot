*** Test Cases ***
create list demo
    ${my_list}=    create list    A    1    s    # it will consider all of these values provided as str only.
    log  ${my_list}

create dictionary demo
    ${my_dic}=    create dictionary    A=1    B=2    C=3    # it will consider all of these values provided as str only.
    log    ${my_dic}
    should contain any