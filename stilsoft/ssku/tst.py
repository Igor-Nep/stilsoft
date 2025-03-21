import os,time
import json
with open('D:/work/WHPython/stilsoft/ssku/api/json/config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)
    ip = config['ip']
    login = config['login']
    password = config['password']
print(ip)
print(login)
print(password)
print(len(str((config['port']))))