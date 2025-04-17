import paramiko
from time import sleep

def check_sensors(host='192.168.202.82', period=6, cels=60):
        while True:
        
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, port=22, username='user', password='stilsoft')
            print (f'Подключено к {host}')
            try:
                ssh.exec_command(f"sensors > /home/user/Desktop/sensors")
                sleep(0.5)
                sftp_client = ssh.open_sftp()
                remote_file = sftp_client.open('/home/user/Desktop/sensors')
                        
                    
                for line in remote_file:
                     if 'Package id' in line:
                        temper = (line[16:20])
                        
                        if float(temper) < float(cels):
                            
                            print(f'Temerature is {temper}\n')
                        
                        else:
                            print(f'\033[31mALERT!\033[0m temperature is {temper}')
                sleep(period)
            finally:   
                next

check_sensors()
