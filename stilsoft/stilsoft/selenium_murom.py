import time
import re
from selenium import webdriver
import webbrowser
import sys
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
    
browser = webdriver.Firefox()
    
browser.get('https://example.com')
    
userid = browser.find_element_by_id('user')
time.sleep(1)
userpass = browser.find_element_by_id('password')
time.sleep(1)
userid.send_keys('aafasdf@gmail.com')
time.sleep(1)
userpass.send_keys('#jlasdjf#')
    
    
time.sleep(1)
userid.send_keys(Keys.RETURN)
userid.clear()
browser.refresh()
time.sleep(5)
print('Hello from Python!')
sys.stdout.flush()

