*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
implicit wait demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

   # Note :
   # implicit wait is basically the time that selenium takes before throwing the exception when it doesn't find the element on HTLM DOM
   # By default implicit wait is 0 secs.

   set selenium implicit wait    10
   select checkbox    //input[@id='bmwcheck']
   close browser
# disadvantages
# It will only check for the presence of the element on DOM not it's visibility & clickability on the webpage, so it's not reliable.
# # If our expected result aims to validate a particular element should not be present(page should not contain element) on the webpage, then at that time it will wait for max specified time trying to find the element, eventhough the expectation is met in 1st second, then the keyword finally passes.