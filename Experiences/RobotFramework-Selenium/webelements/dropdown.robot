*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${dropdown}    //select[@id='carselect']

*** Test Cases ***
handle dropdown
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

    select from list by label    ${dropdown}    Honda
    # In locator I need to give the locator of the dropdown not options in it
    sleep    3

# In dropdown i can usually select only one option, but there can be multi select dropdown as well.
    select from list by value    ${dropdown}    bmw
    sleep    3

    select from list by index    ${dropdown}    2
    sleep    3
   # Indexing starts from 0 in dropdown & listbox options i.e. list options

   close browser

# Note
# - There will be multi select dropdown as well, for selecting the options from that I can use same 'select from list by ...' keyword multiple times.
# - In case of multi select dropdown, i can unslect as well, for that
    # unselect from list by ... keyword I can use.


