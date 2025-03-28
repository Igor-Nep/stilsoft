import paramiko
import os
from time import sleep


def check_sensors(host='192.168.202.221', period=6, warn=30, alert=40):
        while True:
        
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port=22, username='user', password='stilsoft')
            #print (f'Подключено к {host}')
            try:
                ssh.exec_command(f"sensors > /home/user/Desktop/sensors")
                sleep(0.5)
                sftp_client = ssh.open_sftp()
                remote_file = sftp_client.open('/home/user/Desktop/sensors')
                        
                    
                for line in remote_file:
                     if 'Package id' in line:
                        temper = (line[16:20])
                        if float(temper) < float(warn):
                             os.system('cls')
                             print(f'Temerature is {temper}\n')
                        
                        elif float(alert) > float(temper) >= float(warn):
                            os.system('cls')
                            print(f'\033[33mWARNING!\033[0m temperature is {temper}')
                            sleep(0.2)
                            os.system('cls')
                            print(f'\033[30mWARNING!\033[0m temperature is {temper}')
                            sleep(0.2)
                            os.system('cls')
                            print(f'\033[33mWARNING!\033[0m temperature is {temper}')
                            os.system('cls')
                            print(f'\033[30mWARNING!\033[0m temperature is {temper}')
                            sleep(0.2)
                            os.system('cls')
                            print(f'\033[33mWARNING!\033[0m temperature is {temper}')
                            sleep(0.2)

                        elif float(temper) >= float(alert):
                            os.system('cls')
                            print(f'\033[31mALERT!\033[0m temperature is {temper}')
                            sleep(0.2)
                            os.system('cls')
                            print(f'\033[30mALERT!\033[0m temperature is {temper}')
                            sleep(0.2)
                            os.system('cls')
                            print(f'\033[31mALERT!\033[0m temperature is {temper}')
                            os.system('cls')
                            print(f'\033[30mALERT!\033[0m temperature is {temper}')
                            sleep(0.2)
                            os.system('cls')
                            print(f'\033[31mALERT!\033[0m temperature is {temper}')
                            sleep(0.2)

                            
                sleep(period)
            finally:   
                next

check_sensors()
