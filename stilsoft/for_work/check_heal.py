import paramiko
import requests
import os
from os import system as os_sys
from time import sleep
import subprocess

url = 'https://gate.synerget.ru:8179'
drop_count = 0
repeater = True

def ping(host):

    command = ['ping', '-n', '1', host]
    return subprocess.call(command)==0

def get_token(login='admin', password='adm777'):
        creds = {       
            'login': login,
            'password': password,
            }
        resp = requests.post(url+'/api/auth/login', json=creds, verify=False)
        bearer = (f'Bearer {resp.json()["access_token"]}')
        my_token = {
            'Authorization': bearer
        }
        return my_token

def get_cam_id(cam_title): 
        resp = requests.get(url+'/api/data/system/module', headers=get_token(), verify=False)
        for item in resp.json()['data']:
                
                if item['title'] == cam_title:
                        return (item['id'])
                
def check_heal(app_host, cam_id, app_back_dir = 'cd /opt/murom/origin/backend', my_directory = 'c:/work/logs', trigger='offline'):
        
        animation = 0
        global drop_count, repeater
        while repeater:
            
            vssh = paramiko.SSHClient()
            vssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            vssh.connect(app_host, port=22, username='user', password='stilsoft')
            os_sys('cls')
            if drop_count >= 5:
                 print(f'drop count: {drop_count}')
                 print(f'Отключено от {app_host}')
                 break
                 
            elif drop_count > 0:
                 print(f'drop count: {drop_count}')
                
                 
            print (f'Подключено к {app_host}', end= ' ')
            if animation == 0:
                 print('>')
                 animation += 1
            elif animation == 1:
                 print(' >')
                 animation += 1
            elif animation == 2:
                 print('  >')
                 animation += 1
            elif animation == 3:
                 print('   >')
                 animation += 1
            elif animation == 4:
                 print('    >')
                 animation += 1
            elif animation == 5:
                 print('     >')  
                 animation = 0
                                   
            try:
                vssh.exec_command(f'{app_back_dir}; docker-compose logs --tail 200 health-monitor | grep {cam_id}> /home/user/Desktop/logs_health_mon.txt')
                sleep(0.5)
                vssh.exec_command("\x03")
                video_sftp_client = vssh.open_sftp()
                video_remote_file = video_sftp_client.open('/home/user/Desktop/logs_health_mon.txt')

                for line in video_remote_file:
                    if trigger in line:
                          
                          drop_count+=1
                          vssh.exec_command(f'{app_back_dir}; docker-compose logs --tail 1000 media-server > /home/user/Desktop/logs_media-server_after_drop.txt')
                          sleep(1.5)
                          vssh.exec_command(f'{app_back_dir}; docker-compose logs --tail 10000 node-manager > /home/user/Desktop/logs_node-manager_after_drop.txt')
                          sleep(1.5)
                          video_sftp_client.get('/home/user/Desktop/logs_media-server_after_drop.txt', f'{my_directory}/logs_media-server_after_drop_{drop_count}.txt')
                          sleep(1.5)
                          video_sftp_client.get('/home/user/Desktop/logs_node-manager_after_drop.txt', f'{my_directory}/logs_node-manager_after_drop_{drop_count}.txt')
                          sleep(0.5)
                          
                          
                          break

                 
                          
                                 
            except:
                 next

while True:
    a_host = input('Введите IP сервера: ')
    if a_host == '':
        a_host = '192.168.202.238'
    if ping(a_host):      
        os_sys('cls')
        print(f'Сервер -\033[32m [{a_host}]\033[0m')
        break
    else:
        os_sys('cls')
        print(f'Видео-сервер -\033[31m [{a_host} недоступен]\033[0m') 


while True:
    cam = 'Камера дальнего обзора'
    c_id = get_cam_id(cam)
    if c_id == None:
        os_sys('cls')
        print(f'Сервер -           \033[32m [{a_host}]\033[0m')
        
        print(f'Камера -           \033[31m [{cam} неверное наименование]\033[0m ')
    else:
        os_sys('cls')
        print(f'Сервер -           \033[32m [{a_host}]\033[0m')
             
        print(f'ID камеры -        \033[32m [{c_id}]\033[0m ')
        break

while True:
    m_dir  = input('Введите директорию для сохранения логов: ')
    if m_dir == '':
        m_dir = 'c:/work/logs/8122'
        if os.path.isdir(f'{m_dir}'):
            os_sys('cls')
        
        print(f'Сервер -                      \033[32m [{a_host}]\033[0m')
        print(f'ID камеры -                   \033[32m [{c_id}]\033[0m ')
        print(f'Директория сохранения логов - \033[32m [{m_dir}]\033[0m ')
        sleep(2)
        break
    
    else:
        os_sys('cls')
        
        print(f'Сервер -           \033[32m [{a_host}]\033[0m')
        print(f'ID камеры -        \033[32m [{c_id}]\033[0m ')
        print(f'Директории \033[31m[{m_dir}]\033[0m не существует')


check_heal(a_host, c_id, app_back_dir = 'cd /opt/murom/origin/backend', my_directory= m_dir, trigger='ffline')