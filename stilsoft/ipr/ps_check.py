import paramiko
import os
from time import sleep


def check_pcpu(host='192.168.202.9', period=3):
    cores = 32
    change_list=[]
    with open('c:/work/change_list.txt') as file:
        for line in file:
            change_list.append(line.replace('\n',''))
           

        while True:
            os.system('cls')
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port=22, username='user', password='stilsoft')
            #print (f'Подключено к {host}')
            try:
                ssh.exec_command(f"ps -eo pcpu,args > /home/user/ps_check.txt")
                sleep(0.5)
                sftp_client = ssh.open_sftp()
                remote_file = sftp_client.open('/home/user/ps_check.txt')
                print(type(remote_file))        
                    
                for line in remote_file:
                     pcpu = line[0:4].strip()
                     for i in change_list:
                         pcpu = pcpu.replace(i,'')
                         
                     if len(pcpu.strip())>0:
                        if float(pcpu) > 5.0:
                             core_pcpu = float(pcpu)  / cores
                             print(f'Процесс {line[4:]} использует {core_pcpu}% CPU\n')
                

                sleep(period)
            finally:   
                next

check_pcpu()
