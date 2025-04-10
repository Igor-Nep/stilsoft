from statistics import median
import paramiko, os
from time import sleep
from datetime import datetime


timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

def docker_logs(host='192.168.202.221', write_time=720, cores=48):
    log_pref = host.strip().split('.')[-1]
    print('docker_logs() \033[5;33m[START]\033[0m')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username='user', password='stilsoft')
    print(f'Подключено к {host}\nproducing docker stats logs: ',end='')
    sleep(0.5)
    ssh.exec_command(f'docker stats > /home/user/Desktop/docker.txt')
    sleep(write_time)
    ssh.exec_command("\x03")
    sftp_client = ssh.open_sftp()
    sftp_client.get('/home/user/Desktop/docker.txt', f'D:/work/logs/{log_pref}_docker.txt')
    sftp_client.remove('/home/user/Desktop/docker.txt')
    sftp_client.close()
    ssh.close()
    service_list = []
    with open('D:/work/WHPython/stilsoft/ssku/perf.ini','r') as file:
        file_ = file.read()
        for line in file_.split('\n'):
            service_list.append(line)

    need_timer = True
    for service in service_list:
        cpu_list = []
        mem_list = []
        with open(f'D:/work/logs/{log_pref}_docker.txt','r') as file:
            for item in file:
            
                if service in item:
                    try:
                        cpu = item.strip().split()[2]
                        float_cpu = (float(cpu.replace('%',''))/cores)
                        if isinstance(float_cpu, float):
                            cpu_list.append(float_cpu)
                    except:
                        print(f'collect {service} cpu: \033[31m[FAILED]\033[0m')
                        next    
                 
                    try:
                        mem = item.strip().split()[3]
                        char_del = 'TtGgMmKkBib'
                        for i in char_del:
                            mem = mem.replace(i,'')
                        float_mem = (float(mem))
                        if isinstance(float_mem, float): 
                            mem_list.append(float_mem)
                            mem_liter = item.strip().split()[3]
                            num_del = '1234567890.,'
                            for i in num_del:
                                mem_liter = mem_liter.replace(i, '')
                    except:
                        print(f'collect {service} mem: \033[31m[FAILED]\033[0m')
                        next
            
            with open(f'D:/work/logs/{timestamp}_{log_pref}_DOCKER_LOG.txt', 'a') as file:
                    
                file.write(f'{'='*36}\n')
                if need_timer:
                    file.write(f'*{timestamp} {host}*\n')
                file.write(f'{service}\n')    
                file.write(f'{' '*10}CPU (%){' '*8}MEM\n')
                try:
                    file.write(f'ПИКОВОЕ      {round(max(cpu_list),2)}    |    {round(max(mem_list),2)} {mem_liter}\n')
                except:
                    print(service, 'max ERR')
                    file.write('ПИКОВОЕ - ОШИБКА\n')
                    next    
                try:                     
                    file.write(f'МЕДИАННОЕ    {round(median(cpu_list),2)}    |    {round(median(mem_list),2)} {mem_liter}\n')
                except:
                    print(service, 'median ERR')
                    file.write('МЕДИАННОЕ - ОШИБКА\n')                    
                try:
                    file.write(f'МИНИМАЛЬНОЕ   {round(min(cpu_list), 2)}    |    {round(min(mem_list), 2)} {mem_liter}\n')
                except:    
                    print(service, 'min ERR')
                    file.write('МИНИМАЛЬНОЕ - ОШИБКА\n')
                    next   
                need_timer = False      
    os.remove(f'D:/work/logs/{log_pref}_docker.txt')
    print('\033[32m[DONE]\033[0m')


def nethogs_logs(host='192.168.202.221', write_time=60, cores=48):
    log_pref = host.strip().split('.')[-1]
    print('make_logs() \033[5;33m[START]\033[0m')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username='user', password='stilsoft')
    print(f'Подключено к {host}\nmake docker stats logs: ',end='')
    sleep(0.5)
    stdin, stdout, stderr = ssh.exec_command(f'sudo nethogs')
    outer = stdout.read().decode()
    #for line in outer:
    #   if 'TOTAL':

docker_logs()

