*** Test Cases ***
catenate demo
    ${str1}=    catenate    Hi    there    hello        # By default the strs are catenated with single space, i.e by default separator is single space
    log    ${str1}

    ${str2}=    Catenate	SEPARATOR=-	    Hi    there    hello
    log    ${str2}

    ${str3}=   Catenate    SEPARATOR=	    Hi    there    hello
    log    ${str3}

    ${str4}=    Catenate    SEPARATOR=	    1    there    hello
    log    ${str4}
    # the items need not to be str, whatever i give, it will take it as a str & result of catenate will be str
