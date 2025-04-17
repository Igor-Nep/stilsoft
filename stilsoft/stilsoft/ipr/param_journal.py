import datetime
from time import sleep
import paramiko





hosts = {'192.168.202.161': 'sudo journalctl -u ssh.service > /home/user/Desktop/journal_ssh',
         }
name = 'user'
secret = 'stilsoft'

while True:
    for host, comando in hosts.items():
        try:
            name = 'user'
            secret = 'stilsoft'
            if host =='192.168.207.68':
                secret+='1'   
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port=22, username=name, password=secret)
            print (f'\nПодключено к {host}')
            
            for i in range(0,5):
                start=0
                try:
                    channel = ssh.get_transport().open_session()
                    channel.get_pty()               
                    channel.settimeout(5)
                    channel.exec_command(comando)
                    channel.send(secret+'\n')
                    sleep(0.5)
                    
                    sftp_client = ssh.open_sftp()
                    remote_file = sftp_client.open('/home/user/Desktop/journal_ssh')
                    n=0
                
                    for line in remote_file:
                        n+=1
                    
                    if n!=0:
                        print('>')
                        break
                    else:
                        print(f'Попытка записи [{i+2}]')
                finally:    
                    next
            
            sftp_client = ssh.open_sftp()
            remote_file = sftp_client.open('/home/user/Desktop/journal_ssh')
            appr_list = ['192.168.202.61', '192.168.38.28']
            connect_list = []
            pidor_list =[]
            try:
                
                lines=0
                for line in remote_file:
                    lines+=1
                    if 'Accepted password for user' in line:
                        connect_list.append(line)
            
                for member in connect_list:
                    
                    for i in range(0, len(appr_list)-1):
                        pidor_index=0
                        if appr_list[i] not in member:
                            pidor_index+=1
                            
                if pidor_index!=0:        
                    pidor_list.append(member)
                    print(f"{lines} {pidor_list}")
                                            
            finally:
                remote_file.close()
            sleep(1800)
            
            for pid in pidor_list:
                    with open(f'C:/work/logs/containers/spisok_pidorasov.txt', 'a') as file_p:
                        file_p.write(pid)
                        print('Пидорасы, присутствуют пидорасы, внимание!\n')
            
            if len(pidor_list) == 0:
                with open(f'C:/work/logs/containers/spisok_pidorasov.txt', 'a') as file_p:
                    file_p.write('Пидорасы отсутствуют!\n')
                    print('Пидорасы отсутствуют, порядок!\n')
        except:
            print(f'Подключение к {host} не удалось!\n')