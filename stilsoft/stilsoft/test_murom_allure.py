import requests
import allure
from ApiRes import ApiRes
import warnings
import json
from time import sleep
import msgpack
import random
import logging

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@allure.epic('MUROM')
class MuromTest:
    
    #pytest --alluredir=allure_results
    #allure serve allure_results  
    #allure generate C:\work\WHPython\allure_results
    #allure open allure-report
    
    base_url = 'https://gate.synerget.ru:8179'
    api = ApiRes(base_url)
    create_operator = ''
    create_operator_id = ''

    def rand_data(self, n)-> str:
        rnd = ''.join ([random.choice('1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*()<>?:' ) for _ in range(n)])
        return rnd

    @allure.severity('minor')
    @allure.feature('api тесты')
    @allure.story('Тест модулей')
    @allure.title('Получение списка модулей')
    def test_module_list(self):
        warnings.filterwarnings('ignore')
        with allure.step('Получить список модулей из system/module'):
            logger.info('Logged INFO сообщение:')       
            resp = requests.get(self.base_url+'/api/data/system/module', headers=self.api.get_token(), verify=False)
        with allure.step('Сравнить статус-код списка модулей со статус-кодом 200'):
            assert resp.status_code == 200

    
    
    @allure.severity('normal')
    @allure.feature('api тесты')
    @allure.story('Тест модулей')
    @allure.title('Тест стейта поворотного устройства')
    def none_ch_881(self):
        warnings.filterwarnings('ignore')
    
        _body_1t = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{self.api.get_881()}","node":"{self.api.get_node()}"'+',"title":"Поворотное устройство","zone":null,"subsystem":"misc","type":"sdp881","settings":{"ip":"172.18.18.22","port":7001'+'}'+'}'
        _body_2t = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{self.api.get_881()}","node":"{self.api.get_node()}"'+',"title":"Поворотное устройство","zone":null,"subsystem":"misc","type":"sdp881","settings":{"ip":"172.18.18.222","port":7001'+'}'+'}'
        _body_1=json.loads(body_1t)
        _body_2=json.loads(body_2t)
        warnings_num=0
        for _ in range(2):
            with allure.step('Проверка стейта Потеря связи с невалидным ip'):
                resp=requests.put(self.base_url+f'/api/data/system/module/{self.api.get_881()}',headers=self.api.get_token(), json=body_1,verify=False)
                print('Смена ip на невалидный >')
                print(resp)
                sleep(1)
                if self.api.check_881_state()!='OFFLINE':
                    warnings_num+=1
                print(f'ошибок проверки: {warnings_num}')    
                sleep(1)
            with allure.step('Проверка стейта На связи с валидным ip'):
                resp=requests.put(self.base_url+f'/api/data/system/module/{self.api.get_881()}',headers=self.api.get_token(), json=body_2,verify=False)
                print('Смена ip на валидный >')
                print(resp)
                sleep(1)
                if self.api.check_881_state()!= 'ONLINE':
                    warnings_num+=1
                print(f'ошибок проверки: {warnings_num}')       
                sleep(1)
        with allure.step('Количество неверных стейтов = 0'):        
            assert warnings_num == 0

    @allure.severity('blocker')
    @allure.feature('api тесты')
    @allure.story('Тесты авторизации')
    @allure.title('Авторизация администратора с валидными данными')
    def test_auth_adm(self):
        warnings.filterwarnings('ignore')
        with allure.step('Логин admin, пароль adm777'):
             creds = {       
            'login': 'admin',
            'password': 'adm777'
            }
        with allure.step('Отправка запроса на авторизацию'):     
            resp = requests.post(self.base_url+'/api/auth/login', json=creds, verify=False)
        with allure.step('Статус-код = 200'):
            assert resp.status_code == 200

    @allure.severity('trivial')
    @allure.feature('api тесты')
    @allure.story('Тесты авторизации')
    @allure.title('Невозможность авторизации при невалидных данных')
    def test_auth_adm_0(self):
        warnings.filterwarnings('ignore')
        for i in range(0, 26):
            rnd_l = self.rand_data(i)
            rnd_p = self.rand_data(i)
            with allure.step(f'Логин {rnd_l}, пароль {rnd_p}'):
                 creds = {       
                'login':rnd_l,
                'password': rnd_p
                }
            with allure.step('Отправка запроса на авторизацию'):     
                resp = requests.post(self.base_url+'/api/auth/login', json=creds, verify=False)
            with allure.step('Статус-код != 200'):
                assert resp.status_code != 200

    @allure.severity('blocker')
    @allure.feature('api тесты')
    @allure.story('Тесты авторизации')
    @allure.title('Невозможность авторизации администратора при невалидном пароле')
    def test_auth_adm_1(self):
        warnings.filterwarnings('ignore')
        rnd_p = self.rand_data(6)
        with allure.step(f'Логин admin, пароль {rnd_p}'):
            creds = {       
            'login': 'admin',
            'password': rnd_p
             }
        with allure.step('Отправка запроса на авторизацию'):     
            resp = requests.post(self.base_url+'/api/auth/login', json=creds, verify=False)
        
        with allure.step('Статус-код != 200'):
            assert resp.status_code != 200 


    def create_operator_user(self):
        warnings.filterwarnings('ignore')
        global create_operator_id, create_operator

        rnd_id = self.rand_data(5)
        create_operator = f'operator_{rnd_id}'
        body = '{'+f'"login":"{create_operator}","name":"{create_operator}","role":"user","active":true,"description":"","middleName":"","photo":"","surname":"{create_operator}","data":'+'{'+'}'+f',"password":"{create_operator}"'+'}'
        body_=json.loads(body)
        resp = requests.post(self.base_url+'/api/data/security/user', headers = self.api.get_token(), json = body_, verify = False)
        print(f'создание пользователя {create_operator}, роль оператор: {resp}')
        create_operator_id = resp.json()['data']['id']
        print(f'id: {create_operator_id}')
        

    def del_operator_user(self):
        warnings.filterwarnings('ignore')
        global create_operator_id, create_operator
        resp = requests.delete(self.base_url + f'/api/data/security/user/{create_operator_id}', headers = self.api.get_token(), verify = False)
        print(f'Удаление созданного пользователя {create_operator}, роль оператор: {resp}')

    @allure.severity('blocker')
    @allure.feature('api тесты')
    @allure.story('Тесты авторизации')
    @allure.title('Авторизация оператора с валидными данными')
    def test_auth_operator(self):
        warnings.filterwarnings('ignore')
        self.create_operator_user()

        with allure.step(f'Логин {create_operator}, пароль {create_operator}'):
             creds = {       
            'login': create_operator,
            'password': create_operator
            }
        with allure.step('Отправка запроса на авторизацию'):     
            resp = requests.post(self.base_url+'/api/auth/login', json=creds, verify=False)
        with allure.step('Статус-код = 200'):
            assert resp.status_code == 200  
        self.del_operator_user()                  


