import paramiko
import requests
import os
from os import system as os_sys
from time import sleep
import subprocess  


def server_ping(host):
    command = subprocess.run(['ping', '-n', '1', host], stdout=subprocess.PIPE)
    return command.returncode == 0


url = 'https://gate.synerget.ru:8179'

default_app_server_ip = '192.168.202.10'
default_video_server_ip = '192.168.202.9'


while True:
    ans_app_server_ip = input('Введите IP сервера приложений: ')
    if ans_app_server_ip == '':
        app_server_ip = default_app_server_ip
    else:
        app_server_ip = ans_app_server_ip
    print(f'IP сервера приложений: [{app_server_ip}]')    
    
    if server_ping(app_server_ip):
        break

os_sys('cls')
ans_name = input(f'Имя пользователя для [{app_server_ip}]: "\033[34muser\033[0m"? (\033[1;37my\033[0m/\033[1;37mn\033[0m): ')
if ans_name.lower() == 'y':
    app_name = 'user'
else:
    app_name = input(f'Введите имя пользователя для [{app_server_ip}]: ')
ans_secret = input(f'Пароль для [{app_server_ip}]: "\033[34mstilsoft\033[0m"? (\033[1;37my\033[0m/\033[1;37mn\033[0m): ')
if ans_secret.lower() == 'y':
    app_secret = 'stilsoft'
else:
    app_secret = input(f'Введите пароль для [{app_server_ip}]: ')

is_video_server = input('Будет проверка видеосервера? (\033[1;37my\033[0m/\033[1;37mn\033[0m): ')
if is_video_server.lower() == 'y' or is_video_server.lower() == 'yes':
     has_video_server = True
else:
     has_video_server = False


if has_video_server:
    while True:
        ans_video_server_ip = input('Введите IP видеосервера: ')
        if ans_video_server_ip == '':
            video_server_ip = default_video_server_ip
        else:
            video_server_ip = ans_video_server_ip
        print(f'IP видеосервера: [{video_server_ip}]')       
        if server_ping(video_server_ip):
            break 
    ans_video_name = input(f'Имя пользователя для [{video_server_ip}]: "\033[34muser\033[0m"? (\033[1;37my\033[0m/\033[1;37mn\033[0m): ')
    if ans_video_name.lower() == 'y':
        video_name = 'user'
    else:
        video_name = input(f'Введите имя пользователя для [{video_server_ip}]: ')
    ans_video_secret = input(f'Пароль для [{video_server_ip}]: "\033[34mstilsoft\033[0m"? (\033[1;37my\033[0m/\033[1;37mn\033[0m): ')
    if ans_video_secret.lower() == 'y':
        video_secret = 'stilsoft'
    else:
        video_secret = input(f'Введите пароль для [{video_server_ip}]: ')        


def get_app_back_dir(app_host):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(app_host, port=22, username=app_name, password=app_secret)
    back_list=[]
    with open('C:/work/WHPython/stilsoft/for_work/unilog/back_list') as file:
        for line in file:
            back_list.append(line.replace('\n',''))
                                                     
        for dir in (back_list):
            _, stdout, _ = ssh.exec_command(f'cd {dir}')
            if stdout.channel.recv_exit_status() == 0:
                return(dir)


def get_video_back_dir(video_host):   
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(video_host, port=22, username=video_name, password=video_secret)
    back_list=[]
    with open('C:/work/WHPython/stilsoft/for_work/unilog/back_list') as file:
        for line in file:
            back_list.append(line.replace('\n',''))
                                                     
        for dir in (back_list):
            _, stdout, _ = ssh.exec_command(f'cd {dir}')
            if stdout.channel.recv_exit_status() == 0:
                return(dir)


def get_token(login='admin', password='adm777'):
        creds = {       
            'login': login,
            'password': password,
            "hash": "for0test-hash-api0-0000-000000000000"
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


def check_logs(video_host, app_host, cam_id, video_back_dir = None, app_back_dir = get_app_back_dir(app_server_ip), my_directory = 'c:/work/logs', trigger='Отброшен'):
        repeater = True
        animation = 0
        while repeater:
        
            vssh = paramiko.SSHClient()
            vssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            vssh.connect(video_host, port=22, username='user', password='stilsoft')
            os_sys('cls')
            print (f'Подключено к {video_host}', end= ' ')
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
                vssh.exec_command(f'{video_back_dir}; docker-compose logs -f media-server | grep {cam_id}> /home/user/Desktop/logs_sdp850.txt')
                
                vssh.exec_command("\x03")
                video_sftp_client = vssh.open_sftp()
                video_remote_file = video_sftp_client.open('/home/user/Desktop/logs_sdp850.txt')

                for line in video_remote_file:
                     if trigger in line:
                          print('Поток отброшен')
                          print('Сбор логов: ',end='')
                          vssh.exec_command(f'{video_back_dir}; docker-compose logs --tail 1000 media-server > /home/user/Desktop/logs_media-server_after_drop.txt')
                          sleep(1.5)
                          vssh.exec_command(f'{video_back_dir}; docker-compose logs --tail 10000 node-manager > /home/user/Desktop/logs_node-manager_after_drop.txt')
                          sleep(1.5)
                          video_sftp_client.get('/home/user/Desktop/logs_media-server_after_drop.txt', f'{my_directory}/logs_media-server_after_drop.txt')
                          sleep(1.5)
                          video_sftp_client.get('/home/user/Desktop/logs_node-manager_after_drop.txt', f'{my_directory}/logs_node-manager_after_drop.txt')
                          sleep(0.5)
                                                    
                          assh = paramiko.SSHClient()
                          assh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                          assh.connect(app_host, port=22, username='user', password='stilsoft')
                          print (f'Подключено к {app_host}')
                          assh.exec_command(f'{app_back_dir}; docker-compose logs --tail 10000 node-manager > /home/user/Desktop/app_serv_node_logs_after_drop.txt')
                          sleep(5)
                          app_sftp_client = assh.open_sftp()
                          app_sftp_client.get('/home/user/Desktop/app_serv_node_logs_after_drop.txt', f'{my_directory}/app_serv_node_logs_after_drop.txt')
                          repeater = False
                          print('\033[32mDONE\033[0m')
                          break  
                          
                     elif 'ERROR' in line:
                          print('Найдены ошибки')
                          vssh.exec_command(f'{video_back_dir}; docker-compose logs --tail 1000 media-server > /home/user/Desktop/logs_media-server_errors.txt')
                          sleep(1.5)
                          video_sftp_client.get('/home/user/Desktop/logs_media-server_errors.txt', f'{my_directory}/media_err.txt')
                          sleep(1.5)
                          with open(f'{my_directory}/media_errors.txt', 'a') as wr_file:
                               r_file = open(f'{my_directory}/media_err.txt', 'r')
                               for item in r_file:
                                    wr_file.write(item)
                               r_file.close()    
                          os.remove(f'{my_directory}/media_err.txt')      
                          print('Записано')          
                sleep(10)                    
            finally:
                 next


def start_video_server_check():

    while True:
        v_host = input('Введите IP видео-сервера: ')
        if v_host == '':
            v_host = '192.168.202.9'
        if server_ping(v_host):      
            os_sys('cls')
            print(f'Видео-сервер -\033[32m [{v_host}]\033[0m')
            break
        else:
            os_sys('cls')
            print(f'Видео-сервер -\033[31m [{v_host} недоступен]\033[0m') 

    while True:
        a_host = input('Введите IP сервера приложений: ')
        if a_host == '':
            a_host = '192.168.202.10'
        if server_ping(a_host):      
            os_sys('cls')
            print(f'Видео-сервер -     \033[32m [{v_host}]\033[0m')
            print(f'Сервер приложений -\033[32m [{a_host}]\033[0m')
            break
        else:
            os_sys('cls')
            print(f'Видео-сервер -     \033[32m [{v_host}]\033[0m')
            print(f'Сервер приложений -\033[31m [{a_host} недоступен]\033[0m')
    while True:
        cam = input('Введите наименование отслеживаемой камеры: ')
        c_id = get_cam_id(cam)
        if c_id == None:
            os_sys('cls')
            print(f'Видео-сервер -     \033[32m [{v_host}]\033[0m')
            print(f'Сервер приложений -\033[32m [{a_host}]\033[0m')
            print(f'Камера -           \033[31m [{cam} неверное наименование]\033[0m ')
        else:
            os_sys('cls')
            print(f'Видео-сервер -     \033[32m [{v_host}]\033[0m')
            print(f'Сервер приложений -\033[32m [{a_host}]\033[0m')      
            print(f'ID камеры -        \033[32m [{c_id}]\033[0m ')
            break

    while True:
        m_dir  = input('Введите директорию для сохранения логов: ')
        if os.path.isdir(f'{m_dir}'):
            os_sys('cls')
            print(f'Видео-сервер -                \033[32m [{v_host}]\033[0m')
            print(f'Сервер приложений -           \033[32m [{a_host}]\033[0m')
            print(f'ID камеры -                   \033[32m [{c_id}]\033[0m ')
            print(f'Директория сохранения логов - \033[32m [{m_dir}]\033[0m ')
            break
        
        else:
            os_sys('cls')
            print(f'Видео-сервер -     \033[32m [{v_host}]\033[0m')
            print(f'Сервер приложений -\033[32m [{a_host}]\033[0m')
            print(f'ID камеры -        \033[32m [{c_id}]\033[0m ')
            print(f'Директории \033[31m[{m_dir}]\033[0m не существует')
                        

            
        
    sleep(3)



    #check_logs(v_host, a_host, c_id, video_back_dir = 'cd /home/user/rigel/node-ssku/origin/backend', app_back_dir = 'cd /home/user/rigel/server-app/origin/backend', my_directory = m_dir)

os_sys('cls')
print(f'Директория back [{app_server_ip}]: {get_app_back_dir(app_server_ip)}')

if has_video_server:
    print(f'Директория back [{video_server_ip}]: {get_app_back_dir(video_server_ip)}')
