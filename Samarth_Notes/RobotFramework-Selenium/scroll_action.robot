*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
scroll action demo
    open browser    https://www.letskodeit.com/practice    chrome
    maximize browser window

   scroll element into view    //td[.='JavaScript Programming Language']
   sleep    3
   close browser

# If a certain element is in the very down of the page & selenium somehow is not able to identify the element, then may be that element will be generated on that webpage after scrolling
# In such cases first scroll to the last identified element in the page & then again scroll ...