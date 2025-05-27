print('init ssku package')
with open('D:\work\WHPython\stilsoft\ssku/config_ssku.json', 'w') as file:
    file.write('{"base_url": "https://gate.synerget.ru:8179"}')


from color import color
host_file =  open('c:/windows/system32/drivers/etc/hosts', 'r')
len_host = int(len(host_file.readlines()))
host_file.seek(0,0)
active_host = []
for _ in range(0, len_host):
    s = host_file.readline()
    if '#' not in s:
        active_host.append(s)
newti=str(active_host[0])
print(f'{color.blue(newti)}')
print(f'DEBUG: {newti}')
host_file.close()

