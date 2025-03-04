import time
import os
import requests
import json
import tkinter as tk
from tkinter import * 
from tkinter import messagebox

scr = tk.Tk()
scr.geometry('500x250')
scr.title('Get token')
token_expiration_time = 3600  # Срок действия токена в секундах (например, 1 час)
current_time = int(time.time())  # Текущее время в секундах

# Получаем токен и время его получения из переменных окружения
access_token = os.getenv("access_token")
token_timestamp = os.getenv("token_timestamp")

# Проверяем, есть ли токен и не истек ли его срок действия
if not access_token or (current_time - int(token_timestamp)) >= token_expiration_time:
    print("Токен отсутствует или истек. Запрашиваем новый токен...")

    # Если токена нет или он истек, выполняем запрос для получения нового токена
    url = "https://gate.synerget.ru:8179/api/auth/login"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "login": "admin",
        "password": "adm777"
    }

    response = requests.post(url, headers=headers, data=json.dumps(data), verify=False)

    if response.status_code != 200:
        print("Ошибка при получении токена:", response.text)
    else:
        json_data = response.json()

        if "access_token" in json_data:
            os.environ["access_token"] = json_data["access_token"]
            os.environ["token_timestamp"] = str(current_time)
            print("Новый токен получен и сохранен:", json_data["access_token"])

            # Установим Authorization заголовок для текущего запроса
            headers["Authorization"] = "Bearer " + json_data["access_token"]
        else:
            print("Не удалось получить токен. Ответ сервера не содержит 'access_token'.")
else:
    # Если токен действителен, добавим его к заголовку Authorization
    print("Используем существующий токен:", access_token)
    headers = {
        "Authorization": "Bearer " + access_token
    }
scr.mainloop()
# Пример использования заголовка Authorization в последующем запросе
# response = requests.get("https://example.com/api/data", headers=headers)