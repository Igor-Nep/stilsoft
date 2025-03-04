# -*- coding: utf-8 -*-
from datetime import datetime
import subprocess

drop_count = 0
d_modules_list=[]

while True:
	if drop_count >=20:
		break
	status = subprocess.run('cd /opt/murom/origin/backend && docker-compose ps', shell=True, capture_output=True, text=True)

	for line in status.stdout.split('\n'):
		if 'Exit' in line:
			exit_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			module_name = line.split()[0]
			if module_name not in d_modules_list:
				d_modules_list.append(module_name)
				off_status = f'Модуль {module_name} остановлен в {exit_time}\n'
				print(off_status)
				drop_count += 1
				with open('/home/user/docker_status.txt', 'a') as file:
					file.write(off_status)
		elif 'Up' in line:
			module_name = line.split()[0]
			if module_name in d_modules_list:
				start_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
				d_modules_list.remove(module_name)
				on_status = f'Модуль {module_name} запущен в {start_time}\n'
				print(on_status)
				with open('/home/user/docker_status.txt', 'a') as file:
					file.write(on_status)
