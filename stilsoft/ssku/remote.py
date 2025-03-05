class Remote:
    def __init__(self, ip, name='user', secret='stilsoft'):
        self.ip = ip
        self.name = name
        self.secret = secret
        self.back = {'192.168.202.238': '/opt/murom/origin/backend',
         '192.168.202.30': '/opt/murom/origin/backend',
         '192.168.202.18': '/opt/helios/origin/backend',
         '192.168.202.82': '/home/user/dev/rigel/DevOps/Murom',
         '192.168.202.10': '/home/user/rigel/server-app/origin/backend',
         '192.168.202.9': '/home/user/rigel/node-ssku/origin/backend',
         '192.168.207.68': '/opt/server-app/origin/backend',
         '192.168.207.69': '/opt/video-server/origin/backend'
         }
         
        

    def push_lib(self, lib_name):
        import paramiko 
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.name, password=self.secret)
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
        stdin.write(f'{self.secret}\n')
        print('restart node-manager >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose restart node-manager')
        sleep(2)
        print(stdout.read().decode())
        print(stderr.read().decode())


    def push_pack(self, module_name, name='user', secret='stilsoft'):
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

        print('\ncurrent version:')
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
        print('\nfirst curl')
        print(stdout.read().decode())
        print(stderr.read().decode())
        sleep(10)
        print('\nsecond curl')
        with open('D:/work/WHPython/stilsoft/ssku/second_curl.txt', 'r', encoding='utf-8') as file:
            second_curl = file.read()
            second_curl = second_curl.replace("%%MODULE_NAME%%", module_name)
            second_curl = second_curl.replace("%%BACK_DIR%%", self.back[self.ip])

        stdin, stdout, stderr = ssh.exec_command(second_curl)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print('\ndown compose >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose down')
        sleep(10)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print('\nup compose >')
        ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose up')
        sleep(15)
        print('\nupdated version:')
        stdin, stdout, stderr = ssh.exec_command(f'cd {registry_dir}/origin; cat package.json')
        outer = stdout.read().decode()
        for line in outer.split('\n'):
            if module_name in line:
                print(line)
        client.close()
        ssh.close()
        print('Done')

    def cat(self, directory, file, name='user', secret='stilsoft'):
        import paramiko, json
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=name, password=secret)
        stdin, stdout, stderr = ssh.exec_command(f'cd {directory}; cat {file}')
        return stdout.read().decode() 

    def check_versions(self, name='user', secret='stilsoft'):
        import paramiko, json 
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=name, password=secret)
        finded_services = []
        not_finded_servers = []
        not_finded_modules = []
        app_video = {"192.168.202.10": "192.168.202.9",
                     "192.168.207.68": "192.168.207.69"}
        registry_dir = {'192.168.202.238': '/opt/murom/origin/backend/component-registry/registry/origin',
         '192.168.202.30': '/opt/murom/origin/backend/component-registry/registry/origin',
         '192.168.202.18': '/opt/helios/origin/backend/component-registry/registry/origin',
         '192.168.202.82': '/home/user/dev/rigel/DevOps/Murom/component-registry/registry/origin',
         '192.168.202.10': '/home/user/rigel/server-app/origin/backend/component-registry/registry/origin',
         '192.168.202.9': '/home/user/rigel/node-ssku/origin/backend/_component-registry/registry/origin',
         '192.168.207.68': '/opt/server-app/origin/backend/component-registry/registry/origin'}

        if self.ip in app_video.keys():
            server_indicator = 'on app_server:    '
        elif self.ip in app_video.values():
            server_indicator = 'on video-server:  '
        else:
            server_indicator = ''

        try:
            with open('D:\work\WHPython\stilsoft\ssku/module_list.json', 'r', encoding='utf-8') as file:
                print(self.ip)
                module_list = json.load(file)
                name_index = 0
                module_keys_list = list(module_list.keys())

                for k,v in module_list.items():
                    module_name = module_keys_list[name_index]
                    try:
                        outer = self.cat(registry_dir[self.ip], 'package.json')
                        mod_serv = json.loads(outer)['version'][module_name]
                    
                        if v == mod_serv:
                            print(f'{server_indicator}{module_name}'+' '*(24-len(module_name))+'\033[32mMATCH\033[0m')
                        else:
                            print(f'{server_indicator}{module_name}'+' '*(24-len(module_name))+f'\033[31m{mod_serv}\033[0m')
                    except: 
                        not_finded_modules.append(module_name)
                        next        
                    name_index+=1
            print(f'not finded modules: {not_finded_modules}') 
        except:
            print('component-registry not found')
            next
        print('_'*30)
        with open('D:\work\WHPython\stilsoft\ssku/service_list.json', 'r', encoding='utf-8') as file:
            service_list = json.load(file)
            name_index = 0
            service_keys_list = list(service_list.keys())     
            for k,v in service_list.items():
                service_name = service_keys_list[name_index]
                stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; cat docker-compose.yml')
                outer = stdout.read().decode()
                for line in outer.split('\n'):
                    word_1 = line.find('image:')
                    word_2 = line.find(service_name)
                    if word_1 != -1 and word_2 != -1:
                        item = line.split(':')
                        serv_serv = item[-1]
                        finded_services.append(service_name)
                        if v == serv_serv:
                            print(f'{server_indicator}{service_name}'+' '*(24-len(service_name))+'\033[32mMATCH\033[0m')
                        else:
                            print(f'{server_indicator}{service_name}'+' '*(24-len(service_name))+f'\033[31m{serv_serv}\033[0m')
                   
                name_index+=1
            for item in list(service_list.keys()):
                if item not in finded_services:
                    not_finded_servers.append(item)
            print(f'not finded services: {not_finded_servers}') 
        




                 
