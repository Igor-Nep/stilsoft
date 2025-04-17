import os
import random
import msgpack
import requests
from PIL import Image
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService


with open('C:\work\WHPython\password', "rb") as data_file:
    password = msgpack.unpack(data_file)

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get('https://conf.stilsoft.ru/login')

driver.find_element(By.CSS_SELECTOR, '#authPage > div.page > div > div > div > div > form > div > div:nth-child(2) > input').send_keys('nepretimov_i')
driver.find_element(By.CSS_SELECTOR, '#authPage > div.page > div > div > div > div > form > div > div:nth-child(4) > input').send_keys(password)
driver.find_element(By.CSS_SELECTOR, '#authPage > div.page > div > div > div > div > form > div > div.form-footer > button').click()
sleep(3)
driver.find_element(By.CSS_SELECTOR, 'a.nav-link[href="/workers"]').click()
sleep(3)


users = {

 
     }

users2 = {}

user_index = 0

for k, v in users.items():
        try:
            user_index += 1
            user_name = v 
            user_lastname = k
            driver.get('https://corp.stilsoft.ru/workers')
            driver.find_element(By.CSS_SELECTOR, 'input[name="firstname"]').send_keys(user_name)
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, 'input[name="lastname"]').send_keys(user_lastname)
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '#wrapper > div > div.gridWorkersPage > div.searchWorkers > div > button').click()
            sleep(1)
            driver.find_element(By.CSS_SELECTOR, '#box > td.userData > div:nth-child(1) > div.userListFio > b > a').click()
            sleep(3)
            image = driver.find_element(By.CSS_SELECTOR, '#wrapper > div > div.workerPage_wrapper > div.workerPage_avatar > div > img')
            attribute_value = image.get_attribute("src")
            resp = requests.get(attribute_value)
            img_dir = 'c:/work/selen_images'
            os.makedirs(img_dir, exist_ok=True)
            img_path = os.path.join(img_dir, f'{k}_{v}.jpg')
            with open(img_path, 'wb') as img_file:
                img_file.write(resp.content)
            users2[k] = v
            
        except:
                continue        
        

collage_width = 0
collage_height = 0

a = 0
b = 0

up_down = [0, 400, 200]
rotator =[4, -4, 3, -3]

for k, v in users2.items():
     file = f'c:/work/selen_images/{k}_{v}.jpg'
     with Image.open(file) as file:
         collage_width += file.width
         if file.height >= collage_height:
             collage_height = file.height

collage = Image.new('RGB',(collage_width, collage_height), (250,250,250))
collage.save('c:/work/selen_images/collage.jpg')

for k, v in users2.items():
     add_file = f'c:/work/selen_images/{k}_{v}.jpg'
     with Image.open(add_file) as ad_image:
        width, height = ad_image.size
        left = 5
        top = height / 4
        right = 164
        bottom = 3 * height / 4
        ad1_image = ad_image.crop((left, top, right, bottom))
        add_image = ad1_image.rotate(int(random.choice(rotator)))
            
        try:
             collage = Image.open('c:/work/selen_images/collage.jpg')
             collage.paste(add_image,(a, int(random.choice(up_down))))
             a+=add_image.width
             collage.save('c:/work/selen_images/collage.jpg')
            
        except IOError:
            pass

#collage.show()

