*** Settings ***
Documentation     An example resource file
# Library           SeleniumLibrary
Library    ${CURDIR}/../Libraries/CustomSeleniumWireLibrary.py

*** Variables ***
@{type_cn}=    分類資料集    實體資料集    OCR資料集    SR資料集

*** Keywords ***
Type Dataset Name
    [Arguments]    ${name}
    Input Text    xpath:.//*[@formcontrolname='datasetName']    ${name}
            
            
Choose Dataset Type
    [Arguments]    ${type}
    Click    xpath:.//*[@placeholder="請選擇資料集類型"]
    ${index}=    Evaluate    ${type_cn}.index("${type}")
    Click    xpath://*[@id="mat-option-${index}"]//*

Choose Dataset Language    # SR資料集的時候不會用到
    [Arguments]    ${type}
    Click    xpath:.//*[@placeholder="請選擇語系"]
    Click    xpath:.//*span[contains(text(), '${type}')]

Submit Dataset 
    Click    xpath://*[@type='submit']

Open Dataset
    [Arguments]    ${datasetname}
    Click    xpath:.//*[contains(text(), '${datasetname}')]    precense

