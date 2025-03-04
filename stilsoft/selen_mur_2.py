from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from time import sleep

options = Options()
options.binary_location = "C:/Users/nepretimov_i/Desktop/rc-5.0.9_murom-5.0.8.779-desktop-win32-x64/murom-desktop.exe -devtools"
options.debugger_address = 'localhost:9515'

driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options) 
sleep(5)
driver.find_element(By.XPATH,'/html/body/div/div[2]/div/div[2]/div[1]/form/div[1]/div[1]/input').send_keys('admin')
sleep(5)



