class Remote:
    def __init__(self, ip):
        self.ip = ip
        self.back = {'192.168.202.238': '/opt/murom/origin/backend',
         '192.168.202.30': '/opt/murom/origin/backend',
         '192.168.202.18': '/opt/helios/origin/backend',
         '192.168.202.82': '/home/user/dev/rigel/DevOps/Murom',
         '192.168.202.10': '/home/user/rigel/server-app/origin/backend',
         '192.168.202.9': '/home/user/rigel/node-ssku/origin/backend',
         '192.168.207.68': '/opt/server-app/origin/backend'}
        

    def push_lib(self, name, secret, lib_name):
        import paramiko 
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=name, password=secret)
        print(f'Connect to {self.ip}')
        client = ssh.open_sftp()
        lib_dir = f'D:/work/WHPython/stilsoft/lib/{lib_name}.so'
        plugins_dir = f'{self.back[self.ip]}/node-manager/plugins'
        client.put(lib_dir, f'/home/user/{lib_name}.so')
        sleep(2)
        print('stop node-manager >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose stop node-manager')
        sleep(2)
        print(stdout.read().decode())
        print(stderr.read().decode())
        stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/{lib_name}.so {plugins_dir}')
        sleep(1)
        stdin.write(f'{secret}\n')
        print('restart node-manager >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose restart node-manager')
        sleep(2)
        print(stdout.read().decode())
        print(stderr.read().decode())


    def push_pack(self, name, secret, module_name):
        import paramiko
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=name, password=secret)
        print(f'Connect to {self.ip}')
        client = ssh.open_sftp()
        pack_dir = f'D:/work/WHPython/stilsoft/pack/{module_name}.pack'
        registry_dir = f'{self.back[self.ip]}/component-registry/registry'
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
            first_curl = first_curl.replace("%%BACK_DIR%%", self.back[self.ip])

        stdin, stdout, stderr = ssh.exec_command(first_curl)
        print('first curl')
        print(stdout.read().decode())
        print(stderr.read().decode())
        sleep(10)
        print('second curl')
        with open('D:/work/WHPython/stilsoft/ssku/second_curl.txt', 'r', encoding='utf-8') as file:
            second_curl = file.read()
            second_curl = second_curl.replace("%%MODULE_NAME%%", module_name)
            second_curl = second_curl.replace("%%BACK_DIR%%", self.back[self.ip])

        stdin, stdout, stderr = ssh.exec_command(second_curl)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print('down compose >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose down')
        sleep(5)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print('up compose >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose up')
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