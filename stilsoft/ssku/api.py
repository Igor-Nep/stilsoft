 
import requests
import datetime
import pytz
import warnings
import os
import msgpack
import random
import json
import time
from time import sleep
from color import color

class ApiSsku():

    glob_start_time = time.time()
    token = ''

    def __init__(self, ip, url='https://gate.synerget.ru:8179'):
        warnings.filterwarnings('ignore')
        self.url = url
        self.ip = ip
        with open('c:/windows/system32/drivers/etc/hosts', 'r') as host_file:
   
            len_host = int(len(host_file.readlines()))
            host_file.seek(0,0)
            for _ in range(0, len_host):
                s = host_file.readline()
                if self.ip not in s:
                    print('\033[5;31m[WRONG SERVER IN HOSTS]\033[0m')
                    sleep(3)
                    exit()            


    def cls(self):
        import sys
        sys.stdout.write('\r' + ' ' * 100 + '\r')
        sys.stdout.flush() 


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


    
    def get_token(self, login='admin', password='adm777'):
        creds = {       
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
    

    def refresh_token(self):

            if self.token == '':
                self.token = self.get_token()

            elif time.time()-self.glob_start_time>359.0:

                self.token = self.get_token()
                self.glob_start_time = time.time()
            
            else:
                self.token = self.token

              

    def refresh_file_token(self):
        warnings.filterwarnings('ignore')
        os.system('cls')
        with open('ssku_tok_file', 'r') as file:
            str_tok = eval(str(file.read()))
        resp = requests.get(self.url+'/api/data/system/module', headers=str_tok, verify=False)
        if resp.status_code != 200:
             with open('ssku_tok_file', 'w') as file:
                str_token = str(self.get_token())
                file.write(str_token)
        with open('ssku_tok_file', 'r') as file:
             token = eval(str(file.read()))
             print(type(token))
             print(time.time())
             return token
             
            
            

    def get_file_token(self):
        token_file = open('ssku_tok_file','r')
        str_token = token_file.read()
        token_file.close()
        
        return str_token


    def small_token(self): #возвращение только тела токена
        creds = {       
            'login': 'admin',
            'password': 'adm777',
            "hash": "1dab4970-4d9b-11ef-a454-b1120eae1a88"
            }
        resp = requests.post(self.url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        
        return bearer


    def get_modules(self):
        self.refresh_token()
        resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
        return resp.json()

    
    def get_node(self, type):
        video_list =['Сервер-видеонаблюдения','Видео-сервер','видео-сервер','Видеосервер 206.69']
        app_list = ['Сервер-приложений']
        if type == 'video':
             search = video_list
        elif type == 'app':
             search = app_list     
        resp = requests.get(self.url + '/api/data/system/node', headers = self.get_token(), verify = False)
        for item in resp.json()['data']:
            if item['title'] in search:
                return item['id']
    

    def get_need_node(self,type):  
        '''принимает type в значениях "video" / "integrator"'''
        resp = requests.get(self.url + '/api/data/system/node', headers = self.get_token(), verify = False)
        if type == 'video':
            for item in resp.json()['data']:
                if item['title'] == 'Сервер-видеонаблюдения':
                    return item['id']
        elif type == 'integrator':
            for item in resp.json()['data']:
                if item['title'] == 'Сервер-приложений':
                    return item['id']
        else:
             return 'WRONG TYPE OF SERVER'


    def get_module_count(self):
            self.refresh_token()
            resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
            return int(len(resp.json()['data']))


    def get_module(self, i): #принимает значения для использования получения id устройства
        self.refresh_token()
        resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
        return resp.json()['data'][i]
    

    def get_module_id(self, i):
        self.refresh_token()
        resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
        return resp.json()['data'][i]['id']


    def get_module_id_by_type(self, i, type='sdp858i'):
        self.refresh_token()
        resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
        if resp.json()['data'][i]['type'] == type:
            return resp.json()['data'][i]['id']

    
    def get_module_by_name(self, tit):
        self.refresh_token() 
        resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
        for item in resp.json()['data']:
                
                if item['title'] == tit:
                        return (item['id'])


    def get_access_point(self)->dict:
        warnings.filterwarnings('ignore')
        os.system('cls')
        head = {
            'Authorization': self.small_token(),
            'Content-type': 'application/x-msgpack'
                    }
        
        msp_body = msgpack.packb({"accessPoint": f"{self.get_module_by_name('СКУД')}", "photoType": "small"})
        resp = requests.post(self.url+f'/api/modules/{self.get_module_by_name('СКУД')}/GetAccessPointList', headers=head, data=msp_body, verify=False)
        unpack = (msgpack.unpackb(resp.content))
        print(type(unpack))
        return unpack['accessPoints'][0]['id']
         


    def get_skud_sort(self):
        id_count = 0 

        head = {
            'Authorization': self.small_token(),
            'Content-type': 'application/x-msgpack'
                   }
                
        msp_body = msgpack.packb({"accessPoint": f"{self.get_access_point()}", "photoType": "small"})
        resp = requests.post(self.url+f'/api/modules/{self.get_module_by_name('СКУД')}/AccessPointEventList', headers=head, data=msp_body, verify=False)
        unpack = (msgpack.unpackb(resp.content))
        with open('c:/work/WHPython/skud_unpack.txt', 'a') as file:
                  file.write(str(unpack))
        with open('c:/work/WHPython/skud_unpack.txt', 'r') as file:
             for item in file:
                  if "'id'" in item:
                       print(id_count)
                       id_count = id_count + 1
                       with open('c:/work/WHPython/skud_id.txt', 'a', encoding='utf-8') as file_:
                            file_.write(item)
        print(id_count)


    def rand_id(self): #id 8-4-4-4-12
        b1 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(8)])
        b2 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b3 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b4 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(4)])
        b5 = ''.join ([random.choice('654983721abcdefghij' ) for _ in range(12)])
        full_id = (f'{b1}-{b2}-{b3}-{b4}-{b5}')
        return full_id


    def get_user_id(self): 
        self.refresh_token()
        resp = requests.get(self.url +'/api/data/security/user', headers = self.token, verify=False)
        return resp.json()['data'][0]['id']
    

    def get_sub_zones(self, url):
        warnings.filterwarnings('ignore')
        self.refresh_token()
        zone_id = []
        sub_zone_id = []
        resp = requests.get(self.url+f'{url}',headers=self.token, verify=False)
        for i in range(len(resp.json()['data'])):
            if resp.json()['data'][i]['nestedZones'] != []:
                zone_id.append(resp.json()['data'][i]['id'])
                print('_'*20)
                print(f'Объект: {resp.json()['data'][i]['title']}')
                
                print(f'Количество вложенных объектов: {len(resp.json()['data'][i]['nestedZones'])}')
                for n in range(len(resp.json()['data'][i]['nestedZones'])):
                    sub_zone_id.append(resp.json()['data'][i]['nestedZones'][n]['id'])
                    print(f'{n} - {resp.json()['data'][i]['nestedZones'][n]['title']}')
                    
        #for i in sub_zone_id:
            #print(f'self.url+{url}/{i}')
            #resp = requests.get(self.url+f'{url}/{i}',headers=self.token, verify=False)
            #print(resp.json()['data']['title'])
                  


    def get_time(self): #формирует текущее значение времени для timestamp
        day = datetime.date.today()
        time = datetime.datetime.now(pytz.timezone('UTC')).time()
        utc_time = (f'{day}T{time}+00:00')
        return utc_time  


    def set_cams(self): #для ССКУ добавление модулей камеры в цикле с задаваемым количееством через input
        warnings.filterwarnings('ignore')
       
        i = input('количество камер: ')
        for n in range(0,int(i)):
            ip = random.choice(['172.18.18.195','192.168.202.189','172.18.18.210','172.18.18.211','172.18.18.212','172.18.18.213'])
            b = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"aa34df8a-41e5-445e-9b24-de9feee20414",'+f'"title":"inep_test_cam_{n+1}",'+'"zone":null,"subsystem":"video","type":"sdp850","settings":'+'{'+f'"ip":"{ip}","port":80,"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+'}'
            body = json.loads(b)
            self.refresh_token()
            resp = requests.post(self.url+'/api/data/system/module', headers=self.token, json=body, verify=False)
            print(resp.json())


    def set_mock_cams(self): #для ССКУ добавление мок-камеры в цикле с задаваемым количееством через input
        warnings.filterwarnings('ignore')
       
        i = input('количество камер: ')
        for n in range(0,int(i)):
            
            b = '{'+'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"aa34df8a-41e5-445e-9b24-de9feee20414",'+f'"title":"test_mock_{n+1}","zone":null,"subsystem":"video","type":"mockcamera","settings":'+'{'+f'"title":"test_mock_{n+1}","node":"aa34df8a-41e5-445e-9b24-de9feee20414"'+'}'+'}'
            body = json.loads(b)
            self.refresh_token()
            resp = requests.post(self.url+'/api/data/system/module', headers=self.token, json=body, verify=False)
            print(resp.json()) 

        
    def notifications(self): #вывод нотификаций
            
            warnings.filterwarnings('ignore')
            
            os.system('cls' if os.name == 'nt' else 'clear')
            for i in range (0, self.get_module_count()):
                print(f"{i} {self.get_modules()['data'][i]['title']}"+f" тип камеры: {self.get_modules()['data'][i]['type']}")
            print('1350 потеря связи\n3350 восстановление связи\n1779 требуется калибровка\n1780 старт калибровки\n3780 конец калибровки\n1781 прерывание калибровки\n1782 калибровка успешна\n1783 калибровка неудачна\n1135 наступление дня\n3135 наступление ночи\n1321 Включение реле 1\n3321 Выключение реле 1\n1322 Включение реле 2\n3322 Выключение реле 2\n1323 Включение реле 3\n3323 Выключение реле 3\n1324 Включение реле 4\n3324 Выключение реле 4\n1502 Подготовка к выключению тепловизора\n1503 Отключение тепловизора отложено по команде оператора\n1504 Отключение тепловизора по команде оператора\n1505 Автоматическое выключение тепловизора\n3352 Объект потерян в тревожной зоне\n3351 Цель вышла из зоны тревоги\n1351 Обнаружена цель в зоне тревоги\n1792 шторка открыта\n3792 шторка открыта\n1750 Включение питания\n3750 выключение питания\n1911 критический уровень заряда\n1912 критическая температура батареи\n1913 критическая температура платы\n1914 переход в режим пониженного электропотребления\n3914 прекращение режима пониженного энергопотребления\n1910 начало заряда\n3910 конец заряда\n1130 тревога\n3130 переустановка тревоги\n1137 корпус вскрыт\n3137 корпус закрыт\n1302 разряд АКБ\n3302 восстановление АКБ\n1720 начало экспорта\n3720 экспорт завершён\n4730 ошибка экспорта\n4731 предупреждение экспорта(отмена)\n5720 отмена экспорта\n1392 начало заряда от220В\n3392 конец заряда от 220В\n1394 начало заряда от генератора \n3394 конец заряда от генератора\n1394 запуск генератора\n3395 остановка генератора\n1396 неудачный запуск генератора\n1399 уровень топлива (тревога)\n3399 уровень топива(информация)\n3911 заряд батареи в норме\n3912 температура батареи в норме\n1791 обогрев стекла включен\n3791 обогрев стекла выключен') 
            d = int(input(f'Введите номер устройства из списка: '))
            device = (self.get_module(d)['id'])
            e_code = int(input(f'Введите код нотификации для модуля <{self.get_module(d)['title']}>: '))
            time=self.get_time()    
            body = {
                #"data": "Тестовая нотификация", #{'gate':'fedcba098765-4321-fedc-ba09-87654321', 'card_code':'01234567'}
                "eventCode": e_code,
                "source": device,
                "timestamp": time, #"2024-06-06T08:00:00.337136+00:00"
                "user": self.get_user_id() #"51cc139c-a132-49e1-990c-786458d4415f"
                }
            i = int(input('Введите количество итераций: '))
            for _ in range (0, i):
                self.refresh_token()
                resp = requests.post(self.url+'/api/data/events/history', headers=self.token, json=body, verify=False)
                print(resp.status_code)


    def all_notifications(self): #вывод всех нотификаций
                
                warnings.filterwarnings('ignore')
                self.refresh_token()
                os.system('cls')
                for i in range (0, self.get_module_count()):
                    print(f"{i} {self.get_modules()['data'][i]['title']}"+f" тип камеры: {self.get_modules()['data'][i]['type']}")
                #e_codes = [1350, 3350, 1779, 1780, 3780, 1782, 1783, 1135, 3135, 1321, 1781,  3321, 1322, 3322, 1323, 3323, 1324, 3324, 1502, 1503, 1504, 1505, 3352, 3351, 1351, 1792, 3792, 1750, 3750, 1911, 1912, 1913, 1914, 3914, 1910, 3910, 1130, 3130, 1137, 3137, 1302, 3302, 1720, 3720, 4730, 4731, 5720, 1392, 3392, 1394, 3394, 3395, 1396, 1399, 3399, 3911, 3912, 1791, 3791]     
                e_codes=[1310,1311,3310,1357,1356,3356,1850,3850,3851,3856,1851,1852,1853,1854,3854,1855,1350,3350,1750,3750,1751,3751,3751,3401,1401,1351,1325,3325,3352,3353,1352,1934,4934,1929,1930,1931,1932,1933,1916,3916,1917,1918,1919,3719,1312,3312,1313,1760,1314,1740,1761,3760,3761,1130,3129,1137,3137,1302,3302,1305,1901,1902,1903,1904,1905,1906,1138,1824,1825,3825,1826,3826,3390,1390,1391,3392,1392,1393,1920,1921,1922,1923,1924,1925,3925,1926,1960,1961,1962,1963,1964,3429,3965,1429,1965,1966,1967,1968,1969,1970,1971,1972,1973,1980,3980,1981,1982,1983,1984,1985,1990,1991,1992,1993,1141,1142,1134,1131,1122,3124,1124,1125,1126,1127,1128,3141,3142,3134,3130,3131,3122]
                d = int(input(f'Введите номер устройства из списка: '))
                device = (self.get_module(d)['id'])
                for code in range(len(e_codes)):
                     e_code = e_codes[code]
                     time=self.get_time()    
                     body = {
                        
                        "eventCode": e_code,
                        "source": device,
                        "timestamp": time, 
                        "user": self.get_user_id() 
                            }
                
                     resp = requests.post(self.url+'/api/data/events/history', headers=self.token, json=body, verify=False)
                     print(resp)

    def needed_notifications(self):
                
            warnings.filterwarnings('ignore')
            self.refresh_token()
            os.system('cls')
            for i in range (0, self.get_module_count()):
                print(f"{i} {self.get_modules()['data'][i]['title']}"+f" тип камеры: {self.get_modules()['data'][i]['type']}")
            e_codes = [0000,1851]
                
            d = int(input(f'Введите номер устройства из списка: '))
            device = (self.get_module(d)['id'])
            for code in range(len(e_codes)):
                e_code = e_codes[code]
                time=self.get_time()    
                body = {
                        
                    "eventCode": e_code,
                    "source": device,
                    "timestamp": time, 
                    "user": self.get_user_id() 
                        }
                
                resp = requests.post(self.url+'/api/data/events/history', headers=self.token, json=body, verify=False)
                print(resp)


    def status(self,status_code):
        if status_code == 200:
            self.terminal('green',status_code)
        elif 399<status_code<499:
            self.terminal('yellow',status_code)
        elif 499<status_code<500:
            self.terminal('red',status_code)
        else:
            self.terminal('non',status_code)



    def postman(self):
          warnings.filterwarnings('ignore')
          import msvcrt
          os.system('cls' if os.name == 'nt' else 'clear')
          met = input('Enter METHOD: ')
          if met.upper() == 'GET':
            uri = input('Enter uri: ')
            resp = requests.get(self.url+f'{uri}',headers=self.get_token(), verify=False)
            print(resp)
            #print(msgpack.unpackb(resp))
            print(resp.json()['data'])
            print(resp.json())
            print("Ожидание нажатия клавиши...")
            msvcrt.getch()
          elif met.upper() == 'POST':
              uri = input('Enter uri: ')
              body_ = input('Enter Body JSON: ')
              body = json.loads(body_)  
              resp = requests.post(self.url+f'{uri}', headers=self.get_token(), json = body, verify=False)
              print(resp)
              print(resp.json()['data'])
              print("Ожидание нажатия клавиши...")
              msvcrt.getch()
          elif met.upper() == 'PUT':
              uri = input('Enter uri: ')
              body_ = input('Enter Body JSON: ')
              body = json.loads(body_)  
              resp = requests.put(self.url+f'{uri}', headers=self.get_token(), json = body, verify=False)
              print(resp)
              print(resp.json()['data'])
              print("Ожидание нажатия клавиши...")
              msvcrt.getch()    
          elif met.upper() == 'DELETE':
              uri = input('Enter uri: ')
              
              resp = requests.delete(self.url+f'{uri}', headers=self.get_token(), verify=False)
              print(resp)
              #print(resp.json())
              print(resp.json()['data'])     
              print("Ожидание нажатия клавиши...")
              msvcrt.getch()       


    def del_cams(self):
        warnings.filterwarnings('ignore')
        os.system('cls' if os.name == 'nt' else 'clear')
        for i in range (0, self.get_module_count()):
            print(f"{i} {self.get_modules()['data'][i]['title']}"+f" тип камеры: {self.get_modules()['data'][i]['type']}")
        d = int(input(f'Введите номер устройства из списка: '))
        device = (f"ids={self.get_module(d)['id']}")
        self.refresh_token()
        resp = requests.delete(self.url+f'/api/data/system/module',headers=self.token, params=device, verify=False)
        print(resp)


    def add_node(self):
        warnings.filterwarnings('ignore')
        os.system('cls')
        nums = int(input('Введите количество серверов для добавления: '))
        for i in range(0, nums):
            body_ = '{'+'"addr": "192.168.202.9", "configPort": 7777, "enabled": true, "id":' + f' "{self.rand_id()}", "restPort": 0, "title": "test_node_{i}"'+'}'
            body = json.loads(body_)
            self.refresh_token()
            resp = requests.post(self.url+'/api/data/system/node',headers=self.token, json=body, verify=False)
            print(resp.json())
        return(resp)


    def auth_cpu(self):
        warnings.filterwarnings('ignore')
        os.system('cls')
        cpu_title = (input('Наименование АРМа: '))
        cpu_title_body_ = '{'+f'"owner":"admin","title":"{cpu_title}","img":"","shared":false,"config":'+'{'+'"type":["auto","auto","auto","auto"],"content":[[],[],[],[]],"tabsForLayout":['+'{'+'"screenIndex":0,"type":"SOT"'+'}'+',{'+'"screenIndex":1,"type":"SOT"'+'},{'+'"screenIndex":2,"type":"ALARM_MONITOR"'+'},{'+'"screenIndex":3,"type":"INFO_MONITOR"}]'+'}'+'}'
        cpu_title_body = json.loads(cpu_title_body_)
        self.refresh_token()
        layout_resp = requests.post(self.url+'/api/data/ui/layout',headers=self.token, json=cpu_title_body,verify=False)
        print(f'POST layout {layout_resp.status_code}')
        cpu_id = input('CPU ID: ')
        put_arm_body_ = '{'+'"archived":false,"data":'+'{'+'"layoutImages":[{"screenIndex":0,"screenType":"SOT","iconType":null'+'},{'+'"screenIndex":1,"screenType":"SOT","iconType":null'+'},{'+'"screenIndex":2,"screenType":"ALARM_MONITOR","iconType":null'+'},{'+'"screenIndex":3,"screenType":"INFO_MONITOR","iconType":null'+'}]}'+f',"hash":"edab4970-4d9b-11ef-a454-b1120eae1a88","id":"{cpu_id}","ip":"192.168.202.61","layoutId":"40b38e92-2e9b-4c2f-b50d-fce2694e188f","name":"{cpu_title}","type":"arm-cpu","valid":true'+'}'
        put_arm_body = json.loads(put_arm_body_)
        put_arm_resp = requests.put(self.url+f'/api/data/security/arm/{cpu_id}', headers=self.token, json=put_arm_body, verify=False)
        return(put_arm_resp.json())
   

    def post_incident(self,timer=0.2):
        warnings.filterwarnings('ignore')
        from time import sleep
        os.system('cls')
        self.refresh_token()
        #print(f'DEBUG glob_time {color.blue(self.glob_start_time)}')
        tit_cam = input('Введите наименование камеры: ')
        i = int(input('Количество инцидентов: '))
        
        for _ in range(0, i):
            #print(f'DEBUG incident: {color.blue(self.glob_start_time)}')
            #print(f'DEBUG incident: {color.yellow(time.time()-self.glob_start_time)}')
            
            timing=self.get_time()
            body_i= '{"data":'+'{'+'}'+f',"timestamp":"{timing}","sourceId":"{self.get_module_by_name(tit_cam)}"'+'}'
            bodyi = json.loads(body_i)
            resp_i = requests.post(self.url+'/api/events/incident',headers=self.token,json=bodyi,verify=False)
            try:
                self.terminal('yellow','body:')
                self.terminal('mod',resp_i.json())
            except Exception as err:
                self.terminal('red',err)
            try:
                self.status(resp_i.status_code)
            except Exception as err:
                self.terminal('red',err)
            sleep(timer)    


    def add_module(self):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')

        cams = input('Количество камер: ')
        cam_list = {
             '1' : '172.16.16.217',
             '2' : '172.16.16.189',
             '3' : '172.16.16.97',
             '4' : '172.16.16.98',
             '5' : '172.16.16.99',
             '6' : '172.16.16.100',
             '7' : '172.16.16.101',
             '8' : '172.16.16.102',
             '9' : '172.16.16.103',
             '10' : '172.16.16.105',
             '11' : '172.16.16.104',
             '12' : '172.16.16.106',
             '13' : '172.16.16.210',

        }

               
        for k,v in cam_list.items():
            print(len(v))
            
            if int(k)<=int(cams):
                if len(v) == 12:
                     cam_name = v[-2:]
                elif len(v) == 13:
                     cam_name = v[-3:]           
                body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"Камера {cam_name}","zone":null,"settings":'+'{'+f'"ip":"{v}","login":"admin","password":"admin","path":"","port":80,"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+',"subsystem":"video","type":"sdp858i"'+'}'
                body_ = body = json.loads(body)      
                resp = requests.post(self.url +'/api/data/system/module', headers=self.token, json=body_, verify=False)
            else:
                 break    
        return resp.json()
    

    def add_module_by_json(self):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        with open('D:/work/WHPython/stilsoft/ssku/api/devices/device_list.json', 'r', encoding='utf-8') as file:   
            module_list = json.load(file)
            module_count = len(module_list)
            name_index = 0
            keys_list = list(module_list.keys())
            for k,v in module_list.items():
                module_name = keys_list[name_index]
                module_type = v['type']
                integrator_list = ['scud','ksbo']
                if module_type not in integrator_list:
                     with open('D:/work/WHPython/stilsoft/ssku/api/devices/video_module_mask.json', 'r', encoding='utf-8') as file:
                          pre_body_ = json.load(file)
                          pre_body = json.dumps(pre_body_)
                          pre_body = pre_body.replace("%%NODE%%", self.get_node('video'))
                          pre_body = pre_body.replace("%%MODULE_NAME%%", module_name)
                          pre_body = pre_body.replace("%%IP%%", v['ip'])
                          pre_body = pre_body.replace("%%PASSWORD%%", "admin")
                          pre_body = pre_body.replace("%%TYPE%%", module_type)
                          body = json.loads(pre_body)
                elif module_type in integrator_list:
                     with open('D:/work/WHPython/stilsoft/ssku/api/devices/integrator_module_mask.json', 'r', encoding='utf-8') as file:
                          pre_body_ = json.load(file)
                          pre_body = json.dumps(pre_body_)
                          pre_body = pre_body.replace("%%NODE%%", self.get_need_node('integrator'))
                          pre_body = pre_body.replace("%%MODULE_NAME%%", module_name)
                          pre_body = pre_body.replace("%%IP%%", v['ip'])
                          pre_body = pre_body.replace("%%PASSWORD%%", "adm777")
                          pre_body = pre_body.replace("%%TYPE%%", module_type)
                          body = json.loads(pre_body)
                else:
                     print( f'ERROR IN module_list IN LINE {name_index}')
                try:     
                    resp = requests.post(self.url +'/api/data/system/module', headers=self.token, json=body, verify=False)
                    name_index += 1   
                    self.status(resp.status_code)
                except Exception as err:
                    self.terminal('red',err)    
            

    def change_ip(self,ip):
         self.refresh_token()
         warnings.filterwarnings('ignore')
         resp = requests.get(self.url+'/api/data/system/module', headers=self.token, verify=False)
         body = {"settings":{"ip":ip}}
         for i in range(self.get_module_count()):
            item = resp.json()['data'][i]['id']
            requests.put(self.url+f'/api/data/system/module/{item}', headers=self.token, json=body, verify=False)


    def add_vs(self,ip, from_n=None, to_n=None):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        n=0
        for i in range(from_n, to_n+1):
            if i <10:
                cam_pref = 1000
            elif  9<i<100:
                cam_pref = 100
            elif  99<i<1000:
                cam_pref = 10
            elif  999<i<10000:
                cam_pref = 1
            body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"vs_{cam_pref}{i}","zone":null,"subsystem":"analitics","type":"objectdetector","settings":'+'{'+f'"ip":"{ip}","port":5011,"detectPeriod":0.25,"eventsInterval":5,"minConfidence":0.4'+'}'+'}'
            body_ = body = json.loads(body)
            req = requests.post(self.url +'/api/data/system/module', headers=self.token, json=body_, verify=False)
            n+=1
            os.system('cls')
            print(f'Модуль {cam_pref}{i} {n}/{to_n-from_n+1}> [{req}]')



    def add_link(self,from_n=None, to_n=None):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        n=0
        for i in range(from_n, to_n+1):
            if i <10:
                link_pref = 1000
            elif  9<i<100:
                link_pref = 100
            elif  99<i<1000:
                link_pref = 10
            elif  999<i<10000:
                link_pref = 1
            camera = self.get_module_by_name(f'Камера {link_pref}{i}')
            analys = self.get_module_by_name(f'vs_{link_pref}{i}')
            body = '{'+f'"host":"{analys}","member":"{camera}","role":"videoSource","order":1,"data":'+'{'+'"detectionEnabled": true'+'}'+'}'
            body_ = body = json.loads(body)
            req = requests.post(self.url +'/api/data/system/objectlink', headers=self.token, json=body_, verify=False)
            n+=1
            os.system('cls')
            print(f'link {link_pref}{i} {n}/{to_n-from_n+1}> [{req}]')

    def add_link_manual(self,host=None, member=None):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        host_body = self.get_module_by_name(host)
        member_body = self.get_module_by_name(member)
        body = '{'+f'"host":"{host_body}","member":"{member_body}","role":"videoSource","order":1,"data":'+'{'+'"detectionEnabled": true'+'}'+'}'
        body_ = body = json.loads(body)
        req = requests.post(self.url +'/api/data/system/objectlink', headers=self.token, json=body_, verify=False)
        os.system('cls')
        print(f'{self.status(req.status_code)}')


    def del_link(self, from_n=None, to_n=None):
        print(f'DEBUG: from = {from_n}')
        print(f'DEBUG: to = {to_n}')
        import sys
        from datetime import datetime
        sys.path.append('D:\work\WHPython\stilsoft')
        from ssku.db import DbSsku
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        for i in range(from_n,to_n+1):
            if i < 10:
                pref = 1000
            elif 9 < i < 100:
                pref = 100
            elif 99 < i < 1000:
                pref = 10
            elif 999 < i < 10000:
                pref = 1
            print(f'DEBUG: Камера = {pref}{i}')    
            module_id = self.get_module_by_name(f'Камера {pref}{i}')
            print(f'DEBUG: {module_id}')
            DbSsku(self.ip).del_link(module_id)



    def add_suml(self,ip, from_n=None, to_n=None):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        if from_n != None and to_n != None:
             n=0
             for i in range(from_n, to_n+1):
                if i <10:
                    cam_pref = 1000
                elif  9<i<100:
                    cam_pref = 100
                elif  99<i<1000:
                    cam_pref = 10
                elif  999<i<10000:
                    cam_pref = 1
                body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"Камера {cam_pref}{i}","zone":null,"settings":'+'{'+f'"ip":"{ip}","login":"admin","password":"admin","path":"","port":{cam_pref}{i},"useMediamtx":true,"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+',"subsystem":"video","type":"sdp858i"'+'}'
                body_ = body = json.loads(body)
                req = requests.post(self.url +'/api/data/system/module', headers=self.token, json=body_, verify=False)
                n+=1
                os.system('cls')
                print(f'Камера {cam_pref}{i} {n}/{to_n-from_n+1}> [{req}]')


        #{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"7747a3a8-a29e-42d1-9455-1cefb50e07ef","title":"proxy_1","zone":null,"settings":{"ip":"192.168.202.61","port":"8554","rtsp":{"login":"","password":"","path":"/proxy_1","sourceTransport":"udp"},"archive":{"mode":"write","maxArchiveSize":"1 GB","archiveLocation":"/archive"}},"subsystem":"video","type":"rtspstream"}            
                  
        else:
            cams = input('Количество камер: ')
                       
            for i in range(0, int(cams)):
            
                if i <10:
                    cam_pref = 1000
                elif  9<i<100:
                    cam_pref = 100
                elif  99<i<1000:
                    cam_pref = 10
                elif  999<i<10000:
                    cam_pref = 1                                       
                #body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"new_cam_suml_{i}","zone":null,"settings":'+'{'+f'"ip":"192.168.201.126","login":"admin","password":"admin","path":"/onvif/device_service","port":1000{i},"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+',"subsystem":"video","type":"sdp858i"'+'}'
                body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"Камера {cam_pref}{i}","zone":null,"settings":'+'{'+f'"ip":"{ip}","login":"admin","password":"admin","path":"","port":{cam_pref}{i},"useMediamtx":true,"maxArchiveSize":"1 GB","archiveLocation":"/archive","sourceTransport":"udp"'+'}'+',"subsystem":"video","type":"sdp858i"'+'}'
                body_ = body = json.loads(body)
                req = requests.post(self.url +'/api/data/system/module', headers=self.token, json=body_, verify=False)
                os.system('cls')
                print(f'Камера {cam_pref}{i} {i+1}/{cams}> [{req}]')


    def add_rtsp(self,from_n=None, to_n=None):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        n=0
        for i in range(from_n, to_n+1):
            body = '{'+f'"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"{self.get_node('video')}","title":"rtsp_{i}","zone":null,"settings":'+'{'+'"ip":"192.168.202.61","port":"8554","rtsp":'+'{'+f'"login":"","password":"","path":"/camera_{i}","sourceTransport":"udp"'+'}'+',"archive":'+'{'+'"mode":"write","maxArchiveSize":"1 GB","archiveLocation":"/archive"'+'}'+'}'+',"subsystem":"video","type":"rtspstream"'+'}'
            body_ = body = json.loads(body)
            req = requests.put(self.url +'/api/data/system/module', headers=self.token, json=body_, verify=False)
            n+=1
            os.system('cls')
            print(f'rtsp camera rtsp_{i} {n-1}/{to_n-from_n}> [{req}]')


#{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"","node":"937ba7f2-706a-42c0-84ee-5ac4e86642ed","title":"rtsp_2","zone":null,"settings":{"ip":"192.168.202.61","port":"8554","rtsp":{"login":"admin","password":"admin","path":"/camera_2","sourceTransport":"udp"},"archive":{"mode":"write","maxArchiveSize":"1 GB","archiveLocation":"/archive"}},"subsystem":"video","type":"rtspstream"}


    def mode_archive(self,mode,value):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        
        module_list = []
        for i in range(self.get_module_count()):
             module_list.append(self.get_module_id(i))
        for id in module_list:
            body={"settings":{"archive": {mode: value, "mode": "write"}}}
            requests.put(self.url +f'/api/data/system/module/{id}', headers=self.token, json=body, verify=False)
            os.system('cls')
            print(f'{mode} {value}: {module_list.index(id)+1} / {len(module_list)}')

    def mode_archive_by_name(self,mode,value,name):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        id = self.get_module_by_name(name)
        body={"settings":{"archive": {mode: value, "mode": "write"}}}
        resp = requests.put(self.url +f'/api/data/system/module/{id}', headers=self.token, json=body, verify=False)
        os.system('cls')
        print(f'{resp}')


    def mode_settings(self,key,value):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        module_list = []
        for i in range(self.get_module_count()):
             module_list.append(self.get_module_id(i))
        
        body={"settings":{key: value}}
        for id in module_list:
            requests.put(self.url +f'/api/data/system/module/{id}', headers=self.token, json=body, verify=False)
            os.system('cls')
            print(f'{module_list.index(id)+1} / {len(module_list)}')



    def mode_mediamtx(self,mode):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        module_list = []
        for i in range(self.get_module_count()):
             module_list.append(self.get_module_id(i))
        if mode == 'true':
             body={"settings":{"useMediamtx": True}}
        else:
             body={"settings":{"useMediamtx": False}}     

        for id in module_list:
            #body={"settings":{"useMediamtx": True}}
        
            req = requests.put(self.url +f'/api/data/system/module/{id}', headers=self.token, json=body, verify=False)
            os.system('cls')
            print(f'{module_list.index(id)+1} / {len(module_list)}')



    def add_suml_by_json(self):
        self.refresh_token()
        warnings.filterwarnings('ignore')
        os.system('cls')
        with open('D:/work/WHPython/stilsoft/ssku/api/json/config.json', 'r', encoding='utf-8') as file:
            config = json.load(file)
            ip = config['ip']
            login = config['login']
            password = config['password']
             
        
        
        cams = input('Количество камер: ')
                       
        for i in range(0, int(cams)):
            os.system('cls')
            if i <10:
                cam_pref = 1000
            elif 10<i<99: 
                cam_pref = 100 
            elif 100<i<999:
                 cam_pref = 10    
            module_name = f'Камера {cam_pref}{i}'
            with open('D:/work/WHPython/stilsoft/ssku/api/json/body.json', 'r', encoding='utf-8') as file:
                pre_body_ = json.load(file)
                pre_body = json.dumps(pre_body_)
                pre_body = pre_body.replace("%%NODE%%", self.get_need_node('video'))
                pre_body = pre_body.replace("%%TITLE%%", module_name)
                pre_body = pre_body.replace("%%IP%%", 'ip')
                pre_body = pre_body.replace("%%PASSWORD%%", "admin")
                pre_body = pre_body.replace("%%TYPE%%", 'sdp858i')
                body = json.loads(pre_body)

            
            req = requests.post(self.url +'/api/data/system/module', headers=self.token, json=body, verify=False)
            print(f'Камера {cam_pref}{i} {i}/{cams}> [{req.status_code}]')       

    def get_module_id_by_name(self, name): #получение id камеры
        warnings.filterwarnings('ignore')
        for i in range (self.get_module_count()):
            sts_ch = (self.get_modules()['data'][i]['title'])
            if sts_ch == name:
                d = i
        camera = (self.get_module(d)['id'])     
        return camera 


    def check_module_state(self,module_name):
        warnings.filterwarnings('ignore')
        module_id = self.get_module_id_by_name(module_name)
        head = {
            'Authorization': self.small_token(),
            'Content-type': 'application/x-msgpack'
                    }
        nul={}
        msp_null = msgpack.packb(nul)
        resp = requests.post(self.url+f'/api/modules/{module_id}/ModuleStateRequest',headers=head, data=msp_null, verify=False )
        print(f'id: {module_id}')
        print(msgpack.unpackb(resp.content))

        if 'offline' in msgpack.unpackb(resp.content)['states']:
            return 'OFFLINE'
        elif 'online' in msgpack.unpackb(resp.content)['states']:
            return 'ONLINE'
        else:
            return msgpack.unpackb(resp.content)['states']

    def enable_module(self,module_name,enabled):
        warnings.filterwarnings('ignore')
        module_id = self.get_module_id_by_name(module_name)
        head = {
            'Authorization': self.small_token(),
            'Content-type': 'application/x-msgpack'
                    }
        if enabled == True:
            nul= "{\n  \"enabled\": true\n}"
        elif enabled == False:
            nul = "{\n  \"enabled\": false\n}"    
        msp_null = msgpack.packb(nul)
        resp = requests.post(self.url+f'/api/modules/{module_id}//MediaStream/ToggleSourceReading',headers=head, data=msp_null, verify=False )
        #print(msgpack.unpackb(resp.content))
        print(resp.status_code)


    def check_inident_mapping(self):
        import sys
        pass

        


class ByInputSsku(ApiSsku):
        
        def get_module_id_by_name_check(self, name): #получение id камеры
            warnings.filterwarnings('ignore')
            for i in range (self.get_module_count()):
                sts_ch = (self.get_modules()['data'][i]['title'])
                if sts_ch == name:
                    d = i
            camera = (self.get_module(d)['id'])     
            return camera        
     