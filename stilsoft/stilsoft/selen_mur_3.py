from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

cap = DesiredCapabilities.CHROME.copy()
cap['goog:chromeOptions'] = {'binary': "c:/Users/nepretimov_i/Desktop/rc-5.0.8_murom-5.0.8.766-desktop-win32-x64/murom-desktop.exe", 'args': ['--no-sandbox','--remote-debugging-port=7070']}

driver = webdriver.Remote(command_executor='http://localhost:9515', options = cap)