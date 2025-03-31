import requests,os,warnings

url='https://gate.synerget.ru:8179'


def get_token(login='admin', password='adm777'):
        creds = {       
            'login': login,
            'password': password,
            'hash': 'Nepb4970-4d9b-11ef-a454-b1120eae1a88'
            }
        resp = requests.post(url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        
        token = {
            'Authorization': bearer
        }
        return token


token = get_token()


def get_module_count():
    resp = requests.get(url+'/api/data/system/module', headers=token, verify=False)
    return int(len(resp.json()['data']))


def get_module_id_by_type(i, type):
    resp = requests.get(url+'/api/data/system/module', headers=token, verify=False)
    if resp.json()['data'][i]['type'] == type:
        return resp.json()['data'][i]['id']


def mode_mediamtx(mode):
        warnings.filterwarnings('ignore')
        os.system('cls')
        module_list = []
        for i in range(get_module_count()):
             module_list.append(get_module_id_by_type(i,'sdp858i'))
        if mode == 'on':
             body={"settings":{"useMediamtx": True}}
        else:
             body={"settings":{"useMediamtx": False}}     

        for id in module_list:
            requests.put(url +f'/api/data/system/module/{id}', headers=token, json=body, verify=False)
            os.system('cls')
            print(f'{module_list.index(id)+1} / {len(module_list)}')


mode_mediamtx('on')