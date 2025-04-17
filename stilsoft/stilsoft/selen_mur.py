from selenium import webdriver
from selenium.webdriver.common.by import By
#from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options
#from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FoxService
#from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep
import os

os.system('c:/Users/nepretimov_i/Desktop/rc-5.0.9_murom-5.0.8.779-desktop-win32-x64/murom-desktop.exe --args --remote-debugging-port=9515')

opt = Options() 
print('init Options')
#chrome_options.add_argument('--remote-debugging-port=9222')
opt.add_argument('--remote-debugging-port=9515')
#opt.debugger_address('localhost:9515')
opt.add_argument('ignore-certificate-errors')
print('Init port ')
#driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()), options = options) 
#driver = webdriver.Firefox(service = FoxService(GeckoDriverManager().install()), options = options)
driver = webdriver.Firefox("C:/work/WHPython/stilsoft/geckodriver.exe")
driver.options=opt
#driver = webdriver.Chrome(options = options)
print('Set options')
#print(driver.title)
driver.find_element(By.CSS_SELECTOR, 'input[data-testid="login"]').send_keys('admin')                   
#driver.find_element(By.XPATH)     


driver.quit()
