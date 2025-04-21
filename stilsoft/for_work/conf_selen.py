import requests

url = "https://conf.stilsoft.ru/login" 
payload = {
       'os_username': 'nepretimov_i',
       'os_password': '625RjrDgeDhe',
       "login": "log+in"
   }
response = requests.post(url, json=payload, verify = False)


token = response.json()
print(f"Ваш токен: {token}")
