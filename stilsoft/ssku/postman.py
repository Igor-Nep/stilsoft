import requests, msgpack, json, os, warnings

class Postman():

    def __init__(self, url='https://gate.synerget.ru:8179'):
        warnings.filterwarnings('ignore')
        self.url = url
        self.ip = self.hosts()

        self.servers = {"192.168.202.238":{"name":"user","password":"stilsoft","type":"murom"},
                        "192.168.202.30":{"name":"user","password":"stilsoft","type":"murom"},
                        "192.168.202.10":{"name":"user","password":"stilsoft","type":"ssku"},
                        "192.168.207.68":{"name":"user","password":"stilsoft1","type":"ssku"}
                        }


    def check(self):
        print(self.servers[self.ip]['type'])

    
    def hosts(self):
        host_file = open('c:/windows/system32/drivers/etc/hosts', 'r', encoding='utf-8')
        active_host=[]
        len_host = int(len(host_file.readlines()))
        host_file.seek(0,0)
        for _ in range(0, len_host):
            s = host_file.readline()
        if '#' not in s:
            active_host.append(s)
        active_host = [item.replace('gate.synerget.ru', '') for item in active_host]            
        return active_host[0].strip()#.lstrip('\ufeff')


    def get_token(self, login ='admin', password='adm777'):
        creds = {       
            'login': login,
            'password': password
            } if self.servers[self.ip]['type'] == 'murom' else {       
            'login': login,
            'password': password,
            'hash': 'edab4970-4d9b-11ef-a454-b1120eae1a88'
            }
        resp = requests.post(self.url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        my_token = {
            'Authorization': bearer
        }
        return my_token


    def make_json(self, pre_body):
        with open(pre_body, 'r') as file:
            body_ = json.load(file)
            body = json.dumps(body_)
            body = json.loads(body)
            #body = body.replace
            return body



    def get(self, url):
        zone_id = []
        resp = requests.get(self.url+f'{url}',headers=self.get_token(), verify=False)
        for i in range(len(resp.json()['data'])):
            if resp.json()['data'][i]['nestedZones'] != []:
                zone_id.append(resp.json()['data'][i]['id'])
                print(resp.json()['data'][i]['nestedZones'][0]['id'])
                print(len(resp.json()['data'][i]['nestedZones']))
        for i in zone_id:
            #print(f'self.url+{url}/{i}')
            resp = requests.get(self.url+f'{url}/{i}',headers=self.get_token(), verify=False)
          
            if 'хопа' in resp.json()['data']:
                print(i)

    def get_sub_zones(self, url):
        zone_id = []
        sub_zone_id = []
        resp = requests.get(self.url+f'{url}',headers=self.get_token(), verify=False)
        for i in range(len(resp.json()['data'])):
            if resp.json()['data'][i]['nestedZones'] != []:
                zone_id.append(resp.json()['data'][i]['id'])
                print('_'*20)
                print(f'Объект: {resp.json()['data'][i]['title']}')
                
                print(f'Количество вложенных объектов: {len(resp.json()['data'][i]['nestedZones'])}')
                for n in range(len(resp.json()['data'][i]['nestedZones'])):
                    sub_zone_id.append(resp.json()['data'][i]['nestedZones'][n]['id'])
                    print(f'{n} - {resp.json()['data'][i]['nestedZones'][n]['title']}')
                    

        for i in sub_zone_id:
            #print(f'self.url+{url}/{i}')
            resp = requests.get(self.url+f'{url}/{i}',headers=self.get_token(), verify=False)
          
            if 'хопа' in resp.json()['data'][0]['title']:
                print(f'FINDED {i}')




    def delete(self, url):
        resp = requests.delete(self.url+f'{url}',headers=self.get_token(), verify=False)
        print(resp.json())    


    def post(self, url):
        from api import ApiSsku
        id = ApiSsku().get_user_id()
        body = self.make_json('D:\work\WHPython\stilsoft\ssku\postman/body.json')
        #body_ = json.dumps(body)
        #body_ = body_.replace("%%ID%%", id)
        #body = json.loads(body_)
        resp = requests.post(self.url+f'{url}',headers=self.get_token(), json=body, verify=False)
        print(resp.json()['data'][0]['timestamp'])

   # def post(self, url, body):

   #         pre_body =

    def put_anal(self):
        from api import ApiSsku
        body_ = {"data":{"detectionEnabled":False,"minConfidence":0.3}}
        resp = requests.put(self.url+f'/api/data/system/objectlink/{ApiSsku().get_module_by_name('Камера 10000')}',headers=self.get_token(), json=body_, verify=False)
        print(resp.json())
        