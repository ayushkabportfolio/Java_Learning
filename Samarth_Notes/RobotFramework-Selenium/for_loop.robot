*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
for loop with IN RANGE
    FOR    ${i}    IN RANGE    1    5     # 5-1 i.e will be considered
        log    ${i}
    END

for loop with IN
    FOR    ${i}    IN    1    2    3
        log    ${i}
    END

for loop with list
    @{my_list}    create list    1    2    3    4    5
    FOR    ${i}    IN    @{my_list}
        log    ${i}
    END

for loop with str
    FOR    ${i}    IN    SAM    RAM    BAM    KAM    # No need to give '', since it will autoidentify the data type like python
        log    ${i}
    END

for loop with str list
    @{my_list}    create list    RAM    BAM    KAM
    FOR    ${i}    IN    @{my_list}
        log    ${i}
    END

for loop with exit condition
    @{my_list}    create list    1    2    3    4    5
    FOR    ${i}    IN    @{my_list}
        log    ${i}
        exit for loop if    ${i}==4
    END

for loop with continue condition
    @{my_list}    create list    1    2    3    4    5
    FOR    ${i}    IN    @{my_list}
        continue for loop if    ${i}==2 or ${i}==4
        log    ${i}
    END