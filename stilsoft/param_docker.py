import datetime
from time import sleep
import paramiko


hosts = {'192.168.202.238': '/opt/murom/origin/backend',
         '192.168.202.30': '/opt/murom/origin/backend',
         '192.168.202.18': '/opt/helios/origin/backend',
         '192.168.202.82': '/home/user/dev/rigel/DevOps/Murom',
         '192.168.202.10': '/home/user/rigel/server-app/origin/backend',
         '192.168.202.9': '/home/user/rigel/node-ssku/origin/backend',
         '192.168.207.68': '/opt/server-app/origin/backend',
         
}


for host, back_dir in hosts.items():
    try:
        name = 'user'
        secret = 'stilsoft'
        if host == '192.168.207.68':
            secret += '1' 
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=22, username=name, password=secret)
        print (f'Подключено к {host}')
        
        for i in range(0,5):
            start=0
            try:
                ssh.exec_command(f"cd {back_dir}; docker-compose ps > /home/user/Desktop/docker_status")
                sleep(0.5)
                sftp_client = ssh.open_sftp()
                remote_file = sftp_client.open('/home/user/Desktop/docker_status')
                n=0
            
                for line in remote_file:
                    n+=1
                
                if n!=0:
                    print('Done\n')
                    break
                else:
                    print(f'Попытка записи [{i+2}]')
            finally:    
                next
        
        sftp_client = ssh.open_sftp()
        remote_file = sftp_client.open('/home/user/Desktop/docker_status')
        try:
            for line in remote_file:
                with open(f'C:/work/logs/containers/docker_{host}_log.txt', 'a') as _file:
                    _file.write(line)
                with open(f'C:/work/logs/containers/container_exit.txt', 'a') as file_:
                    
                        if 'Exit' in line:
                            file_.write(f'{host} {line[:22]} is Exit\n')
                            print(f'{host} {line[:22].strip()} is '+'\033[1m\033[31m{}\033[0m'.format('Exit\n'))
                            
                        
        finally:
           remote_file.close()
    except:
        print(f'Подключение к {host} не удалось!\n')