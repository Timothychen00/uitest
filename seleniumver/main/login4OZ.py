import os
import time

from icecream import ic
from dotenv import load_dotenv
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
driver.get('https://192.168.118.159:8443/OZ/')

wait_load_elements(driver,By.CSS_SELECTOR,'[placeholder]')[0].send_keys(f'{os.environ["username1"]}')
wait_load_elements(driver,By.CSS_SELECTOR,'[placeholder]')[1].send_keys(f'{os.environ["password1"]}')
wait_load_element(driver,By.CSS_SELECTOR,'[name=checkImg]').click()
time.sleep(2)

for request in driver.requests:
    ic(request.url)
 
#     # 根据自己的需求找出请求
    if 'getCheckCode' in request.url:
        import json
        data=json.loads(request.response.body.decode())
        ic(data[1])
        # ic(data['getCheckCode'])
wait_load_elements(driver,By.CSS_SELECTOR,'[placeholder]')[2].send_keys(f'{data[1]}')
# # for request in driver.requests:
# #     print(request,request.headers,request.response)
 
# #     # 根据自己的需求找出请求
# #     if request.response and "x-signature" in request.headers:
# #         print(request.headers["x-signature"])
# wait_load_element(driver,By.CSS_SELECTOR,'[type=submit]').click()
time.sleep(40)
driver.quit()

#把所有的find_element替換成，等待直到目標物件可見，再回傳
