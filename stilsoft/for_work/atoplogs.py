from statistics import median
import paramiko,os
from time import sleep
from datetime import datetime
timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def atop_logs(host='192.168.202.221', write_time=15, param='eth0'):
    log_pref = host.strip().split('.')[-1]
    print('atop_logs() \033[5;33m[START]\033[0m')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username='user', password='stilsoft')
    print(f'Подключено к {host}\nwrite atop logs: ',end='')
    sleep(0.5)
    ssh.exec_command(f'atop -w /home/user/atop.txt 1 {write_time}')
    sleep(write_time+1)
    ssh.exec_command(f'atop -r /home/user/atop.txt | grep {param} > /home/user/log.txt')
    sleep(1)
    sftp_client = ssh.open_sftp()
    sftp_client.get('/home/user/log.txt', f'D:/work/logs/{log_pref}_atop.txt')  
    sleep(1)
    sftp_client.remove('/home/user/atop.txt')
    sftp_client.remove('/home/user/log.txt') 
    sftp_client.close()
    ssh.close()

    need_timer = True
    with open(f'D:/work/logs/{log_pref}_atop.txt','r') as file:
        percent_list = []
        param_1_list = []
        param_2_list = []
        for item in file:
            try:
                finded = item.strip().split()[2]
                percent = float(item.strip().split()[3].replace('%',''))
                if isinstance(percent, float):
                     percent_list.append(percent)
                param_1 = item.strip().split()[11]
                param_1_value = float(item.strip().split()[12])
                if isinstance(param_1_value, float):
                    param_1_list.append(param_1_value)
                param_1_char = item.strip().split()[13]
                param_2 = item.strip().split()[15]
                param_2_value = float(item.strip().split()[16])
                if isinstance(param_2_value, float):
                    param_2_list.append(param_2_value)
                param_2_char = item.strip().split()[17]

            except:
                print(f'collect {param}: \033[31m[FAILED]\033[0m')
                next    

        with open(f'D:/work/logs/{timestamp}_{log_pref}_ATOP_LOG.txt', 'a') as file:
                    
            file.write(f'{'='*36}\n')
            if need_timer:
                file.write(f'*{timestamp} {host}*\n')
            file.write(f'{finded}\n')    
                
            try:
                file.write(f'ПИКОВОЕ      {round(max(percent_list),2)}% | {param_1}-{round(max(param_1_list),2)} {param_1_char}   | {param_2}-{round(max(param_2_list),2)} {param_2_char} \n')
            except:
                file.write('ПИКОВОЕ - ОШИБКА\n')
                next    
            try:                     
                file.write(f'МЕДИАННОЕ    {round(median(percent_list),2)}% | {param_1}-{round(median(param_1_list),2)} {param_1_char}   | {param_2}-{round(median(param_2_list),2)} {param_2_char} \n')
            except:
                file.write('МЕДИАННОЕ - ОШИБКА\n')                    
            try:
                file.write(f'МИНИМАЛЬНОЕ   {round(min(percent_list),2)}% | {param_1}-{round(min(param_1_list),2)} {param_1_char}   | {param_2}-{round(min(param_2_list),2)} {param_2_char} \n')
            except:    
                file.write('МИНИМАЛЬНОЕ - ОШИБКА\n')
                next   
            need_timer = False      
    os.remove(f'D:/work/logs/{log_pref}_atop.txt')
    print('\033[32m[DONE]\033[0m')
atop_logs()    