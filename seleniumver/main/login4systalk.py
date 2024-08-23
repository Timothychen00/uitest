import os
import time

from icecream import ic
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By

from __init__ import initialize

load_dotenv()

def wait_load_element(driver,selector,para):#visibility_of_element_located/presence_of_element_located
    element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((selector, para)))
    return element

def wait_load_elements(driver,selector,para):#visibility_of_element_located/presence_of_element_located
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((selector, para)))
    elements=driver.find_elements(selector,para)
    return elements

driver=initialize()
driver.get('http://192.168.118.36/login')

wait_load_elements(driver,By.CSS_SELECTOR,'[placeholder]')[0].send_keys(f'{os.environ["username"]}')
wait_load_elements(driver,By.CSS_SELECTOR,'[placeholder]')[1].send_keys(f'{os.environ["password"]}')

for request in driver.requests:
    ic(request.url)
 
#     # 根据自己的需求找出请求
    if 'recaptcha' in request.url:
        import json
        data=json.loads(request.response.body.decode())
        ic(data)
        ic(data['captchaCode'])
wait_load_elements(driver,By.CSS_SELECTOR,'[placeholder]')[2].send_keys(f'{data["captchaCode"]}')
wait_load_element(driver,By.CSS_SELECTOR,'[type=submit]').click()

#productButtons > button
# driver.get("https://192.168.118.90/datasets")# 不能直接get過去

action = ActionChains(driver) 
element=wait_load_element(driver,By.CSS_SELECTOR,"#productHover")
action.move_to_element(element).perform() 

#productHover
wait_load_element(driver,By.CSS_SELECTOR,'#productButtons > button').click()
time.sleep(2)
chwd = driver.window_handles
p = driver.current_window_handle
for w in chwd:
    if(w!=p):
        driver.switch_to.window(w)
ic('tabbed')
wait_load_element(driver,By.CSS_SELECTOR,'.stai-button').click()
wait_load_element(driver,By.XPATH,".//*[@formcontrolname='datasetName']").send_keys('kkkkkkk')
wait_load_element(driver,By.XPATH,'.//*[@placeholder="請選擇資料集類型"]').click()
wait_load_element(driver,By.XPATH,'//*[@id="mat-option-3"]').click()
wait_load_element(driver,By.XPATH,"//*[@type='submit']").click()

action = ActionChains(driver) 
element=wait_load_element(driver,By.XPATH,".//*[contains(text(), 'kkkkkkk')]")
action.move_to_element(element).perform() 
wait_load_element(driver,By.XPATH,".//*[contains(text(), 'kkkkkkk')]").click()
time.sleep(1)
driver.quit()

#把所有的find_element替換成，等待直到目標物件可見，再回傳
