import pyautogui
# from selenium import webdriver
from seleniumwire import webdriver
from selenium.webdriver.common.by import By

def initialize(position=''):
    options = webdriver.EdgeOptions()
    options.add_argument('--ignore-ssl-errors=yes')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--no-zygote')
    options.add_argument('--disable-http2')
    # options.page_load_strategy = 'eager'
    width, height = pyautogui.size()
    driver = webdriver.Edge(options=options)
    
    #設定window的位置
    startY=0
    startX=0
    if position=='right':
        startX=width//2

    driver.set_window_position(startX,startY)
    #設定window size
    if position=="":
        driver.set_window_size(width,height)
    else:
        driver.set_window_size(width//2,height)
    return driver
