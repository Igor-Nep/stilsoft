import requests
base_url = 'https://x-clients-be.onrender.com'
class CompanyApi:

    def __init__(self, url):
        self.url = url
        

    def get_company_list(self, params_to_add = None):
        resp = requests.get(self.url +'/company',params=params_to_add)
        return resp.json()

    def get_token(self, user = 'raphael', password = 'cool-but-crude'):
        creds = {       
        'username': user,
        'password': password
        }

        resp = requests.post(self.url+'/auth/login', json=creds)
        return resp.json()["userToken"]

    def create_company(name, description = ''):
        company ={
            "name": name,
            "description": description
        }

        my_headers = {}
        my_headers["x-client-token"]= get_token()
        
        create = requests.post(base_url+'/company', json=company, headers=my_headers)
        return create.json()    