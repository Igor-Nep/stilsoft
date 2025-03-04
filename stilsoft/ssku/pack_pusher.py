import paramiko
from time import sleep

back = {'192.168.202.238': '/opt/murom/origin/backend',
         '192.168.202.30': '/opt/murom/origin/backend',
         '192.168.202.18': '/opt/helios/origin/backend',
         '192.168.202.82': '/home/user/dev/rigel/DevOps/Murom',
         '192.168.202.10': '/home/user/rigel/server-app/origin/backend',
         '192.168.202.9': '/home/user/rigel/node-ssku/origin/backend',
         '192.168.207.68': '/opt/server-app/origin/backend'
         
}

def push_lib(app_host, name, secret, lib_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(app_host, port=22, username=name, password=secret)
    print(f'Connect to {app_host}')
    client = ssh.open_sftp()
    lib_dir = f'D:/work/WHPython/stilsoft/lib/{lib_name}.so'
    plugins_dir = f'{back[app_host]}/node-manager/plugins'
    client.put(lib_dir, f'/home/user/{lib_name}.so')
    sleep(2)
    print('stop node-manager >')
    stdin, stdout, stderr = ssh.exec_command(f'cd {back[app_host]}; docker-compose stop node-manager')
    sleep(2)
    print(stdout.read().decode())
    print(stderr.read().decode())
    stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/{lib_name}.so {plugins_dir}')
    sleep(1)
    stdin.write(f'{secret}\n')
    print('restart node-manager >')
    stdin, stdout, stderr = ssh.exec_command(f'cd {back[app_host]}; docker-compose restart node-manager')
    sleep(2)
    print(stdout.read().decode())
    print(stderr.read().decode())
    


def push_pack(app_host, name, secret, module_name):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(app_host, port=22, username=name, password=secret)
    print(f'Connect to {app_host}')
    client = ssh.open_sftp()
    pack_dir = f'D:/work/WHPython/stilsoft/pack/{module_name}.pack'
    registry_dir = f'{back[app_host]}/component-registry/registry'
    client.put(pack_dir, f'/home/user/{module_name}.pack')
    sleep(2)
    stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/{module_name}.pack {registry_dir}')
    sleep(1)
    stdin.write(f'{secret}\n')
    stdin.flush()
    print(stderr.read().decode())

    print('current version:\n')
    stdin, stdout, stderr = ssh.exec_command(f'cd {registry_dir}/origin; cat package.json')
    outer = stdout.read().decode()
    for line in outer.split('\n'):
        if module_name in line:
            print(line)

    with open('D:/work/WHPython/stilsoft/ssku/first_curl.txt', 'r', encoding='utf-8') as file:
        first_curl = file.read()
        first_curl = first_curl.replace("%%MODULE_NAME%%", module_name)
        first_curl = first_curl.replace("%%BACK_DIR%%", back[app_host])

    stdin, stdout, stderr = ssh.exec_command(first_curl)
    print('first curl')
    print(stdout.read().decode())
    print(stderr.read().decode())
    sleep(10)
    print('second curl')
    with open('D:/work/WHPython/stilsoft/ssku/second_curl.txt', 'r', encoding='utf-8') as file:
        second_curl = file.read()
        second_curl = second_curl.replace("%%MODULE_NAME%%", module_name)
        second_curl = second_curl.replace("%%BACK_DIR%%", back[app_host])

    stdin, stdout, stderr = ssh.exec_command(second_curl)
    print(stdout.read().decode())
    print(stderr.read().decode())
    print('down compose >')
    stdin, stdout, stderr = ssh.exec_command(f'cd {back[app_host]}; docker-compose down')
    sleep(5)
    print(stdout.read().decode())
    print(stderr.read().decode())
    print('up compose >')
    stdin, stdout, stderr = ssh.exec_command(f'cd {back[app_host]}; docker-compose up')
    sleep(3)
    print(stdout.read().decode())
    print(stderr.read().decode())
    print('updated version:\n')
    stdin, stdout, stderr = ssh.exec_command(f'cd {registry_dir}/origin; cat package.json')
    outer = stdout.read().decode()
    for line in outer.split('\n'):
        if module_name in line:
            print(line)
    client.close()
    ssh.close()
    print('Done')

push_lib('192.168.202.238','user','stilsoft','libsdp8122')