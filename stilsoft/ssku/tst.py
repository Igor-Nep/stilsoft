import json
origin_ips = []
set_ips = []
with open('D:/work/WHPython/stilsoft/ssku/api/devices/device_list.json', 'r', encoding='utf-8') as file:   
    module_list = json.load(file)
    module_count = len(module_list)
    name_index = 0
    keys_list = list(module_list.keys())
    for k,v in module_list.items():
        origin_ips.append(v['ip'])
print(f'ORIGIN IPS {len(origin_ips)}')
print(f'SET IPS {len(set(origin_ips))}')        
