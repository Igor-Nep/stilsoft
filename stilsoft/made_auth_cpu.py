from ApiSsku import ApiSsku
import requests
import msgpack
import json
import os
import time
from time import sleep
import warnings

base_url = 'https://gate.synerget.ru:8179'
api = ApiSsku(base_url)


def made_user():
    warnings.filterwarnings('ignore')
    name = 'test_auth_cpu'
    login = 'test_auth_cpu'
    password = 'test_auth_cpu'

    b = '{'+f'"name":"{name}","login":"{login}","password":"{password}","confirmPassword":"{password}","role":"operator-cpu","surname":"","middleName":""'+'}'
    body =json.loads(b)
    make = requests.post(base_url+'/api/data/security/user', headers=api.get_token(), json=body, verify=False)
    print(make)
    req = requests.get(base_url+'/api/data/security/user', headers=api.get_token(), verify=False)
        
    for i in range(0, int(len(req.json()['data']))):
        sts_ch = (req.json()['data'][i]['name'])
        
        if sts_ch == 'test_auth_cpu':
            d = int(i)
        
    user_id = requests.get(base_url+'/api/data/security/user', headers=api.get_token(), verify=False)
    print(user_id.json()['data'][d]['id'])
    print(user_id.json()['data'][d]['login'])

made_user()    
    
