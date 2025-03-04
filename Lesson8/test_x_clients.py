import requests
import json
from CompanyApi import CompanyApi
base_url = 'https://x-clients-be.onrender.com'



api = CompanyApi('https://x-clients-be.onrender.com')
def test_get_companiesq():
    resp = requests.get(base_url +'/company')
    body = resp.json()
    assert resp.status_code == 200
    assert len(body) > 0

def test_get_active_companies():
    #список всех компаний
    #список активных компаний
    #проверить список 1Ю2

    full_list = get_company_list()


    my_params ={
        'active': 'true'
    }
    resp = requests.get(base_url+'/company', params=my_params)
    filtred_list = resp.json()
    
    assert len(full_list) > len(filtred_list)

def test_add_new():
    #к-во компаний
    #создать новую
    #кол-во компаний
    #проверить +1
    #проверить id последней = resp шаг 2
    #назв и описание последней компании
    body = get_company_list()
    len_before = len(body)
    
    nam = 'AUTO-Nemov'
    des = 'Nemov-Des'
    result = create_company(nam , des)
    new_id = result["id"]
    
    body = get_company_list()
    len_after = len(body)

    assert len_after - len_before == 1 

    assert body[-1]["name"] == nam
    assert body[-1]["description"] == des
    assert body[-1]["id"] == new_id