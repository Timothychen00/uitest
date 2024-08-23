
*** Settings ***
Documentation     An example resource file
# Library           SeleniumLibrary
Library    ${CURDIR}/../Libraries/CustomSeleniumWireLibrary.py



*** Keywords ***
Check To Be Displayed
    [Arguments]    ${selector}
    ${is_displayed}=    Is Displayed    ${selector}
    Should Be Equal    ${is_displayed}    ${False}

Check To Be Not Displayed
    [Arguments]    ${selector}
    ${is_displayed}=    Is Displayed    ${selector}
    Should Be Equal    ${is_displayed}    ${True}

Check To Be Empty
    [Arguments]    ${selector}
    ${is_empty}=    Is Empty    ${selector}
    Should Be Equal    ${is_empty}    ${True}

