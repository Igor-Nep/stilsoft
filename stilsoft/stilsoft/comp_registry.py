import requests
import json
import os
import warnings

base_url = 'https://gate.synerget.ru:8179'

path_string=''

body = json.loads('{'+f'"path": "{path_string}"'+'}')
resp = requests.post(base_url+'/api/registry/packages', json=body, verify = False)
print(resp)