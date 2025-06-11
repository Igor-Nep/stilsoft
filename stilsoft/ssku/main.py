from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote

#Remote('192.168.202.221').hosts_check()
'''камеры на vs90'''
#DbSsku('192.168.202.221').archive_and_del_all_modules(file='kill_before_a5000_06.06')
#DbSsku('192.168.202.221').archive_and_del_needed_modules(from_n=10060, to_n=10089, file_name='reserved_a5000_for60.txt')
#DbSsku('192.168.202.221').reset_needed_modules(from_n=10000, to_n=10090)
#ApiSsku('192.168.202.221').add_suml('192.168.203.200',0,29)
#ApiSsku('192.168.202.221').add_vs('192.168.202.112',0,29)
#ApiSsku('192.168.202.10').add_link(from_n=0, to_n=29)
#ApiSsku('192.168.202.10').add_link_manual(host='test_sprint', member='Камера 210')
#ApiSsku('192.168.202.221').del_link(from_n=60, to_n=89)
#print(ApiSsku('192.168.202.221').get_module_by_name('Камера 10045'))
#ApiSsku('192.168.202.221').mode_archive("splitInterval","1m")
#ApiSsku('192.168.202.10').mode_archive_by_name(mode="splitInterval",value="1m",name="213-шка")
#ApiSsku('192.168.207.68').add_rtsp(1,15)

#Remote('192.168.202.221').docker_restart('archive-manager')
#ApiSsku('192.168.202.221').change_ip('192.168.203.200')

'''смена типа арм старый/новый'''
#DbSsku('192.168.202.221').change_arm_type('new')

'''нагрузка atop и docker stats'''
#Remote('192.168.207.69').docker_logs(write_time=300,cores=40)
#Remote('192.168.207.69').atop_logs(write_time=40, param='eth0')
#Remote('192.168.207.69').atop_logs(write_time=40, param='eth1')
#Remote('192.168.202.221').atop_logs(write_time=20, param='eth0')
##Remote('192.168.202.221').atop_logs(write_time=20, param='eth1')
#Remote('192.168.202.221').atop_logs(write_time=20, param='bond0')
#Remote('192.168.207.69').docker_check_exit()
#Remote('192.168.207.68').mtx_check_rtp()

'''postman'''
#Postman().get('/api/data/security/user')
#Postman().post('/api/events/incident')
#Postman().delete('/api/data/system/zone/')

'''сверка версий'''
Remote('192.168.202.129').update_versions()
#Remote('192.168.202.10').check_versions('ssku')
#Remote('192.168.207.69').change_versions_modules('ssku')
#self.push_lib_target(ip, module_name, new_version)
#Remote('192.168.202.126').push_lib_targeting('192.168.202.126','sdp858i','1.2.10') 

#ApiSsku('192.168.207.68').enable_module(module_name='Камера 101',enabled=False)
#ApiSsku('192.168.202.126').check_module_state(module_name='Этаж 3. Вход')


'''добавление камер'''
#ApiSsku('192.168.207.68').add_module_by_json()

'''создание инцидентов'''
#ApiSsku('192.168.207.68').post_incident()

'''обновление модулей'''
#Remote('192.168.207.68').push_pack('sdp858i')
#Remote('192.168.202.9').push_lib('libobjectdetector')

#Postman().get('api/data/system/module')

'''переключение стримов'''
#Remote('192.168.207.69').change_ms_view('open')

#ApiSsku('192.168.207.68').postman()
#print(ApiSsku('192.168.202.221').check_module_state('Камера 10039'))
#ApiSsku('192.168.207.68').get_sub_zones('/api/data/system/zone') #найти ОО с вложенными зонами

#print(ApiSsku('192.168.207.68').get_node('video'))
#ApiSsku('192.168.202.221').mode_archive("mode","write")
#ApiSsku('192.168.202.221').mode_settings('useMediamtx', False)
#DbSsku('192.168.202.221').archive_and_del_needed_modules(from_n=10000, to_n=10040, file_name='reserved_221_1404.txt')
#DbSsku('192.168.202.221').reset_archived_modules('kill_221_04_17_1')
#DbSsku('192.168.207.68').get_rows_in_massive('select event_code from events.history')
#print(DbSsku('192.168.202.10').get_user_id_by_login('ivanov'))
#print(DbSsku('192.168.207.68').get_user_hash_by_name('testauth2'))
#archived_all_modules()
#reset_archived_modules()

#DbSsku('192.168.207.68').change_password('testauth','test')

#Remote('192.168.202.10').check_versions_by_manifest('ssku')
#Remote('192.168.207.68').check_versions_by_logs('ssku')


#ApiSsku('192.168.207.68').needed_notifications()

'''мониторинг остановки сервисов'''
#Remote('192.168.207.68').docker_chech()

#Postman().post('/api/events/maping')