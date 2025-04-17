import requests
import allure
from ApiRes import ApiRes
import warnings
import json
from time import sleep
import msgpack


@allure.epic('MUROM')
class MuromTest:
    #pytest --alluredir=C:/work/allure/allure_results
    #allure serve D:/allure/allure_results  
    base_url = 'https://gate.synerget.ru:8179'
    api = ApiRes(base_url)

    @allure.severity('critical')
    @allure.feature('api тесты')
    @allure.story('Тест модулей')
    @allure.title('Получение списка модулей')
    def test_create_com(self):
        with allure.step('Получить список модулей из system/module'):       
            resp = requests.get(self.base_url+'/api/data/system/module', headers=self.api.get_token(), verify=False)
        with allure.step('Сравнить статус код списка модулей с статус кодом 200'):
            assert resp.status_code == 200


    def ch_loc_state(self):
        warnings.filterwarnings('ignore')
        head = {
            'Authorization': self.api.small_token(),
            'Content-type': 'application/x-msgpack'
                    }
        nul=None
        msp_null = msgpack.packb(nul)
        resp = requests.post(self.base_url+f'/api/modules/{self.api.get_177()}/CurrentState',headers=head, data=msp_null, verify=False )
        
        return msgpack.unpackb(resp.content)['state']

    
    @allure.severity('normal')
    @allure.feature('api тесты')
    @allure.story('Тест модулей')
    @allure.title('Тест стейта радиолокатора')
    def test_ch_loc(self):
        warnings.filterwarnings('ignore')
    
        body_1t = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":'+f'"{self.api.get_177()}"'+',"node":"7b3efdfa-b3f2-4758-a5b8-0168fec4c339","title":"Радиолокатор","zone":null,"subsystem":"misc","type":"sts177","settings":{"ip":"192.168.0.101","port":7001'+'}'+'}'
        body_2t = '{"parent":null,"archived":false,"enabled":true,"group":"00000000-0000-0000-0000-000000000000","id":"f2c09e71-87a5-4f11-a39e-09dd8ea9f7b0","node":"7b3efdfa-b3f2-4758-a5b8-0168fec4c339","title":"Радиолокатор","zone":null,"subsystem":"misc","type":"sts177","settings":{"ip":"192.168.0.100","port":7001'+'}'+'}'
        body_1=json.loads(body_1t)
        body_2=json.loads(body_2t)
        warnings_num=0
        for _ in range(5):
            with allure.step('Проверка стейта Потеря связи с невалидным ip'):
                resp=requests.put(self.base_url+f'/api/data/system/module/{self.api.get_177()}',headers=self.api.get_token(), json=body_1,verify=False)
                print(resp)
                if self.ch_loc_state()!=None:
                    warnings_num+=1
                    
                sleep(6)
            with allure.step('Проверка стейта На связи с валидным ip'):
                resp=requests.put(self.base_url+f'/api/data/system/module/{self.api.get_177()}',headers=self.api.get_token(), json=body_2,verify=False)
                print(resp)
                if self.ch_loc_state()==None:
                    warnings_num+=1
                    
                sleep(6)
        with allure.step('Количество неверных стейтов = 0'):        
            assert warnings_num == 0

           