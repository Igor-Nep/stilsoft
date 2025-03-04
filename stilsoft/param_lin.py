import paramiko
from time import sleep

hosts = {'192.168.202.238': '/opt/murom/origin/backend',
         '192.168.202.30': '/opt/murom/origin/backend',
         '192.168.202.18': '/opt/helios/origin/backend',
         '192.168.202.82': '/home/user/dev/rigel/DevOps/Murom',
         '192.168.202.10': '/home/user/rigel/server-app/origin/backend'
}

for host, back_dir in hosts.items():
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=22, username='user', password='stilsoft')
        print (f'Подключено к {host}')
        
        for i in range(0,5):
            start=0
            try:
                ssh.exec_command(f"cd {back_dir}; docker-compose ps > /home/user/Desktop/docker_status.txt")
                sleep(0.5)
                sftp_client = ssh.open_sftp()
                remote_file = sftp_client.open('/home/user/Desktop/docker_status.txt')
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
        remote_file = sftp_client.open('/home/user/Desktop/docker_status.txt')
        try:
            for line in remote_file:
                with open(f'/home/user/Desktop/docker_{host}_log.txt', 'a') as _file:
                    _file.write(line)

        finally:
            remote_file.close()
    except:
        print(f'Подключение к {host} CLOSE')