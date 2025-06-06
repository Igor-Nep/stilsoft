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
        
        host_file =  open('c:/windows/system32/drivers/etc/hosts', 'r')
        len_host = int(len(host_file.readlines()))
        host_file.seek(0,0)
        active_host = []
        for _ in range(0, len_host):
            s = host_file.readline()#.split(' ')[0]
            if '#' not in s:
                active_host.append(s)
        newti=str(active_host[0])
        self.terminal('blue',(newti))
        host_file.close()


    def check(self):
        print(self.servers[self.ip]['type'])


    def cls(self):
        import sys
        sys.stdout.write('\r' + ' ' * 100 + '\r')
        sys.stdout.flush()        

    def status(self,status_code):
        if status_code == 200:
            self.terminal('green',status_code)
        elif 399<status_code<499:
            self.terminal('yellow',status_code)
        elif 499<status_code<500:
            self.terminal('red',status_code)
        else:
            self.terminal('non',status_code)


    def terminal(self,paint,text,nextrow=True):
        import sys
        from color import color
        self.cls()
        if paint == 'yellow':
            sys.stdout.write(f'{color.grey('[')}{color.yellow(f'{text}')}{color.grey(']')}')
        elif paint == 'green':
            sys.stdout.write(f'{color.grey('[')}{color.green(f'{text}')}{color.grey(']')}')
        elif paint == 'red':
            sys.stdout.write(f'{color.grey('[')}{color.red(f'{text}')}{color.grey(']')}')
        elif paint == 'blue':
            sys.stdout.write(f'{color.grey('[')}{color.blue(f'{text}')}{color.grey(']')}')
        elif paint == 'grey':
            sys.stdout.write(f'{color.grey('[')}{color.grey(f'{text}')}{color.grey(']')}')
        elif paint == 'non':
            sys.stdout.write(f'{color.grey('[')}{color.non(f'{text}')}{color.grey(']')}')
        elif paint == 'mod':    
            sys.stdout.write(f'{color.grey('[')}{text}{color.grey(']')}')
        sys.stdout.flush()
        if nextrow:
            sys.stdout.write('\n')

    
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


    def get(self,url):
        try:
            resp = requests.get(self.url+f'{url}',headers=self.get_token(),verify=False)
        except Exception as err:
            self.terminal('mod','can not make request')
            self.terminal('red',err)
        try:        
            self.terminal('yellow','body:')
            self.terminal('mod',resp.json())
        except Exception as err:
            self.terminal('red',err) 
        try:       
            self.status(resp.status_code)
        except Exception as err:
            self.terminal('red',err)    



    def delete(self, url):
        try:
            resp = requests.delete(self.url+f'{url}',headers=self.get_token(), verify=False)
        except Exception as err:
            self.terminal('mod','can not make request')
            self.terminal('red',err)
        try:
            self.terminal('yellow','body:')
            print(resp.json())#['data'][0]['timestamp'])
        except Exception as err:
            self.terminal('yellow','none')
            self.terminal('red',err)
        try:        
            self.status(resp.status_code)   
        except Exception as err:
            self.terminal('red',err)    


    def post(self,url,body='body.json'):
        from api import ApiSsku       
        data = self.make_json(f'D:\work\WHPython\stilsoft\ssku\postman\{body}')
        #body_ = json.dumps(body)
        #body_ = body_.replace("%%ID%%", id)
        #body = json.loads(body_)
        try:
            resp = requests.post(self.url+f'{url}',headers=self.get_token(), json=data, verify=False)
        except Exception as err:
            self.terminal('mod','can not make request')
            self.terminal('red',err)            
        try:
            self.terminal('yellow','body:')
            print(resp.json())#['data'][0]['timestamp'])
        except Exception as err:
            self.terminal('yellow','none')
            self.terminal('red',err)
        try:        
            self.status(resp.status_code)
        except Exception as err:
            self.terminal('red',err)    

    def put_anal(self):
        from api import ApiSsku
        body_ = {"data":{"detectionEnabled":False,"minConfidence":0.3}}
        resp = requests.put(self.url+f'/api/data/system/objectlink/{ApiSsku().get_module_by_name('Камера 10000')}',headers=self.get_token(), json=body_, verify=False)
        print(resp.json())
        