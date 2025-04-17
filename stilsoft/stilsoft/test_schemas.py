import requests

url = "http://192.168.202.30:8000/api/modules/ad361c52-9756-467d-9d7d-ed7cf392cba7/SetMuted"

payload = '{"muted": false}'
headers = {
    "Content-Type": "application/msgpack",
    "Accept": "application/msgpack"
}

response = requests.post(url, data=payload, headers=headers, verify=False)

print(response.json())