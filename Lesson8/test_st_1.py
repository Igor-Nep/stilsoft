import os
import requests
import json
base_url = 'https://gate.synerget.ru:8179'

def get_token(user = "admin", password = "adm777"):
  creds = {       
          'login': user,
            'password': password
    }
  resp = requests.post(base_url+'/api/auth/login', json=creds, verify=False)
  bearer = (f'Bearer {resp.json()["access_token"]}')
  my_token = {
      'Authorization': bearer
    }
  return my_token

def test_requests():
    
    #my_token = {}
    #my_token["access_token"] = get_token()
    token = get_token()   
    
     
    resp = requests.get(base_url+'/api/data/system/module', headers=get_token(),verify=False)
  
    assert resp.status_code == 200
      

