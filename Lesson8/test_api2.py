import requests
import json
base_url = 'https://x-clients-be.onrender.com'
creds = {       
    'username': 'michaelangelo',
    'password': 'party-dude'
    }
resp = requests.post(base_url+'/auth/login', json=creds)
res = resp.json()
print (res)