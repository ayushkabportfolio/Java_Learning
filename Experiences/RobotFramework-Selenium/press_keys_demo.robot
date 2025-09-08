*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
press keys demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window
    input text    //input[@id='autosuggest']    Samarth
    sleep    3
    press keys    //input[@id='autosuggest']    CTRL+a+DELETE    # executes ctrl+a+delete then releases
    # ctrl will not work I need to mention CTRL or CONTROL, similarily I need to mention the keys in expected format only.
    sleep    3

    press keys    //input[@id='autosuggest']    ABC
    sleep    3
    press keys    //input[@id='autosuggest']    CTRL+x
    sleep    3
    press keys    //input[@id='autosuggest']    CTRL+a+DELETE
    sleep    3
    press keys    //input[@id='autosuggest']    H+OmE

    press keys    //input[@id='autosuggest']    TAB
    sleep    3
    close browser

# if I want to enter any text which is not among any keys then 'ABC', it will press all at once & leave
# if I want to press any key, them 'TAB', this key is expected in a particular format & it should be given in that format only, else it will not work, so for referenec refer selenium keys.
# combo of keys i.e CTRL+a+DELETE    presss one after the other, keeping hold & finally releases every thing.
# if I want to eneter some text which is same as any key i.e. 'HOME' then i can use 'H+OME'

# Note: No need to specify shift or caps for upper case letter, if directly specified, it can identify it.