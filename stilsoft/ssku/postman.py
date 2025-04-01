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
        resp = requests.get(self.url+f'{url}',headers=self.get_token(), verify=False)
        print(resp.json())

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
