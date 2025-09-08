*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${checkbox}    //input[@id='bmwcheck']

*** Test Cases ***
Handle Checkboxes
   open browser    https://www.letskodeit.com/practice    chrome
   maximize browser window

   # 1
   page should contain checkbox    ${checkbox}
   # Not contain also there

   # 2
   element should be visible    ${checkbox}
   # not visible is also there

   # 3
   element should be enabled    ${checkbox}
   # not enabled also there

   # 4
   checkbox should not be selected    ${checkbox}

   # 5
   select checkbox    ${checkbox}
   sleep    2

   # 6
   checkbox should be selected    ${checkbox}

   # 7
   unselect checkbox    ${checkbox}
   sleep    2

   close browser

# Note
# - Multiple checkboxes can be selected
# - Note if the locator matches the multiple checkboxes, only first checkbox will be selected.