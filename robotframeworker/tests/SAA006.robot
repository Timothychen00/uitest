*** Variables***
${datasetname}    
*** Settings ***
Documentation    標註類別名稱字數限制
# Suite Setup + 关键字语句
Suite Setup    Clear Folder
Suite Teardown    Close Browser
Test Teardown    Screenshot Element    ${TEST NAME}    
Resource    ${CURDIR}/../resouces/PageDataSets.resource
Resource    ${CURDIR}/../resouces/PageEachDataSet.resource
Resource    ${CURDIR}/../resouces/general.resource
Library    ${CURDIR}/../Libraries/CustomSeleniumWireLibrary.py    

*** Keywords ***

*** Test Cases ***
Setup For Test
    [Documentation]    準備systalk的測試環境
    [Tags]    test:retry(2)
    [Timeout]
    ${driver}=    Create Driver    full_page
    Log    ${driver}  console=True
    Go To    http://192.168.118.36/login
    Log In To Systalk       timothychen123    123123123Tt!!!
    Go To Database
    Sleep    2s
    Switch Tab

Pre-conditions
    [Documentation]    先建立一份新的SR資料集，並進入內頁
    [Tags]    test:retry(2)
    [Timeout]
    ${datasetname}=     Random   5

    Click    css:.stai-button
    Type Dataset Name    ${datasetname}
    Choose Dataset Type    SR資料集
    Submit Dataset 
    Check To Be Displayed    css:.stacked-toasts
    Move To Database    ${datasetname}
    Open Dataset    ${datasetname}

Step1
    [Documentation]    [Action]點擊側邊欄第三個icon->[Expected Result]打開標註類別列表分頁
    [Tags]    test:retry(2)
    [Timeout]
    Click Side Button index    3

Step2
    [Documentation]    [Action]點擊 新增類別 按鈕->[Expected Result]開啟新增類別視窗
    [Timeout]
    [Tags]    test:retry(2)
    Click    css:.add-btn

Step3
    [Documentation]    [Action]輸入 0123401234012345->[Expected Result]成功輸入
    [Tags]    test:retry(2)
    [Timeout]
    Input In the New Class Inputbox    0123401234012345
Step4
    [Documentation]    [Action]點擊 新增 按鈕->[Expected Result]無法成功新增出現紅色hint「請至少輸入1~15個字元，且不得重複既有標註類別名稱」
    [Tags]    test:retry(2)
    [Timeout]
    Check To Be Not Displayed    css:.form-erro

Step5
    [Documentation]    [Action]改為僅輸入 0    ->    [Expected Result]成功輸入
    [Tags]    test:retry(2)
    [Timeout]
    Clear In the New Class Inputbox
    Input In the New Class Inputbox    0

Step6
    [Documentation]    [Action]點擊 新增 按鈕    ->    [Expected Result]成功新增
    [Tags]    test:retry(2)
    [Timeout]
    Check To Be Empty    css:.form-erro
    Click New    
    
Step7:
    [Documentation]    [Action]清除輸入內容    ->    [Expected Result]成功清除
    [Tags]    test:retry(2)
    [Timeout]
    
    Click New Class
    Check To Be Not Displayed    css:.form-erro

Step8:
    [Documentation]    [Action]點擊 新增 按鈕    ->    [Expected Result]新增按鈕disable出現紅色hint「請至少輸入1~15個字元，且不得重複既有標註類別名稱」
    [Tags]    test:retry(2)
    [Timeout]
    Sleep    3s
    # Click    css:.add-btn   
    Input In the New Class Inputbox    0
    Check To Be Displayed    css:.stacked-toasts
