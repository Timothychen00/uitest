*** Settings ***
Documentation     An example resource file
# Library           SeleniumLibrary
Library    ${CURDIR}/../Libraries/CustomSeleniumWireLibrary.py

*** Variables ***
@{type_cn}=    分類資料集    實體資料集    OCR資料集    SR資料集

*** Keywords ***
Move To Database
    [Arguments]    ${datasetname}
    Move To    xpath:.//*[contains(text(), '${datasetname}')]    precense

Click Side Button index
    [Arguments]    ${index}
    Click    xpath:.//*[@id="mat-tab-content-0-0"]/div/puzzle-sr-details/puzzle-side-menu/div/div/div[${index}]/img
Input In The New Class Inputbox
    [Arguments]    ${data}
    Input Text    xpath:.//*[@placeholder='請輸入欲新增標註類別名稱，字數上限 15 字元']    ${data}

Clear In The New Class Inputbox
    Clear Input    xpath:.//*[@placeholder='請輸入欲新增標註類別名稱，字數上限 15 字元']
    
Click New
    Click    xpath:.//*[@type='submit']

Click New Class
    Click    css:.add-btn