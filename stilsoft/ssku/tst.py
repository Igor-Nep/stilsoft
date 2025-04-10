import paramiko
from time import sleep
def atop_logs(host='192.168.202.221', write_time=5, param='eth1'):
    log_pref = host.strip().split('.')[-1]
    print('atop_logs() \033[5;33m[START]\033[0m')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username='user', password='stilsoft')
    print(f'Подключено к {host}\nwriting atop logs: ',end='')
    ssh.exec_command(f'atop -w /home/user/atop.txt 1 {write_time}')
    sleep(write_time+1)
    ssh.exec_command(f'atop -r /home/user/atop.txt | grep {param} > /home/user/log.txt')
    sleep(1)
    sftp = ssh.open_sftp()
    sftp.get('/home/user/log.txt', 'D:/work/logs/atop_log.txt')  
    sftp.remove('/home/user/atop.txt')
    sftp.remove('/home/user/log.txt')  
    with open(f'D:/work/logs/atop_log.txt','r') as file:
       for item in file:
        for i in range(10):
            print(f'{i}: {item.strip().split()[i]}')
            


atop_logs()    