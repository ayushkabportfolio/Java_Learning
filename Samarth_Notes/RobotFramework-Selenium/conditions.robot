*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
demo or condition
    @{my_list}    create list    SAM    RAM    KAM    BAM   GAM
    FOR    ${i}    IN    @{my_list}
        continue for loop if    '${i}'=='SAM' or '${i}'=='BAM'    # while checking the condition with the str value should be specified withing ''. but when I am specifying simple no need to give quotes.
        log    ${i}
    END

demo and condition
    @{my_list}    create list    SAM    RAM    KAM    BAM   GAM
    FOR    ${i}    IN    @{my_list}
        exit for loop if    '${i}'=='SAM' and '${i}'=='BAM'    # while checking the condition with the str value should be specified withing ''.
        log    ${i}
    END