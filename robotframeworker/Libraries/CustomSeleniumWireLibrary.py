import os
import random

from icecream import ic
import pyautogui
from seleniumwire import webdriver
from robot.api import logger
from robot.libraries.BuiltIn import BuiltIn
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains 
from selenium.webdriver.common.by import By

class CustomSeleniumWireLibrary():
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'
    def __init__(self):
        pass
    
    #initialization----------------------------------------
    
    def create_driver(self,position):
        
        options = webdriver.EdgeOptions()
        options.add_argument('--ignore-ssl-errors=yes')
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--disable-http2')
        # options.add_argument('--no-zygote')
        # options.page_load_strategy = 'eager'
        width, height = pyautogui.size()
        self.driver = webdriver.Edge(options=options)
        
        #設定window的位置
        startY=0
        startX=0
        if position=='right':
            startX=width//2

        self.driver.set_window_position(startX,startY)
        #設定window size
        if position=="full_page":
            self.driver.set_window_size(width,height)
        else:
            self.driver.set_window_size(width//2,height)
            
        self.driver.set_page_load_timeout(120)

        return self.driver
    
    #general purpose----------------------------------------
    
    def go_to(self,url):
        self.driver.get(url)

    def wait_elements_until(self,selector_para,depend='visible'):
        try:
            logger.debug('[wait_elements_until]'+depend)
            index=selector_para.index(':')
            selector=selector_para[:index]
            selector_dict={'css':By.CSS_SELECTOR,'xpath':By.XPATH}
            selector=selector_dict[selector]
            para=selector_para[index+1:]
            logger.debug("[wait_elements_until]"+selector)
            logger.debug("[wait_elements_until]"+para)
            if depend=='visible':
                WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((selector,para)))
            elif depend=='clickable':
                WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((selector,para)))
            else:
                WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((selector,para)))
            elements=self.driver.find_elements(selector,para)
            logger.debug("[wait_elements_until]"+'elements get!')
            return elements
        
        except Exception as e:
            logger.error('[wait_elements_until]error')
            logger.error(e)
            return None
    
    def wait_element_until(self,selector_para,depend='visible'):#visibility_of_element_located/presence_of_element_located
        try:
            logger.debug('[wait_element_until]'+depend)
            index=selector_para.index(':')
            selector=selector_para[:index]
            selector_dict={'css':By.CSS_SELECTOR,'xpath':By.XPATH}
            selector=selector_dict[selector]
            para=selector_para[index+1:]
            
            logger.debug("[wait_element_until]"+selector)
            logger.debug("[wait_element_until]"+para)
            if depend=='visible':
                element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located((selector,para)))
            elif depend=='clickable':
                element= WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((selector,para)))
            else:
                element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((selector,para)))
            logger.debug("[wait_element_until]"+'element get!')
            return element
        except Exception as e:
            logger.error('[wait_element_until]error')
            logger.error(e)
            return None
    
    def switch_tab(self):
        chwd = self.driver.window_handles
        p = self.driver.current_window_handle
        for w in chwd:
            if(w!=p):
                self.driver.switch_to.window(w)
        logger.debug('[switch_tab]success')
            
    def get_requests(self):
        """Get the HTTP requests captured by Selenium Wire."""
        return self.driver.requests
    
    def input_text(self,selector_para,data):
        self.wait_element_until(selector_para).send_keys(data)
        logger.debug("[input_text]finish")
        
    def click(self,selector_para,depend='clickable'):#預設等待clickable再進行點擊
        ele=self.wait_element_until(selector_para,depend)
        ele.click()
        logger.debug('clicked')
        
    def close_browser(self):
        """Close the browser."""
        if self.driver:
            self.driver.quit()
    
    def is_displayed(self,selector_para):
        element=self.wait_element_until(selector_para,'precense')
        return element.is_displayed()
    
    def move_to(self,selector_para,depend='visible'):
        action = ActionChains(self.driver) 
        element=self.wait_element_until(selector_para,depend)
        action.move_to_element(element).perform() 

    def screenshot_element(self,name,selector_para='css:body',depend='visible'):
        element=self.wait_element_until(selector_para,depend)
        element.screenshot(f'screenshots/{name}.png')
        
    def clear_folder(self,foldername='screenshots'):
        os.system('rm -rf screenshots/*')
        
    
    def load_env_var(self,key):
        result=os.environ.get(key,None)
        if not result:
            logger.error('[load_env_var]not found key')
            
    def is_empty(self,selector_para):
        ele=self.wait_element_until(selector_para,'located')
        son=ele.find_elements(By.XPATH,'.//*')
        if not son:
            return True
        return (son[0].get_attribute('outerHTML'),son[0].get_attribute('innerHTML'),len(list(son)))
        
    def clear_input(self,selector_para):
        self.wait_element_until(selector_para).clear()
        
    #special----------------------------------------
    
    def get_check_code(self):
        for request in self.driver.requests:
        #     # 根据自己的需求找出请求
            if 'recaptcha' in request.url:
                import json
                data=json.loads(request.response.body.decode())
                logger.debug(data['captchaCode'])
                return data['captchaCode']
    
    def log_in_to_systalk(self,username,password):
        self.wait_elements_until('css:[placeholder]')[0].send_keys(f'{username}')
        self.wait_elements_until('css:[placeholder]')[1].send_keys(f'{password}')
        checkCode=self.get_check_code()
        logger.debug(f"checkCode:{checkCode}")
        self.wait_elements_until('css:[placeholder]')[2].send_keys(f'{checkCode}')
        self.wait_element_until('css:[type=submit]','clickable').click()
        logger.debug(f"submitted!")
    
    def go_to_database(self):
        action = ActionChains(self.driver) 
        element=self.wait_element_until("css:#productHover")
        action.move_to_element(element).perform() 
        #productHover
        self.wait_element_until('css:#productButtons > button','clickable').click()
        logger.debug("go_to_database-done")

    def random(self,length):
        return ''.join(random.sample('1234567890abcdefghijklmnopqrstuvwxyz',int(length)))
