import paramiko
import os
from time import sleep

#sudo apt-get install lm-sensors
#sudo sensors-detect
#sensors

def check_sensors(host='192.168.202.221', period=6, warn=40, alert=60):
        import sys
        from color import color
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(host, port=22, username='user', password='stilsoft')
        stdin, stdout, stderr = ssh.exec_command('which sensors')
        installed = stdout.read().decode().strip()
        print(f'DEBUG {installed}')
        if not installed:

            sys.stdout.write(f'{color.grey('lm-sensors')} [{color.red('не установлен')}] на {host}')
            sys.stdout.flush()
            sleep(1)
            stdin, stdout, stderr = ssh.exec_command('sudo apt-get install lm-sensors')
            try:
                stdin.write(f'stilsoft\n')
                stdin.flush()
                print(stderr.read().decode())
            except:
                next
            sleep(1)
            print(stdout)
            stdin, stdout, stderr = ssh.exec_command('sudo sensors-detect')
            try:
                stdin.write(f'stilsoft\n')
                stdin.flush()
                print(stderr.read().decode())
            except:
                next
            sleep(1)
            print(stdout)
            #exit()        
        
        from color import color
        import sys

        def cls():
            sys.stdout.write('\r' + ' ' * 100 + '\r')
            sys.stdout.flush()

        while True:
            #ssh = paramiko.SSHClient()
            #ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            #ssh.connect(host, port=22, username='user', password='stilsoft')
            #print (f'Подключено к {host}')
            try:
                ssh.exec_command(f"sensors > /home/user/sensors")
                sleep(0.5)
                sftp_client = ssh.open_sftp()
                remote_file = sftp_client.open('/home/user/sensors')
                        
                    
                for line in remote_file:
                     if 'Package id' in line:
                        temper = (line[16:20])
                        if float(temper) < float(warn):
                             cls()
                             sys.stdout.write(f' temperature is {temper}\r')
                             sys.stdout.flush()

                             #os.system('cls')
                             #print(f'Temerature is {temper}\n')
                        
                        elif float(alert) > float(temper) >= float(warn):
                             cls()
                             for timer in range(int(period), -1, -1):
                                  if timer % 2 == 0:                                      
                                      sys.stdout.write(f'{color.yellow('WARNING!')} temperature is {temper}\r')
                                      sys.stdout.flush()
                                      sleep(0.2)
                                  else:
                                      sys.stdout.write(f'{color.grey('WARNING!')} temperature is {temper}\r')
                                      sys.stdout.flush()
                                      sleep(0.2)
                            #os.system('cls')
                            #print(f'\033[33mWARNING!\033[0m temperature is {temper}')
                            #sleep(0.2)
                            #os.system('cls')
                            #print(f'\033[30mWARNING!\033[0m temperature is {temper}')
                            #sleep(0.2)
                            #os.system('cls')
                            #print(f'\033[33mWARNING!\033[0m temperature is {temper}')
                            #os.system('cls')
                            #print(f'\033[30mWARNING!\033[0m temperature is {temper}')
                            #sleep(0.2)
                            #os.system('cls')
                            #print(f'\033[33mWARNING!\033[0m temperature is {temper}')
                            #sleep(0.2)

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
