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
         '192.168.207.69': '/opt/video-server/origin/backend',
         '192.168.202.221': '/opt/vs90/origin/backend'
         }
        
        self.configurate = {
        "192.168.202.238": {"name":"user", "password":"stilsoft", "back_dir":"/opt/murom/origin/backend", "registry_dir":"/component-registry/registry/origin", "need_video":False},
        "192.168.202.30": {"name":"user", "password":"stilsoft", "back_dir":"/opt/murom/origin/backend", "registry_dir":"/component-registry/registry/origin", "need_video":False},
        "192.168.202.82": {"name":"user", "password":"stilsoft", "back_dir":"/home/user/dev/rigel/DevOps/Murom", "registry_dir":"", "need_video":False},
        "192.168.202.10": {"name":"user", "password":"stilsoft", "back_dir":"/home/user/rigel/server-app/origin/backend", "registry_dir":"/component-registry/registry/origin", "need_video":True},
        "192.168.202.9": {"name":"user", "password":"stilsoft", "back_dir":"/home/user/rigel/node-ssku/origin/backend", "registry_dir":"/_component-registry/registry/origin", "need_video":False, "compose_name":"docker-compose.yml"},
        "192.168.207.68": {"name":"user", "password":"stilsoft1", "back_dir":"/opt/server-app/origin/backend/", "registry_dir":"/component-registry/registry/origin", "need_video":True},
        "192.168.207.69": {"name":"user", "password":"stilsoft", "back_dir":"/opt/video-server/origin/backend", "registry_dir":"", "need_video":False, "compose_name":"docker-compose.yml"},
        "192.168.202.18": {"name":"user", "password":"stilsoft", "back_dir":"/opt/helios/origin/backend", "registry_dir":"/component-registry/registry/origin", "need_video":False},
        "192.168.202.221": {"name":"user", "password":"stilsoft", "back_dir":"/opt/vs90/origin/backend", "registry_dir":"/component-registry/registry/origin", "need_video":False},
        "192.168.202.200": {"name":"user", "password":"stilsoft", "back_dir":"/opt/onvif-server", "registry_dir":"/config", "need_video":False}
        }

        self.video_partner = {"192.168.202.10":"192.168.202.9",
                              "192.168.207.68":"192.168.207.69"
                              }
        
        self.GREEN = '\033[32m'
        self.RED = '\033[31m'
        self.YELLOW = '\033[33m'
        self.GREY = '\033[90m'
        self.NON = '\033[0m'

    
        host_file =  open('c:/windows/system32/drivers/etc/hosts', 'r')
        len_host = int(len(host_file.readlines()))
        host_file.seek(0,0)
        active_host = []
        for _ in range(0, len_host):
            s = host_file.readline()#.split(' ')[0]
            if '#' not in s:
                active_host.append(s)
        newti=str(active_host[0])
        self.terminal('blue',(newti))
        host_file.close() 


  


    def config(self,param):
        return self.configurate[self.ip][param]
    
    def cls(self):
        import sys
        sys.stdout.write('\r' + ' ' * 100 + '\r')
        sys.stdout.flush()        
        log_pref = str(self.ip).strip().split('.')[-1]

    def terminal(self,paint,text,nextrow=True):
        import sys
        from color import color
        self.cls()
        if paint == 'yellow':
            sys.stdout.write(f'{color.grey('[')}{color.yellow(f'{text}')}{color.grey(']')}')
        elif paint == 'green':
            sys.stdout.write(f'{color.grey('[')}{color.green(f'{text}')}{color.grey(']')}')
        elif paint == 'red':
            sys.stdout.write(f'{color.grey('[')}{color.red(f'{text}')}{color.grey(']')}')
        elif paint == 'blue':
            sys.stdout.write(f'{color.grey('[')}{color.blue(f'{text}')}{color.grey(']')}')
        elif paint == 'grey':
            sys.stdout.write(f'{color.grey('[')}{color.grey(f'{text}')}{color.grey(']')}')
        elif paint == 'non':
            sys.stdout.write(f'{color.grey('[')}{color.non(f'{text}')}{color.grey(']')}')
        elif paint == 'mod':    
            sys.stdout.write(f'{color.grey('[')}{text}{color.grey(']')}')
        sys.stdout.flush()
        
            
        if nextrow:
            sys.stdout.write('\n')

    def hosts_check(self):
        from color import color
        host_file =  open('c:/windows/system32/drivers/etc/hosts', 'r')
        len_host = int(len(host_file.readlines()))
        host_file.seek(0,0)
        active_host = []
        for _ in range(0, len_host):
            s = host_file.readline()
            if '#' not in s:
                active_host.append(s)
        newti=str(active_host[0])
        self.terminal('blue',(newti))
        host_file.close() 
    

    def push_lib(self, lib_name):
        import paramiko 
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.configurate[self.ip]['name'], password=self.configurate[self.ip]['password'])
        print(f'Connect to {self.ip}')
        client = ssh.open_sftp()
        lib_dir = f'D:/work/WHPython/stilsoft/lib/{lib_name}.so'
        plugins_dir = f'{self.configurate[self.ip]['back_dir']}/node-manager/plugins'
        client.put(lib_dir, f'/home/user/{lib_name}.so')
        sleep(2)
        print('stop node-manager >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose stop node-manager')
        sleep(2)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print('update lib')
        stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/{lib_name}.so {plugins_dir}')
        sleep(1)
        try:
            stdin.write(f'{self.configurate[self.ip]['password']}\n')
        except:
            next    
        print('restart node-manager >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose restart node-manager')
        sleep(2)
        print(stdout.read().decode())
        print(stderr.read().decode())
        try:
            print('del tmp_lib >')
            client.remove(f'/home/user/{lib_name}.so')
        except:
            print('can not del')
            next
        client.close()
        ssh.close()
        self.terminal('non','done')    



    def push_pack(self, module_name):
        import paramiko
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.configurate[self.ip]['name'], password=self.configurate[self.ip]['password'])
        print('self_secr: ', self.secret)
        print(f'Connect to {self.ip}')
        client = ssh.open_sftp()
        reg_dir = f'{self.configurate[self.ip]['back_dir']}{self.configurate[self.ip]['registry_dir']}'
        pack_dir = f'D:/work/WHPython/stilsoft/pack/{module_name}.pack'
        registry_dir = f'{self.back[self.ip]}/component-registry/registry'
        client.put(pack_dir, f'/home/user/{module_name}.pack')
        sleep(2)
        stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/{module_name}.pack {reg_dir}')
        sleep(1)
        try:
            stdin.write(f'{self.secret}\n')
            stdin.flush()
            print(stderr.read().decode())
        except:
            next    
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
        sleep(11)
        print('\nsecond curl')
        with open('D:/work/WHPython/stilsoft/ssku/second_curl.txt', 'r', encoding='utf-8') as file:
            second_curl = file.read()
            second_curl = second_curl.replace("%%MODULE_NAME%%", module_name)
            second_curl = second_curl.replace("%%BACK_DIR%%", self.back[self.ip])

        stdin, stdout, stderr = ssh.exec_command(second_curl)
        print(stdout.read().decode())
        print(stderr.read().decode())
        print('restart docker-compose >')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose restart')
        print(stdout.read().decode())
        print(stderr.read().decode())
        #print('\ndown compose >')
        #stdin, stdout, stderr = ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose down')
        #sleep(10)
        #print(stdout.read().decode())
        #print(stderr.read().decode())
        #print('\nup compose >')
        #ssh.exec_command(f'cd {self.back[self.ip]}; docker-compose up')
        #sleep(15)
        print('\nupdated version:')
        stdin, stdout, stderr = ssh.exec_command(f'cd {registry_dir}/origin; cat package.json')
        outer = stdout.read().decode()
        try:
            print('del pack >')
            client.remove(f'/home/user/{module_name}.pack')
        except:
            print('can not del')
            next  
        for line in outer.split('\n'):
            if module_name in line:
                print(line)
        client.close()
        ssh.close()
        self.terminal('non','done')

    def cat(self, directory, file):
        import paramiko, json
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        stdin, stdout, stderr = ssh.exec_command(f'cd {directory}; cat {file}')
        return stdout.read().decode()

    def terminal_command(self, param):
        import paramiko
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        print(self.config('password'))
        print(f'Connect to {self.ip}')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; {param}')
        sleep(2)
        print(stdout.read().decode())


    def check_versions(self, project):
        from color import color
        import paramiko, json, os
        from time import sleep

        need_change = []
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        self.terminal("non", "check versions")
        self.terminal("non", self.ip)
        finded_services = []
        log_pref = str(self.ip).strip().split('.')[-1]
        if project == 'ssku':
            self.terminal("non", 'Syn5')
            json_path = 'D:/work/WHPython/stilsoft/ssku/remote/json/ssku'
        else:
            self.terminal("non", 'Murom')
            json_path = 'D:/work/WHPython/stilsoft/ssku/remote/json/murom'
        if self.ip in self.video_partner.keys() or project == 'murom':
            server_indicator = 'on app_server:    '
        elif self.ip in self.video_partner.values():
            server_indicator = 'on video-server:  '
        else:
            server_indicator = ''

        try:
            sftp_client = ssh.open_sftp()
        except:
            print(color.red('can not open sftp'))
            next
        try:
            sftp_client.get(f'{self.config('back_dir')}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker.txt')
            sleep(1)
             
        except:
            print(color.red('can not get docker file'))
            next

        try:
            sftp_client.get(f'{self.config('back_dir')}{self.config('registry_dir')}/package.json', f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.txt')
            sleep(1)
                
        except:
            print(color.red('can not get package file'))
            next
        sftp_client.close()                 
        try:
            print(color.yellow('check modules versions \r'))
            with open(f'{json_path}/module_list.json', 'r', encoding='utf-8') as file:
                module_list = json.load(file)
                name_index = 0
                module_keys_list = list(module_list.keys())
                

                for k,v in module_list.items():
                    module_name = module_keys_list[name_index]
                    try:
                       #outer = self.cat(f'{self.config('back_dir')}{self.config('registry_dir')}/origin', 'package.json')
                       with open(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.txt') as file:
                           outer = file.read()
                    except:
                       print(color.red('can not open package.json'))
                       next
                    try:  
                       mod_serv = json.loads(outer)['version'][module_name]
                       if v == mod_serv:
                           print(f'{server_indicator}{module_name}'+' '*(32-len(module_name))+f'{color.grey(v)} {color.green(f'{mod_serv}')}')
                       else:
                           print(f'{server_indicator}{module_name}'+' '*(32-len(module_name))+f'{color.grey(v)} {color.red(mod_serv)}')
                           need_change.append('app_module')
                    except:
                        print(color.grey('can not get module '), color.red(f'{module_name}'))
                        next        
                    name_index+=1
            #self.terminal('green','done')

        except:
            pass

        try:
            print(color.yellow('check services versions \r'))
            with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                service_list = json.load(file)
                name_index = 0
                service_keys_list = list(service_list.keys())     
                for k,v in service_list.items():
                    service_name = service_keys_list[name_index]
                    try:
                        with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker.txt', 'r') as file:
                            outer = file.read()
                            
                        for line in outer.split('\n'):
                                if 'image:' in line and f'{service_name}:' in line and '#' not in line:
                                    item = line.split(':')
                                    docker_service_version = item[-1]
                                    if v == docker_service_version:
                                        print(f'{server_indicator}{service_name}'+' '*(32-len(service_name))+f'{color.grey(v)}  {color.green(docker_service_version)}')
                                    else:
                                        print(f'{server_indicator}{service_name}'+' '*(32-len(service_name))+f'{color.grey(v)}  {color.red(docker_service_version)}')
                                        need_change.append('app_service')
                                else:
                                    pass

                    except:
                        print('can not open docker file')
                        next
                    name_index+=1
            if self.ip not in self.video_partner.keys():
                self.terminal('green','done')
     
                    
        except:
            print('error with open sevice_list'+'_'*30)
            next
        ssh.close()
        
        if self.ip in self.video_partner.keys():
            server_indicator = 'on video-server:  '
            try:    
                ip = self.video_partner[self.ip]
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, port=22, username=self.configurate[ip]['name'], password=self.configurate[ip]['password'])
                sftp_client = ssh.open_sftp()
                sftp_client.get(f'{self.configurate[ip]['back_dir']}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker.txt')
                sftp_client.close()
                
            
            except:
                print('can not connect to video server')
                next
            try:
                with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                    service_list = json.load(file)
                    name_index = 0
                    service_keys_list = list(service_list.keys())     
                    for k,v in service_list.items():
                        service_name = service_keys_list[name_index]
                        try:
                            with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker.txt', 'r') as file:
                                outer = file.read()
                            for line in outer.split('\n'):
                                    if 'image:' in line and f'{service_name}:' in line and '#' not in line:
                                        item = line.split(':')
                                        docker_service_version = item[-1]
                                        finded_services.append(service_name)
                                        if v == docker_service_version:
                                            print(f'{server_indicator}{service_name}'+' '*(32-len(service_name))+f'{color.grey(v)}  {color.green(docker_service_version)}')
                                        else:
                                            print(f'{server_indicator}{service_name}'+' '*(32-len(service_name))+f'{color.grey(v)}  {color.red(docker_service_version)}')
                                            need_change.append('video_service')

                        except:
                            next
                        name_index+=1
            except:
                print('can not open service_list')
            try:
                os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker.txt')
                os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.txt')
            except Exception as err:
                print(f'can not remove local temp files. {err}')    
            
            self.terminal('green','done')

        return list(set(need_change))                      


    def check_versions_by_logs(self, project):
        from color import color
        import paramiko, json 
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        print('> init check versions by logs')
        print(f'connected {self.ip}')
        
        not_finded_services = []
        if project == 'ssku':
            print('project - ssku')
            json_path = 'D:/work/WHPython/stilsoft/ssku/remote/json/ssku'
        else:
            print('project - murom')
            json_path = 'D:/work/WHPython/stilsoft/ssku/remote/json/ssku'
        ssh.exec_command(f'cd {self.config('back_dir')}; docker-compose restart')
        sleep(10)
        try:
            with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                service_list = json.load(file)
                name_index = 0
                service_keys_list = list(service_list.keys())     
                for k,v in service_list.items():
                    service_name = service_keys_list[name_index]
                    try:
                        #outer = self.cat(self.back[self.ip], 'docker-compose.yml')
                        #outer = stdout.read().decode()
                        print(service_keys_list[name_index])
                        #stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose logs --tail 10000 | grep sdp858i | grep started | grep {v}')
                        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose logs --tail 10000 {service_keys_list[name_index]} | grep started | grep {v}')
                        outer = stdout.read().decode()

                        for line in outer.split('\n'):
                            #word_1 = line.find('image:')
                            #word_2 = line.find(service_name)
                            #if word_1 != -1 and word_2 != -1:
                                #item = line.split(':')
                                #serv_serv = item[-1]
                                #finded_services.append(service_name)
                                if v in line:
                                    print(line)
                                    print(f'{service_name}'+' '*(24-len(service_name))+f'\033[32mMATCH\033[0m ({v})')
                                else:
                                    print('\033[33mnot_found\033[0m')
                    except:
                        not_finded_services.append(service_name)
                        next
                    name_index+=1
            print(f'not finded services: {not_finded_services}')    
        except:
            print('_'*30)
            next

    def check_versions_by_manifest(self, project):
        import paramiko, json, fnmatch
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        client = ssh.open_sftp()
        print('> init check versions by manifest')
        print(f'connected {self.ip}')
        not_finded_services = []
        if project == 'ssku':
            print('project - ssku')
            json_path = 'D:/work/WHPython/stilsoft/ssku/remote/json/ssku'
        else:
            print('project - murom')
            json_path = 'D:/work/WHPython/stilsoft/ssku/remote/json/ssku'
        try:
            with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                service_list = json.load(file)
                name_index = 0
                service_keys_list = list(service_list.keys())
                for k,v in service_list.items():
                    service_name = service_keys_list[name_index]
                    try:
                        found_manifest = None
                        for file in client.listdir(self.configurate[self.ip]['back_dir']):
                            if fnmatch.fnmatch(file, 'manifest' + '*'):
                                found_manifest = file
                                break


                        with client.open(f'{self.configurate[self.ip]['back_dir']}/{found_manifest}', 'r') as file:
                            pre_file = file.read().decode('utf-8')
                            json_file = json.loads(pre_file)
                            if json_file['services'][service_name][0] == v:
                                print(f'{service_name} \033[32mMATCH\033[0m {v}')
                        name_index+=1
                    except:
                        print(f'{service_name} \033[33mnot_found\033[0m')
                        name_index+=1
                        next
                        
        except:
            next


    def change_versions(self, project):
        from color import color
        import paramiko, json, os
        from time import sleep
        from datetime import datetime
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        if self.ip in self.video_partner.keys():
            server_indicator = 'app_server'
        elif self.ip in self.video_partner.values():
            server_indicator = 'video-server'
        else:
            server_indicator = ''
        print('change services versions > ')

        print(f'connected {color.grey(server_indicator)} {self.ip}')
        
        log_pref = str(self.ip).strip().split('.')[-2]+'.'+str(self.ip).strip().split('.')[-1]
        json_path = f'D:/work/WHPython/stilsoft/ssku/remote/json/{project}'

        try:
            with open(f'{json_path}/module_list.json', 'r', encoding='utf-8') as file:
                module_list = json.load(file)
                name_index = 0
                module_keys_list = list(module_list.keys())
        except Exception as err:
            print(f'open module_list.json error: {color.red(err)}')
            return

        try:
            with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                service_list = json.load(file)
        except Exception as err:
            print(f'open service_list.json error: {color.red(err)}')
            return

        try:
            sftp_client = ssh.open_sftp()
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            sftp_client.get(f'{self.config('back_dir')}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/backup/{timestamp}_{log_pref}_docker-compose.yml')
            sleep(1)
            sftp_client.get(f'{self.config('back_dir')}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
            sleep(1)
            with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', 'r', encoding='utf-8') as file:
                docker_lines = file.readlines()
        except Exception as err:
            print(f'open docker-compose.yml error: {color.red(err)}')
            return

        changes = False
        for service_name, new_version in service_list.items():
            for i, line in enumerate(docker_lines):
                if f'{service_name}:' in line and 'image:' in line:
                    current_version = line.split(':')[-1].strip()
                    if current_version != new_version:
                        print(f'update {color.grey(service_name)} from {color.grey(current_version)} to {color.green(new_version)}')
                        docker_lines[i] = line.replace(current_version, new_version)
                        changes = True
                        if service_name == 'api-gateway':
                            continue
                        else:
                            break

        if changes:
            try:
                with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', 'w', encoding='utf-8') as file:
                    file.writelines(docker_lines)
                self.terminal('green','done')
            except Exception as err:
                print(f'writing docker-compose.yml error: {color.red(err)}')
        else:
            print(color.yellow('docker-compose is up to date')) 
        if changes:
            answer = input(f'обновить docker-compose.yml на {self.ip}? (y/n): ')
            if answer == 'y':
                print(color.yellow('[IN PROGRESS]'))
                sftp_client.put(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', f'/home/user/docker-compose.yml')
                print('copying docker-compose.yml to server')
                sleep(1)
                stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/docker-compose.yml {self.config('back_dir')}')
                sleep(1)
                try:
                    stdin.write(self.config('password')+'\n')
                    stdin.flush()
                    print(stderr.read().decode())
                except:
                    next
                sleep(1) 
                stdin, stdout, stderr = ssh.exec_command(f'cd {self.config('back_dir')}; docker-compose up -d')
                print('updating docker-compose')
                print(stdout.read().decode())
                print(stderr.read().decode())
                stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose ps')
                status = stdout.read().decode()    
                for line in status.split('\n'):
                    if 'Exit' in line or "Restarting" in line:
                        module_name = line.split()[0]
                        print(f'{module_name} остановлен')
                        try:
                            print(f'restarting {module_name}')
                            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose restart {module_name}')
                            status = stderr.read().decode()
                        except:
                            print(f'can not restart docker-compose')
                        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose ps')
                        status = stdout.read().decode()
                        for line in status.split('\n'):
                            if 'Exit' in line:
                                module_name = line.split()[0]
                                print(f'{module_name} проблема запуска')
                    
                print('docker-compose is updated')             
                ssh.exec_command(f'rm /home/user/docker-compose.yml')
                print('deleting temp files  ... \r')
                try:
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
                except Exception as err:
                    print(f'delete local temp file error {err}')
                    pass
                self.terminal('non','done')
            else:
                try:
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose//backup/{timestamp}_{log_pref}_docker-compose.yml')
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
                except Exception as err:
                    print(f'delete local temp files error {err}')
                    pass
                self.terminal('yellow','done')


    def change_servise_versions(self, ip, project):
        from color import color
        import paramiko, json, os
        from time import sleep
        from datetime import datetime
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=self.configurate[ip]['name'], password=self.configurate[ip]['password'])

        print('change services versions > ')

        print(f'connected {color.grey(ip)}')
        
        log_pref = str(self.ip).strip().split('.')[-2]+'.'+str(self.ip).strip().split('.')[-1]
        json_path = f'D:/work/WHPython/stilsoft/ssku/remote/json/{project}'

        try:
            with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                service_list = json.load(file)
        except Exception as err:
            print(f'open service_list.json error: {color.red(err)}')
            return

        try:
            sftp_client = ssh.open_sftp()
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            sftp_client.get(f'{self.configurate[ip]['back_dir']}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/backup/{timestamp}_{log_pref}_docker-compose.yml')
            sleep(1)
            sftp_client.get(f'{self.configurate[ip]['back_dir']}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
            sleep(1)
            with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', 'r', encoding='utf-8') as file:
                docker_lines = file.readlines()
        except Exception as err:
            print(f'open docker-compose.yml error: {color.red(err)}')
            return

        changes = False
        
        for service_name, new_version in service_list.items():
            for i, line in enumerate(docker_lines):
                if f'{service_name}:' in line and 'image:' in line:
                    current_version = line.split(':')[-1].strip()
                    if current_version != new_version:
                        print(f'update {color.grey(service_name)} from {color.grey(current_version)} to {color.green(new_version)}  ... \r')
                        docker_lines[i] = line.replace(current_version, new_version)
                        changes = True
                        if service_name == 'api-gateway':
                            continue
                        else:
                            break

        if changes:
            try:
                with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', 'w', encoding='utf-8') as file:
                    file.writelines(docker_lines)
                self.terminal('non','done')

            except Exception as err:
                print(f'writing docker-compose.yml error: {color.red(err)}')
        else:
            print(color.yellow('docker-compose is up to date')) 
        if changes:
            answer = 'y'
            if answer == 'y':
                sftp_client.put(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', f'/home/user/docker-compose.yml')
                print('copying docker-compose.yml to server')
                sleep(1)

                stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/docker-compose.yml {self.configurate[ip]['back_dir']}')
                sleep(1)
                
                try:
                    stdin.write(self.configurate[ip]['password']+'\n')
                    stdin.flush()
                    print(stderr.read().decode())
                except:
                    next
                sleep(1) 
                stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[ip]['back_dir']}; docker-compose up -d')
                print('updating docker-compose')
                print(stdout.read().decode())
                print(stderr.read().decode())
                stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[ip]['back_dir']} && docker-compose ps')
                status = stdout.read().decode()    
                for line in status.split('\n'):
                    if 'Exit' in line or "Restarting" in line:
                        module_name = line.split()[0]
                        print(f'{module_name} остановлен')
                        try:
                            print(f'restarting {module_name}')
                            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[ip]['back_dir']} && docker-compose restart {module_name}')
                            status = stderr.read().decode()
                        except:
                            print(f'can not restart docker-compose')
                        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[ip]['back_dir']} && docker-compose ps')
                        status = stdout.read().decode()
                        for line in status.split('\n'):
                            if 'Exit' in line or 'Restarting' in line:
                                module_name = line.split()[0]
                                print(f'{module_name} проблема запуска')
                    
                print('docker-compose is updated')             
                ssh.exec_command(f'rm /home/user/docker-compose.yml')
                print('deleting temp files  ... ', end='')
                try:
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
                except Exception as err:
                    print(f'delete local temp file error {err}')
                    pass
                self.terminal('green','done')
            else:
                try:
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose//backup/{timestamp}_{log_pref}_docker-compose.yml')
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
                except Exception as err:
                    print(f'delete local temp files error {err}')
                    pass
                self.terminal('yellow','done')



    def push_lib_targeting(self, ip, lib_name, lib_version):
        import paramiko, os
        from color import color
        from time import sleep

    
        with paramiko.SSHClient() as ssh:
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip, port=22, username=self.configurate[ip]['name'], password=self.configurate[ip]['password'])
            except Exception as e:
                print(f'{color.red("ERROR: ")}Не удалось подключиться: {str(e)}')
                return

            with ssh.open_sftp() as sftp:
                lib_dir = f'd:/work/WHPython/stilsoft/lib/{lib_name}/{lib_version}'
                if not os.path.exists(f'{lib_dir}/lib{lib_name}.so'):
                    print(f'{color.red("ERROR: ")}библиотека {lib_name} {lib_version} отсутствует в локальном репозитории : <push_lib_target()>')
                    return

                plugins_dir = f'{self.configurate[ip]['back_dir']}/node-manager/plugins'

                try:
                    sftp.put(f'{lib_dir}/lib{lib_name}.so', f'/home/user/lib{lib_name}.so')
                    sleep(2)
                    print(f'update lib {color.grey(lib_name)} to {color.green(lib_version)}\r')
                    print('stop node-manager >')
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose stop node-manager')
                    sleep(2)
                    print(stdout.read().decode())
                    print(stderr.read().decode())
                

                    stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/lib{lib_name}.so {plugins_dir}')
                    sleep(2)
                    try:
                        stdin.write(f'{self.configurate[ip]['password']}\n')
                    except:

                        next

                    

                    print('restart node-manager >')
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose restart node-manager')
                    sleep(2)
                    print(stdout.read().decode())
                    print(stderr.read().decode()) 
                    self.terminal('non','done')
                except Exception as err:
                    print(f'{color.red("ERROR: ")}ошибка при копировании библиотеки {lib_name} {lib_version}: {str(err)}')
                finally:
                    try:
                        sftp.remove(f'/home/user/lib{lib_name}.so') 
                    except Exception as err:
                        print(f'can not delete temp lib files: {err}')
                        pass

        self.terminal('non','done')



    def push_lib_target(self, ip, lib_name, lib_version):
        import paramiko, os
        from color import color
        from time import sleep
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=self.configurate[ip]['name'], password=self.configurate[ip]['password'])
        client = ssh.open_sftp()
        lib_dir = f'D:/work/WHPython/stilsoft/lib/{lib_name}/{lib_version}'
        if os.path.exists(f'{lib_dir}/lib{lib_name}.so'):
            pass
        else:
            print(f'{color.red("ERROR: ")}библиотека {lib_name} {lib_version} отсутствует в локальном репозитории : <push_lib_target()>')
            return
        plugins_dir = f'{self.configurate[ip]['back_dir']}/node-manager/plugins'
        try:
            client.put(f'{lib_dir}/lib{lib_name}.so', f'/home/user/lib{lib_name}.so')
            sleep(2)
        except Exception as err:
            print(f'{color.red("ERROR: ")}ошибка при копировании библиотеки {lib_name} {lib_version} : <push_lib_target()>')
            return

        print(f'update lib {color.grey(lib_name)} to {color.green(lib_version)} \r')
        try:
            stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/lib{lib_name}.so {plugins_dir}')
            sleep(1)
        except Exception as err:
            print(f'color.red(ERROR: )copying lib{lib_name}.so to plugins_dir error: {err}')

        try:
            stdin.write(f'{self.configurate[ip]['password']}\n')
        except:

            next

        self.terminal('non','done')
        try:
            print('deleting temp lib files: \r')
            client.remove(f'/home/user/lib{lib_name}.so')
            pass
        except Exception as err:
            print(f'can not delete temp lib files: {err}')
            next
        client.close()
        ssh.close()
        self.terminal('non','done')


    def change_modules_versions(self, ip, project):
        from color import color
        import paramiko, json, os
        from time import sleep
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        package = True
        lib_error = False
        module_change_list = {}
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, port=22, username=self.configurate[ip]['name'], password=self.configurate[ip]['password'])
        sftp_client = ssh.open_sftp()
        print('change modules versions > ')
        print(f'connected {color.grey(ip)}')
        if ip in self.video_partner.values():
            package = False
        log_pref = str(self.ip).strip().split('.')[-2]+'.'+str(self.ip).strip().split('.')[-1]
        json_path = f'D:/work/WHPython/stilsoft/ssku/remote/json/{project}'

        try:
            with open(f'{json_path}/module_list.json', 'r', encoding='utf-8') as file:
                module_list = json.load(file)
        except Exception as err:
            print(f'open module_list.json error: {color.red(err)}')
            return
        if package:
            try:
                sftp_client.get(f'{self.configurate[ip]['back_dir']}{self.configurate[ip]['registry_dir']}/package.json', f'D:/work/WHPython/stilsoft/ssku/remote/package/backup/{timestamp}_{log_pref}_package.json')
                sleep(1)
                sftp_client.get(f'{self.configurate[ip]['back_dir']}{self.configurate[ip]['registry_dir']}/package.json', f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json')
                sleep(1)
                with open(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json', 'r', encoding='utf-8') as file:
                    package_lines = file.readlines()
                with open(f'{json_path}/module_list.json', 'r', encoding='utf-8') as file:
                    module_list = json.load(file)
                    
            except Exception as err:
                    print(f'open package.json error: {color.red(err)}')
                    next            
                
                

        module_changes = False
        if package:
            for module_name, new_version in module_list.items():
                for i, line in enumerate(package_lines):
                    if f'{module_name}' in line:
                        crr_version = line.split(':')[1].strip()
                        if ',' in line:
                            current_version = crr_version.split(',')[0]
                        else:
                            current_version = crr_version
                        if current_version[1:-1] != new_version:
                            if len(current_version) < 17:
                                print(f'update {color.grey(module_name)} form {color.grey(current_version[1:-1])} to {color.green(new_version)}')
                                module_change_list[module_name] = new_version
                                lib_dir = f'D:/work/WHPython/stilsoft/lib/{module_name}/{new_version}'
                                if os.path.exists(f'{lib_dir}/lib{module_name}.so'):
                                    pass
                                else:
                                    print(f'{color.red("ERROR: ")}библиотека {color.grey(module_name)} версии {color.grey(new_version)} отсутствует в локальном репозитории')
                                    lib_error = True
                                    continue
                                package_lines[i] = line.replace(f'{current_version[1:-1]}', f'{new_version}')
                            else: 
                                continue    
                            module_changes = True
  
                            break

        if module_changes:
            try:
                if package:
                    with open(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json', 'w', encoding='utf-8') as file:
                        file.writelines(package_lines)
                else:
                    if package:
                        print(color.yellow('module list is up-to-date'))
            except Exception as err:
                if package:
                    print(f'writing package.json error: {color.red(err)}')
        else:
            if not lib_error:
                print(color.yellow('module list is up-to-date'))                
        if ip in self.video_partner.values():
            module_changes = True
            
        if module_changes :
                if package:
                    try:
                        sftp_client.put(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json', f'/home/user/package.json')
                        print(f'copying package.json to server \r')
                        sleep(2)
                    except Exception as err:
                        print(f'{color.red("ERROR: ")}copying package.json to server error: {err}')
                    try:    
                        stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/package.json {self.configurate[ip]['back_dir']}{self.configurate[ip]['registry_dir']}/')
                        sleep(1)
                    except Exception as err:
                        print(f'{color.red("ERROR: ")}copying package.json to server error: {err}')
                    try:
                        stdin.write(self.configurate[ip]['password']+'\n')
                        stdin.flush()
                        print(stderr.read().decode())
                    except:
                        next
                    sleep(1)
                    self.terminal('non','done')                     
                if len(module_change_list) > 0:
                    print('updating module list >')
                    print('stop node-manager: ')
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose stop node-manager')
                    print(stdout.read().decode())
                    print(stderr.read().decode())
                    sleep(2)
                    for module_name, new_version in module_change_list.items():
                        if os.path.exists(f'D:/work/WHPython/stilsoft/lib/{module_name}/{new_version}/lib{module_name}.so'):
                            try:
                                self.push_lib_target(ip, module_name, new_version)
                            except Exception as err:
                                print(f'update {module_name} {new_version} error {err}')
                        else:
                            print(f'{color.red("ERROR: ")}библиотека {color.grey(module_name)} {color.grey(new_version)} отсутствует в локальном репозитории')
                    
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose restart node-manager')
                    sleep(2)
                    print(stdout.read().decode())
                    print(stderr.read().decode())
                try:
                    sftp_client.remove(f'/home/user/package.json')
                except Exception as err:
                    print(f'can not delete package.json fom /user: {err}')    
                sftp_client.close()
                ssh.close()    
                self.terminal('green','done')
        if ip in self.video_partner.keys():

            video_ip = self.video_partner[ip]

            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(video_ip, port=22, username=self.configurate[video_ip]['name'], password=self.configurate[video_ip]['password'])
            sftp_client = ssh.open_sftp()
            print('change modules versions > ')
            print(f'connected {color.grey(video_ip)}')
  
            if len(module_change_list) > 0:
                    print('updating module list >')
                    print('stop node-manager: ')
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[video_ip]['back_dir']}; docker-compose stop node-manager')
                    sleep(2)
                    print(stdout.read().decode())
                    print(stderr.read().decode())
                    for module_name, new_version in module_change_list.items():
                        if os.path.exists(f'D:/work/WHPython/stilsoft/lib/{module_name}/{new_version}/lib{module_name}.so'):
                            try:
                                
                                self.push_lib_target(video_ip, module_name, new_version)
                            except Exception as err:
                                print(f'update {module_name} {new_version} error {err}')
                        else:
                            print(f'{color.red("ERROR: ")}библиотека {color.grey(module_name)} {color.grey(new_version)} отсутствует в локальном репозитории')
                    
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[video_ip]['back_dir']}; docker-compose restart node-manager')
                    sleep(2)
                    print(stdout.read().decode())
                    print(stderr.read().decode())
            self.terminal('green','done')
            try:
                os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json')
                
            except Exception as err:
                print(f'delte local temp file error {err}')    

    def update_versions(self, project='ssku'):
        from color import color
        need_changes = self.check_versions(project)

        if need_changes:
            answer = input(f'обновить версии на {self.ip}? (y/n): ')
            if answer == 'y':
                for item in need_changes:
                    if 'app_service' in item:
                        self.change_servise_versions(self.ip,project)
                    elif 'video_service' in item:
                        self.change_servise_versions(self.video_partner[self.ip],project)
                    elif 'app_module' in item:
                        self.change_modules_versions(self.ip,project)

            else:
                self.terminal('red','exit')
                exit()            
        else:
            print(color.yellow('versions is up-to-date'))


               


    def change_versions_modules(self, project):
        from color import color
        import paramiko, json, os
        from time import sleep
        from datetime import datetime
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        if self.ip in self.video_partner.keys():
            server_indicator = 'app_server'
        elif self.ip in self.video_partner.values():
            server_indicator = 'video-server'
        else:
            server_indicator = ''
        print('change services versions > ')

        print(f'connected {color.grey(server_indicator)} {self.ip}')
        
        log_pref = str(self.ip).strip().split('.')[-2]+'.'+str(self.ip).strip().split('.')[-1]
        json_path = f'D:/work/WHPython/stilsoft/ssku/remote/json/{project}'

        try:
            with open(f'{json_path}/module_list.json', 'r', encoding='utf-8') as file:
                module_list = json.load(file)
        except Exception as err:
            print(f'open module_list.json error: {color.red(err)}')
            return

        try:
            with open(f'{json_path}/service_list.json', 'r', encoding='utf-8') as file:
                service_list = json.load(file)
        except Exception as err:
            print(f'open service_list.json error: {color.red(err)}')
            return

        try:
            sftp_client = ssh.open_sftp()
            timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
            sftp_client.get(f'{self.config('back_dir')}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/backup/{timestamp}_{log_pref}_docker-compose.yml')
            sleep(1)
            sftp_client.get(f'{self.config('back_dir')}/docker-compose.yml', f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
            sleep(1)
            with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', 'r', encoding='utf-8') as file:
                docker_lines = file.readlines()
        except Exception as err:
            print(f'open docker-compose.yml error: {color.red(err)}')
            return
        if server_indicator != 'video-server':
            try:
                sftp_client.get(f'{self.config('back_dir')}{self.config('registry_dir')}/package.json', f'D:/work/WHPython/stilsoft/ssku/remote/package/backup/{timestamp}_{log_pref}_package.json')
                sleep(1)
                sftp_client.get(f'{self.config('back_dir')}{self.config('registry_dir')}/package.json', f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json')
                sleep(1)
                with open(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json', 'r', encoding='utf-8') as file:
                    package_lines = file.readlines()
                with open(f'{json_path}/module_list.json', 'r', encoding='utf-8') as file:
                    module_list = json.load(file)
                    module_change_list = {}
            except Exception as err:
                print(f'open package.json error: {color.red(err)}')
                return

        module_changes = False
        service_changes = False
        if server_indicator != 'video-server':
            for module_name, new_version in module_list.items():
                for i, line in enumerate(package_lines):
                    if f'{module_name}' in line:
                        crr_version = line.split(':')[1].strip()
                        if ',' in line:
                            current_version = crr_version.split(',')[0]
                        else:
                            current_version = crr_version
                        if current_version[1:-1] != new_version:
                            if len(current_version) < 17:
                                print(f'{color.blue(module_name)} form {color.grey(current_version[1:-1])} to {color.blue(new_version)}')
                                module_change_list[module_name] = new_version
                                package_lines[i] = line.replace(f'{current_version[1:-1]}', f'{new_version}')
                            else: 
                                continue    
                            module_changes = True
                            break
                            
        for service_name, new_version in service_list.items():
            for i, line in enumerate(docker_lines):
                if f'{service_name}:' in line and 'image:' in line:
                    current_version = line.split(':')[-1].strip()
                    if current_version != new_version:
                        print(f'update {color.grey(service_name)} from {color.grey(current_version)} to {color.green(new_version)}')
                        docker_lines[i] = line.replace(current_version, new_version)
                        service_changes = True
                        if service_name == 'api-gateway':
                            continue
                        else:
                            break

        if module_changes:
            if server_indicator != 'video-server':
                try:
                    with open(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json', 'w', encoding='utf-8') as file:
                        file.writelines(package_lines)
                except Exception as err:
                    print(f'writing package.json error: {color.red(err)}')
            else:
                print(color.yellow('module list is up to date'))

        if service_changes:    
            try:
                with open(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', 'w', encoding='utf-8') as file:
                    file.writelines(docker_lines)
                self.terminal('green','done')
            except Exception as err:
                print(f'writing docker-compose.yml error: {color.red(err)}')
        else:
            print(color.yellow('docker-compose is up to date')) 
            
        if module_changes or service_changes:
            answer = input(f'обновить версии на {self.ip}? (y/n): ')
            if answer == 'y':
                print(color.yellow('[IN PROGRESS]'))
                if service_changes:
                    sftp_client.put(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml', f'/home/user/docker-compose.yml')
                    print('copying docker-compose.yml to server')
                    sleep(1)
                    stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/docker-compose.yml {self.config('back_dir')}')
                    sleep(1)
                    try:
                        stdin.write(self.config('password')+'\n')
                        stdin.flush()
                        print(stderr.read().decode())
                    except:
                        next
                    sleep(1)

               

                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.config('back_dir')}; docker-compose up -d')
                    print('updating docker-compose')
                    print(stdout.read().decode())
                    print(stderr.read().decode())
                    stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose ps')
                    status = stdout.read().decode()    
                    for line in status.split('\n'):
                        if 'Exit' in line or "Restarting" in line:
                            module_name = line.split()[0]
                            print(f'{module_name} остановлен')
                            try:
                                print(f'restarting {module_name}')
                                stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose restart {module_name}')
                                status = stderr.read().decode()
                            except:
                                print(f'can not restart docker-compose')
                            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose ps')
                            status = stdout.read().decode()
                            for line in status.split('\n'):
                                if 'Exit' in line:
                                    module_name = line.split()[0]
                                    print(f'{module_name} проблема запуска')
                    
                    print('docker-compose is UP and updated')             
                    ssh.exec_command(f'rm /home/user/docker-compose.yml')
                    print('deleting temp files')
                    try:
                        os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
                    except Exception as err:
                        print(f'delete local temp file error {err}')
                        pass

                if module_changes:
                    if server_indicator != 'video-server':
                        sftp_client.put(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json', f'/home/user/package.json')
                        print('copying package.json to server')
                        sleep(1)
                        stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/package.json {self.config('back_dir')}{self.config('registry_dir')}/origin/')
                        sleep(1)
                        try:
                            stdin.write(self.config('password')+'\n')
                            stdin.flush()
                            print(stderr.read().decode())
                        except:
                            next
                        sleep(1)                     
                        if len(module_change_list) > 0:
                            print('updating module list')
                            print('stop node-manager >')
                            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose stop node-manager')
                            sleep(2)
                            print(stdout.read().decode())
                            print(stderr.read().decode())
                            for module_name, new_version in module_change_list.items():
                                if os.path.exists(f'D:/work/WHPython/stilsoft/lib/{module_name}/{new_version}/lib{module_name}.so'):
                                    try:
                                        self.push_lib_target(self.ip, module_name, new_version)
                                    except Exception as err:
                                        print(f'update {module_name} {new_version} error {err}')
                                else:
                                    print(f'{color.red("ERROR: ")}библиотека {color.grey(module_name)} {color.grey(new_version)} отсутствует в локальном репозитории')
                            print('restart node-manager >')
                            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose restart node-manager')
                            sleep(2)
                            print(stdout.read().decode())
                            print(stderr.read().decode())
                self.terminal('green','done')
                try:
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json')
                except Exception as err:
                    print(f'deleting local temp file error {err}')
                    pass    

            else:
                try:
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/backup/{timestamp}_{log_pref}_docker-compose.yml')
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/compose/{log_pref}_docker-compose.yml')
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/package/backup/{timestamp}_{log_pref}_package.json')
                    os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/package/{log_pref}_package.json')
                except Exception as err:
                    print(f'delete local temp files error {err}')
                    pass
                self.terminal('yellow','done')






    def docker_chech(self):
        import paramiko, json
        #https://core.telegram.org/bots/api#making-requests
        #Checker_state_stil_bot
        #8106710833:AAHD-nZHCeFopceKkFPjJ6u04i77TblyFmA

        from datetime import datetime
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        print('\033[90mdocker_chech() \033[5;33m[START]\033[0m')
        print('> init check versions by logs')
        print(f'connected {self.ip}')
        drop_count = 0
        d_modules_list=[]

        while True:
            if drop_count >=20:
                break
            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose ps')
            status = stdout.read().decode()


            for line in status.split('\n'):
                if 'Exit' in line:
                    exit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    module_name = line.split()[0]
                    if module_name not in d_modules_list:
                        d_modules_list.append(module_name)
                        off_status = f'Модуль {module_name} остановлен в {exit_time}\n'
                        print(off_status)
                        drop_count += 1
                        with open('D:/work/WHPython/stilsoft/ssku/remote/docker_status.txt', 'a') as file:
                            file.write(off_status)
                elif 'Up' in line:
                    module_name = line.split()[0]
                    if module_name in d_modules_list:
                        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        d_modules_list.remove(module_name)
                        on_status = f'Модуль {module_name} запущен в {start_time}\n'
                        print(on_status)
                        with open('D:/work/WHPython/stilsoft/ssku/remote/docker_status.txt', 'a') as file:
                            file.write(on_status)


    def docker_restart(self,service):
        import paramiko
        from color import color
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        print('\033[90mdocker_restart \033[5;33m[START]\033[0m')
        print(f'> init docker_restart [{service}]')
        print(f'connected {self.ip}')
        stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose restart {service}')
        status = stdout.read().decode()    
        #print(status) 
        print(stdout.read())
        print(f'{color.grey('docker_restart')} {self.terminal('green','done')}') 


    def docker_logs(self, write_time=60, cores=48):
        from color import color
        from statistics import median
        import paramiko, os, sys
        from time import sleep
        from datetime import datetime
        def cls():
            sys.stdout.write('\r' + ' ' * 100 + '\r')
            sys.stdout.flush()        
        log_pref = str(self.ip).strip().split('.')[-1]
        #postfix = input(f'POSTFIX{prefix}= ')        
        cls()
        sys.stdout.write(f'{color.grey(' docker_logs')} [{self.ip}] [cores: {cores}] [{write_time} sec] [{color.yellow('start')}]\r')
        sys.stdout.flush()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        #print(f'Подключено к {self.ip}\nwrite docker stats logs > ',end='')
        sleep(0.5)
        ssh.exec_command(f'docker stats > /home/user/docker.txt')
        for timer in range(write_time, -1, -1):
            cls()
            sys.stdout.write(f"{color.grey(' docker_logs')} [{self.ip}] [cores: {cores}] [{timer} sec] [{color.yellow('recording logs')}]\r")
            sys.stdout.flush()
            sleep(1)
        sleep(1)        
        #sleep(write_time)
        ssh.exec_command("\x03")
        cls()
        sys.stdout.write(f"{color.grey(' docker_logs')} [{self.ip}] [cores: {cores}] [{color.grey(write_time)} sec] [{color.yellow('processing logs')}]\r")
        sys.stdout.flush()        
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        sftp_client = ssh.open_sftp()
        sftp_client.get('/home/user/docker.txt', f'D:/work/logs/{log_pref}_docker.txt')
        sftp_client.remove('/home/user/docker.txt')
        sftp_client.close()
        ssh.close()
        service_list = []
        with open('D:/work/WHPython/stilsoft/ssku/remote/perf.ini','r') as file:
            file_ = file.read()
            for line in file_.split('\n'):
                service_list.append(line)
                print(f'DEBUG: service list: {service_list}')

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
                            print(f'collect {service} cpu: [{self.RED}FAILED{self.NON}]')
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
                            print(f'collect {service} mem: [{color.red("FAILED")}]')
                            next
                cls()
                sys.stdout.write(f"{color.grey(' docker_logs')} [{self.ip}] [cores: {cores}] [{color.grey(write_time)} sec] [{color.yellow('processing logs')}]\r")
                sys.stdout.flush()
                with open(f'D:/work/logs/{timestamp}_{log_pref}_DOCKER_LOG.txt', 'a') as file:
                    
                    file.write(f'{'='*37}\n')

                    if need_timer:
                        file.write(f'{timestamp} {self.ip}\n')
                        #file.write(f'{prefix}={postfix}')
                    file.write(f'{service}\n')    
                    file.write(f'{' '*12}CPU (%){' '*8}MEM\n')
                    try:
                        file.write(f'ПИКОВОЕ      {round(max(cpu_list),2)}    |    {round(max(mem_list),2)} {mem_liter}\n')
                    except:
                        file.write('ПИКОВОЕ - ОШИБКА\n')
                        next    
                    try:                     
                        file.write(f'МЕДИАННОЕ    {round(median(cpu_list),2)}    |    {round(median(mem_list),2)} {mem_liter}\n')
                    except:
                        file.write('МЕДИАННОЕ - ОШИБКА\n')                    
                    try:
                        file.write(f'МИНИМАЛЬНОЕ   {round(min(cpu_list), 2)}    |    {round(min(mem_list), 2)} {mem_liter}\n')
                    except:    
                        file.write('МИНИМАЛЬНОЕ - ОШИБКА\n')
                        next
                        
                    if need_timer:
                        cls()
                        sys.stdout.write(f"{color.grey(' docker_logs')} [{self.ip}] [cores: {cores}] [{color.grey(write_time)} sec] [{color.green('done')}]\n")
                        sys.stdout.flush()
                        print('\n')
                        print(f'{timestamp} {self.ip}\n')
                        #print(f'{prefix}={postfix}')
                    else:
                        cls()
                        sys.stdout.flush()    
                    print(f'{service}\n')
                     
                    print(f'{' '*12}CPU (%){' '*8}MEM\n')
                    try:
                        print(f'ПИКОВОЕ      {round(max(cpu_list),2)}    |    {round(max(mem_list),2)} {mem_liter}\n')
                    except:                        
                        print(f'ПИКОВОЕ - {color.red('ОШИБКА')}\n')
                        next    
                    try:                     
                        print(f'МЕДИАННОЕ    {round(median(cpu_list),2)}    |    {round(median(mem_list),2)} {mem_liter}\n')
                    except:                   
                        print(f'МЕДИАННОЕ - {color.red('ОШИБКА')}\n')                   
                    try:
                        print(f'МИНИМАЛЬНОЕ   {round(min(cpu_list), 2)}    |    {round(min(mem_list), 2)} {mem_liter}\n')
                    except:       
                        print(f'МИНИМАЛЬНОЕ - {color.red('ОШИБКА')}\n')
                        next                           
                    need_timer = False
                    print(f'\n{'='*37}\n')   
        os.remove(f'D:/work/logs/{log_pref}_docker.txt')




    def atop_net_logs(self, write_time=15, param='eth0'):
        from statistics import median
        import paramiko, os
        from time import sleep
        from datetime import datetime 
        log_pref = str(self.ip).strip().split('.')[-1]
        print(f'\033[90matop_logs(\033[0m{self.ip}\033[90m) \033[5;33m[START]\033[0m')
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        print(f'write atop logs  > ',end='')
        sleep(0.5)
        stdin, stdout, stderr = ssh.exec_command('which atop')
        installed = stdout.read().decode().strip()
        if not installed:
            print(f'\033[31m[atop НЕ УСТАНОВЛЕН]\033[0m на {self.ip}')
            sleep(1)
            exit()

        ssh.exec_command(f'atop -w /home/user/atop.txt 1 {write_time}')
        sleep(write_time+1)
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        ssh.exec_command(f'atop -r /home/user/atop.txt | grep {param} > /home/user/log.txt')
        sleep(1)
        self.terminal('non','done')
        sftp_client = ssh.open_sftp()
        sftp_client.get('/home/user/log.txt', f'D:/work/logs/{log_pref}_atop.txt')  
        sleep(1)
        print('clear temp files > ', end='')
        sftp_client.remove('/home/user/atop.txt')
        sftp_client.remove('/home/user/log.txt') 
        sftp_client.close()
        ssh.close()
        self.terminal('non','done')

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
                    param_1_prechar = item.strip().split()[13]
                    param_2_prechar = item.strip().split()[17]

                    param_1 = item.strip().split()[11]
                    param_1_value = float(item.strip().split()[12])
                    if isinstance(param_1_value, float):
                        if str(param_1_prechar) == 'Mbps':
                            param_1_value = param_1_value * 1000
                        param_1_list.append(param_1_value)


                    param_2 = item.strip().split()[15]
                    param_2_value = float(item.strip().split()[16])
                    if isinstance(param_2_value, float):
                        if str(param_2_prechar) == 'Mbps':
                            param_2_value = param_1_value * 1000
                        param_2_list.append(param_2_value)    

                
                except:
                    print(f'collect {param}: \033[31m[FAILED]\033[0m')
                    next 


            max_param_1 = round(max(param_1_list),2)
            if max_param_1 > 9999:
                max_param_1 = max_param_1 / 1000
                param_1_max_char = 'Mbps'
            else:  
                param_1_max_char = 'Kbps'  

            max_param_2 = round(max(param_2_list),2)
            if max_param_2 > 9999:
                max_param_2 = max_param_2 / 1000
                param_2_max_char = 'Mbps'
            else:  
                param_2_max_char = 'Kbps'                     


            median_param_1 = round(median(param_1_list),2)
            if median_param_1 > 9999:
                median_param_1 = median_param_1 / 1000
                param_1_med_char = 'Mbps'
            else:  
                param_1_med_char = 'Kbps'                 
            
            median_param_2 = round(median(param_2_list),2)
            if median_param_2 > 9999:
                median_param_2 = median_param_2 / 1000
                param_2_med_char = 'Mbps'
            else:  
                param_2_med_char = 'Kbps'                


            min_param_1 = round(min(param_1_list),2)
            if min_param_1 > 9999:
                min_param_1 = min_param_1 / 1000
                param_1_min_char = 'Mbps'
            else:  
                param_1_min_char = 'Kbps'                
            
            min_param_2 = round(min(param_2_list),2)
            if min_param_2 > 9999:
                min_param_2 = min_param_2 / 1000
                param_2_min_char = 'Mbps'
            else:  
                param_2_min_char = 'Kbps'
                

            with open(f'D:/work/logs/{timestamp}_{log_pref}_ATOP_LOG.txt', 'a') as file:
                    
                file.write(f'{'='*36}\n')
                if need_timer:
                    file.write(f'*{timestamp} {self.ip}*\n')
                file.write(f'{finded}\n')    
                
                try:
                    file.write(f'ПИКОВОЕ      {round(max(percent_list),2)}% | {param_1}: {max_param_1} {param_1_max_char}   | {param_2}: {max_param_2} {param_2_max_char} \n')
                except:
                    file.write('ПИКОВОЕ - ОШИБКА\n')
                    next    
                try:                                                                    
                    file.write(f'МЕДИАННОЕ    {round(median(percent_list),2)}% | {param_1}: {median_param_1} {param_1_med_char}   | {param_2}: {median_param_2} {param_2_med_char} \n')
                except:
                    file.write('МЕДИАННОЕ - ОШИБКА\n')                    
                try:                                           
                    file.write(f'МИНИМАЛЬНОЕ   {round(min(percent_list),2)}% | {param_1}: {min_param_1} {param_1_min_char}   | {param_2}: {min_param_2} {param_2_min_char} \n')
                except:    
                    file.write('МИНИМАЛЬНОЕ - ОШИБКА\n')
                    next
                print(f'\n{'='*36}\n')
                if need_timer:
                    print(f'*{timestamp} {self.ip}*\n')
                print(f'{finded}\n')    
                
                try:                                              
                    print(f'ПИКОВОЕ      {round(max(percent_list),2)}% | {param_1}: {max_param_1} {param_1_max_char}   | {param_2}: {max_param_2} {param_2_max_char} \n')
                except:
                    print('ПИКОВОЕ - ОШИБКА\n')
                    next    
                try:                                        
                    print(f'МЕДИАННОЕ    {round(median(percent_list),2)}% | {param_1}: {median_param_1} {param_1_med_char}   | {param_2}: { median_param_2} {param_2_med_char} \n')
                except:
                    print('МЕДИАННОЕ - ОШИБКА\n')
                    next
                try:                   
                    print(f'МИНИМАЛЬНОЕ   {round(min(percent_list),2)}% | {param_1}: {min_param_1} {param_1_min_char}   | {param_2}: {min_param_2} {param_2_min_char} \n')
                except:    
                    print('МИНИМАЛЬНОЕ - ОШИБКА\n')
                    next                       
                need_timer = False      
        os.remove(f'D:/work/logs/{log_pref}_atop.txt')
        from color import color
        #print(f'\033[90matop_logs(\033[0m{self.ip}\033[90m) \033[32m[DONE]\033[0m')
        print(f'{color.grey('atop_logs')} {self.ip} {self.terminal('green','done')}')


    def atop_logs(self, write_time=15, param='md126'):
        from statistics import median
        import paramiko, os, sys
        from time import sleep
        from datetime import datetime 
        from color import color
        def cls():
            sys.stdout.write('\r' + ' ' * 100 + '\r')
            sys.stdout.flush()
        log_pref = str(self.ip).strip().split('.')[-1]
        cls()
        sys.stdout.write(f'{color.grey(' atop_logs')} [{self.ip}] [{param}] [{write_time} sec] [{color.yellow('start')}]\r')
        sys.stdout.flush()
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        #print(f'write atop logs  > ',end='')
        sleep(0.5)
        stdin, stdout, stderr = ssh.exec_command('which atop')
        installed = stdout.read().decode().strip()
        if not installed:
            cls()
            sys.stdout.write(f'{color.grey('atop')} [{color.red('не установлен')}] на {self.ip}')
            sys.stdout.flush()
            sleep(1)
            exit()

        ssh.exec_command(f'atop -w /home/user/atop.txt 1 {write_time}')
        
        for timer in range(write_time, -1, -1):
            cls()
            sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{timer} sec] [{color.yellow('recording logs')}]\r")
            sys.stdout.flush()
            sleep(1)
        sleep(1)
        #sleep(write_time+1)
        cls()
        sys.stdout.write(f"{color.grey('atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.yellow('processing logs')}]\r")
        sys.stdout.flush()
        timestamp = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        ssh.exec_command(f'atop -r /home/user/atop.txt | grep {param} > /home/user/log.txt')
        #print(f'stdout: {stdout.read().decode().strip()}')
        #print(f'stderr: {stderr.read().decode().strip()}')
        sleep(1)
        cls()
        sys.stdout.write(f"{color.grey('atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.green('processing logs')}]\r")
        sys.stdout.flush()
        sftp_client = ssh.open_sftp()
        sftp_client.get('/home/user/log.txt', f'D:/work/logs/{log_pref}_atop.txt')  
        sleep(1)
        sys.stdout.write(f"{color.grey('atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.yellow('clear temp')}]\r")
        sys.stdout.flush()
        sftp_client.remove('/home/user/atop.txt')
        sftp_client.remove('/home/user/log.txt') 
        sftp_client.close()
        ssh.close()
        cls()
        sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.green('clear temp')}]\r")
        sys.stdout.flush()

        need_timer = True
        with open(f'D:/work/logs/{log_pref}_atop.txt','r') as file:
            percent_list = []
            param_1_list = []
            param_2_list = []
            need_find = True
            for item in file:
                try:
                    if need_find:
                        finded = item.strip().split()[2]
                        need_find = False
                    percent = float(item.strip().split()[3].replace('%',''))
                    if isinstance(percent, float):
                        percent_list.append(percent)
                    param_1_prechar = item.strip().split()[13]
                    param_2_prechar = item.strip().split()[17]

                    param_1 = item.strip().split()[11]
                    param_1_value = float(item.strip().split()[12])
                    if isinstance(param_1_value, float):
                        
                        if str(param_1_prechar) == 'Mbps':
                            param_1_value = param_1_value * 1000
                        param_1_list.append(param_1_value)


                    param_2 = item.strip().split()[15]
                    param_2_value = float(item.strip().split()[16])
                    if isinstance(param_2_value, float):
                        if str(param_2_prechar) == 'Mbps':
                            param_2_value = param_2_value * 1000
                        param_2_list.append(param_2_value)   

                
                except:
                    cls()
                    sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.red(f'collect {param}: failed')}]\r")
                    sys.stdout.flush()
                    continue


            max_param_1 = round(max(param_1_list),2)
            if max_param_1 > 9999:
                max_param_1 = max_param_1 / 1000
                param_1_max_char = 'Mbps'
            else:  
                param_1_max_char = 'Kbps'  

            max_param_2 = round(max(param_2_list),2)
            if max_param_2 > 9999:
                max_param_2 = max_param_2 / 1000
                param_2_max_char = 'Mbps'
            else:  
                param_2_max_char = 'Kbps'                     


            median_param_1 = round(median(param_1_list),2)
            if median_param_1 > 9999:
                median_param_1 = median_param_1 / 1000
                param_1_med_char = 'Mbps'
            else:  
                param_1_med_char = 'Kbps'                 
            
            median_param_2 = round(median(param_2_list),2)
            if median_param_2 > 9999:
                median_param_2 = median_param_2 / 1000
                param_2_med_char = 'Mbps'
            else:  
                param_2_med_char = 'Kbps'                


            min_param_1 = round(min(param_1_list),2)
            if min_param_1 > 9999:
                min_param_1 = min_param_1 / 1000
                param_1_min_char = 'Mbps'
            else:  
                param_1_min_char = 'Kbps'                
            
            min_param_2 = round(min(param_2_list),2)
            if min_param_2 > 9999:
                min_param_2 = min_param_2 / 1000
                param_2_min_char = 'Mbps'
            else:  
                param_2_min_char = 'Kbps'
                

            with open(f'D:/work/logs/{timestamp}_{log_pref}_ATOP_LOG.txt', 'a') as file:
                    
                file.write(f'{'='*36}\n')
                if need_timer:
                    file.write(f'*{timestamp} {self.ip}*\n')
                file.write(f'{finded}\n')    
                
                try:
                    file.write(f'ПИКОВОЕ      {round(max(percent_list),2)}% | {param_1}: {max_param_1} {param_1_max_char}   | {param_2}: {max_param_2} {param_2_max_char} \n')
                except:
                    file.write('ПИКОВОЕ - ОШИБКА\n')
                    cls()
                    sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.red('error in max')}]\n")
                    sys.stdout.flush()
                    next    
                try:                                                                    
                    file.write(f'МЕДИАННОЕ    {round(median(percent_list),2)}% | {param_1}: {median_param_1} {param_1_med_char}   | {param_2}: {median_param_2} {param_2_med_char} \n')
                except:
                    file.write('МЕДИАННОЕ - ОШИБКА\n')
                    cls()
                    sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.red('error in median')}]\n")
                    sys.stdout.flush()                    
                try:                                           
                    file.write(f'МИНИМАЛЬНОЕ   {round(min(percent_list),2)}% | {param_1}: {min_param_1} {param_1_min_char}   | {param_2}: {min_param_2} {param_2_min_char} \n')
                except:    
                    file.write('МИНИМАЛЬНОЕ - ОШИБКА\n')
                    cls()
                    sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.red('error in min')}]\n")
                    sys.stdout.flush() 
                    next
                cls()
                sys.stdout.write(f"{color.grey(' atop_logs')} [{self.ip}] [{param}] [{color.grey(write_time)} sec] [{color.green('done')}]\n")
                sys.stdout.flush()
                    
                
                if need_timer:
                    print(f'\n{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n')
                print(f'{finded}\n')    
                
                try:                                              
                    print(f'ПИКОВОЕ      {round(max(percent_list),2)}% | {param_1}: {max_param_1} {param_1_max_char}   | {param_2}: {max_param_2} {param_2_max_char} \n')
                except:
                    print('ПИКОВОЕ - ОШИБКА\n')
                    next    
                try:                                        
                    print(f'МЕДИАННОЕ    {round(median(percent_list),2)}% | {param_1}: {median_param_1} {param_1_med_char}   | {param_2}: { median_param_2} {param_2_med_char} \n')
                except:
                    print('МЕДИАННОЕ - ОШИБКА\n')
                    next
                try:
                    decorline = f'МИНИМАЛЬНОЕ   {round(min(percent_list),2)}% | {param_1}: {min_param_1} {param_1_min_char}   | {param_2}: {min_param_2} {param_2_min_char} \n'                   
                    print(decorline)
                except:    
                    print('МИНИМАЛЬНОЕ - ОШИБКА\n')
                    next                       
                need_timer = False
                print(color.grey(f'\n{'='*int(len(decorline))}\n'))
        os.remove(f'D:/work/logs/{log_pref}_atop.txt')


    def change_ms_view(self, view):
        import paramiko, os
        from color import color
        from time import sleep
        need_to_change = False
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        client = ssh.open_sftp()
        client.get(f'{self.configurate[self.ip]['back_dir']}/.env', f'D:/work/WHPython/stilsoft/ssku/remote/env.txt')
        if view == 'open':
            need_ip = '192.168.207.69'
        elif view == 'close':
            need_ip = '192.168.206.69'
        else:
            print(f'{color.red('ERROR')} view is not correct')        
        with open(f'D:/work/WHPython/stilsoft/ssku/remote/env.txt', 'r') as file:
            env_lines = file.readlines()
        for i, line in enumerate(env_lines):
            if 'MEDIA_SERVER_IP=' in line:
                current_ip = line.split('=')[-1].strip()

                if current_ip != need_ip:
                    if view == 'open':
                        print(f'change media-server view to {color.green('open')}')
                    else:
                        print(f'change media-server view to {color.blue('close')}')
                    env_lines[i] = line.replace(current_ip, need_ip)
                    need_to_change = True
                    break
                else:
                    if view == 'open':
                        print(f'media-server view is already {color.green('open')}')
                    else:
                        print(f'media-server view is already {color.blue('close')}')
                    break
        if need_to_change:
            with open(f'D:/work/WHPython/stilsoft/ssku/remote/env.txt', 'w') as file:
                file.writelines(env_lines)
            try:
                client.put(f'D:/work/WHPython/stilsoft/ssku/remote/env.txt', f'/home/user/env.txt')
            except:
                print(f'{color.red('ERROR')} can not copy env file to server')
            sleep(1)
            try:
                stdin, stdout, stderr = ssh.exec_command(f'sudo -S cp /home/user/env.txt {self.configurate[self.ip]['back_dir']}/.env')
                sleep(1)
                try:
                    stdin.write(f'{self.configurate[self.ip]['password']}\n')
                except:
                    next

            except:
                print(f'{color.red('ERROR')} can not copy env file to backdir')
            sleep(1)
            try:
                stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']}; docker-compose up -d')
                sleep(1)
                print(stdout.read().decode())
                print(stderr.read().decode())
            except:
                print(f'{color.red('ERROR')} can not restart docker-compose')
            try:
                client.remove('/home/user/env.txt')
            except:
                print(f'{color.red('ERROR')} can not remove env file from server')
            try:
                os.remove(f'D:/work/WHPython/stilsoft/ssku/remote/env.txt')
            except:
                print(f'{color.red('ERROR')} can not remove env file from local')
        self.terminal('green','done')
        client.close()
        ssh.close()


    def docker_check_exit(self):
        from datetime import datetime
        import paramiko
        from color import color

        drop_count = 0
        drop_modules_list = []

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ssh.connect(self.ip, port=22, username=self.config('name'), password=self.config('password'))
        self.terminal('non', self.ip)

        while True:
            if drop_count >= 10:
                break
            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[self.ip]['back_dir']} && docker-compose ps')
            status = stdout.read().decode().split('\n')
            
            for line in status:
                if 'Exit' in line:
                    exit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    module_name = line.split()[0]
                    if module_name not in drop_modules_list:
                        drop_modules_list.append(module_name)
                        #off_status = f'модуль {module_name} остановлен в {exit_time}\n'
                        self.terminal('mod', f'модуль {color.grey(module_name)} {color.red('остановлен')} в {exit_time}')
                        drop_count+=1
                elif 'Restarting' in line:
                    restarting_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    module_name = line.split()[0]
                    if module_name not in drop_modules_list:
                        drop_modules_list.append(module_name)
                        #off_status = f'модуль {module_name} остановлен (restarting) в {restarting_time}\n'
                        self.terminal('mod', f'модуль {color.grey(module_name)} {color.yellow('остановлен (restarting)')} в {restarting_time}')
                        drop_count+=1

                elif 'Up' in line:
                    module_name = line.split()[0]
                    if module_name in drop_modules_list:
                        start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                        drop_modules_list.remove(module_name)
                        on_status = f'Модуль {module_name} запущен в {start_time}\n'
                        self.terminal('mod', f'модуль {color.grey(module_name)} {color.green('запущен')} в {start_time}')


    def mtx_check_rtp(self):
        import sys
        from datetime import datetime
        sys.path.append('D:\work\WHPython\stilsoft')
        from ssku.db import DbSsku
        import paramiko
        from color import color

        drop_count = 0

        main_list = {}
        alt_list = {}
        

        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy)
        ip = self.video_partner[self.ip]
        
        ssh.connect(ip, port=22, username=self.configurate[ip]['name'], password=self.configurate[ip]['password'])
        self.terminal('non', self.ip)

        while True:
            if drop_count >= 1:
                break
            stdin, stdout, stderr = ssh.exec_command(f'cd {self.configurate[ip]['back_dir']} && docker-compose logs --tail 1000 mediamtx-server')
            status = stdout.read().decode().split('\n')
            for line in status:

                if 'RTP packets lost' in line:
                    #start_time = line.split()[3]
                    #print(f'{color.green(start_time)}')
                    module_trash_id = line.split()[6]
                    if '0001' in module_trash_id:
                        module_id = line.split()[6].strip('-0002]')
                        module_value = int(line.split()[9])
                        if module_id not in main_list:
                            main_list[module_id] = [module_value]
                        else:    
                            main_list[module_id].append(module_value)
                    elif '0002' in module_trash_id:
                        module_id = line.split()[6].strip('-0001]')
                        module_value = int(line.split()[9])
                        if module_id not in alt_list:
                            alt_list[module_id] = [module_value]
                        else:    
                            alt_list[module_id].append(module_value)
                drop_count+=1                                   

   
                
        for k in range(len(main_list:))
            module_id = main_list[k].strip('-0001]').strip('-0002]')
            module_name = DbSsku(self.ip).get_module_name_by_id(module_id)
            

        

                #module_id = line.split()[6].strip('-0001]').strip('-0002]')
                #module_name = DbSsku(self.ip).get_module_name_by_id(module_id)
 
                    





