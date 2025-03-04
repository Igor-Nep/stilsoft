from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.chrome.service import Service

chromedriver_path = "C:/work/WHPython/stilsoft/chromedriver.exe"
electron_path = "C:/Users/nepretimov_i/Desktop/rc-5.0.9_murom-5.0.8.779-desktop-win32-x64/murom-desktop.exe -devtools"

opts = Options()
opts.binary_location = electron_path
service = Service(executable_path="C:/work/WHPython/stilsoft/chromedriver.exe")
driver = webdriver.Chrome(service=service, options=opts)
driver.implicitly_wait(15)

time.sleep(3) # отладочные слипы)
el = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#app > div.app-layout-auth > div > div.auth__activity > div.auth-form.auth__activity-form > form > div:nth-child(1) > div.app-input__wrapper > input")))
el.send_keys('1234567890')
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, "#app > div.app-layout-auth > div > div.auth__activity > div.auth-form.auth__activity-form > form > button").click()
time.sleep(3)
driver.quit()
