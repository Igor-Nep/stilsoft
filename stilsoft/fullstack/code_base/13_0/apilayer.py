import requests
#exchanges_QA_532
url = 'https://api.apilayer.com/exchangerates_data/latest&symbols={symbols}&base={base}'

payload = {}
headers = {"apikey": "xpFd05ILsUUB68jwX3VPstrDf6dPNpUf"}
#a96487c75a4788efa14dfee5b799a787
#xpFd05ILsUUB68jwX3VPstrDf6dPNpUf
resp = requests.request("GET", url, headers=headers, data = payload)

status_code = resp.status_code

print(status_code)