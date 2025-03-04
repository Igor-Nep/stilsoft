import requests


url = 'https://gate.synerget.ru:8179'

def get_token(login='admin', password='adm777'): 
        creds = {       
            'login': login,
            'password': password,
            "hash": "edab4970-4d9b-11ef-a454-b1120eae1a88"
            }
        resp = requests.post(url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        my_token = {
            'Authorization': bearer
        }
        return my_token

def get_modules(cam_tit): 
        resp = requests.get(url+'/api/data/system/module', headers=get_token(), verify=False)
        for item in resp.json()['data']:
                
                if item['title'] == cam_tit:
                        return (item['id'])


        

print(get_modules('tst_media_drop'))