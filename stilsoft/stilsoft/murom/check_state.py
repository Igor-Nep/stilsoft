from api import ApiMurom
import requests, warnings, msgpack, paramiko, os
from time import sleep
from datetime import datetime

api = ApiMurom('https://gate.synerget.ru:8179')
http_url = 'http://192.168.202.238:8189'

id_8122 = ''

drop_count = 0
is_drop_now = False


def write_logs(app_host = '192.168.202.238'):
    print('START LOGS AND COPY')
    drop_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(app_host, port=22, username='user', password='stilsoft')
    client = ssh.open_sftp()
    ssh.exec_command(f'cd /opt/murom/origin/backend && docker-compose logs --tail 1000 media-server > /home/user/media-server_after_drop.txt')
    sleep(1.5)
    ssh.exec_command(f'cd /opt/murom/origin/backend && docker-compose logs --tail 10000 node-manager > /home/user/node-manager_after_drop.txt')
    sleep(1.5)
    client.get('/home/user/media-server_after_drop.txt', f'C:/work/logs/8122/media-server_{drop_count}.txt')
    sleep(1.5)
    client.get('/home/user/node-manager_after_drop.txt', f'C:/work/logs/8122/node-manager_{drop_count}.txt')
    sleep(0.5)
    with open (f'C:/work/logs/8122/media-server_{drop_count}.txt', 'a') as m_file:
        m_file.write(f'\ntime of drop: {drop_time} (-3H)')
    with open (f'C:/work/logs/8122/node-manager_{drop_count}.txt', 'a') as n_file:
        n_file.write(f'\ntime of drop: {drop_time} (-3H)')    
    print('DONE')

def check_8122_drop():
        global id_8122
        if id_8122 == '':
             id_8122 = api.get_camera()
        warnings.filterwarnings('ignore')
        head = {
            'Content-type': 'application/x-msgpack'
                    }
        nul={}
        msp_null = msgpack.packb(nul)
        try: 
            resp = requests.post(http_url+f'/api/modules/{id_8122}/ModuleStateRequest',headers=head, data=msp_null, verify=False )
        
            if 'offline' in msgpack.unpackb(resp.content)['states']:
                return True
            else:
                return False
        except:
             pass    

while True:
    if drop_count >=10:
        break 
    
    elif not is_drop_now:
        if check_8122_drop():
             is_drop_now = True
             drop_count += 1
             write_logs()

    elif is_drop_now:
         if not check_8122_drop():
              is_drop_now = False         
    os.system('cls')     
    print(f'[{drop_count}]')
    sleep(1)