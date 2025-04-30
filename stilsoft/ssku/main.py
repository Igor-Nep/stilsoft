from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote
import requests, warnings

'''камеры на vs90'''
#DbSsku('192.168.202.221').archive_and_del_all_modules(file='kill_221_04_17_1')
#ApiSsku('192.168.202.221').add_suml('192.168.202.201',0,89)
#ApiSsku('192.168.202.221').mode_archive("splitInterval","1m")
#ApiSsku('192.168.202.10').mode_archive_by_name(mode="splitInterval",value="1m",name="213-шка")

#Remote('192.168.202.221').docker_restart('archive-manager')
#ApiSsku('192.168.202.221').change_ip('192.168.203.200')


'''нагрузка atop и docker stats'''
#Remote('192.168.202.221').docker_logs(write_time=20,cores=48)
#Remote('192.168.202.200').atop_logs(write_time=10, param='enp3s0')
#Remote('192.168.202.200').atop_logs(write_time=10, param='enp1s0')
#Remote('192.168.202.221').atop_logs(write_time=20, param='eth0')
##Remote('192.168.202.221').atop_logs(write_time=20, param='eth1')
#Remote('192.168.202.221').atop_logs(write_time=20, param='bond0')


'''сверка версий'''
Remote('192.168.207.68').update_versions('ssku')
#Remote('192.168.207.68').check_versions('ssku')
#Remote('192.168.207.69').change_versions_modules('ssku')

'''обновление модулей'''
#Remote('192.168.207.68').push_pack('sdp858i')
#Remote('192.168.207.69').push_lib('libsdp858i')

#ApiSsku().get_sub_zones('/api/data/system/zone')

#print(ApiSsku('192.168.202.221').get_node('video'))
#ApiSsku('192.168.202.221').mode_archive("mode","write")
#ApiSsku('192.168.202.221').mode_settings('useMediamtx', True)
#DbSsku('192.168.202.221').archive_and_del_needed_modules(from_n=10000, to_n=10040, file_name='reserved_221_1404.txt')
#DbSsku('192.168.202.221').reset_archived_modules('kill_221_04_17_1')
#DbSsku('192.168.202.10').get_rows_in_massive('select event_code from events.history')
#print(DbSsku('192.168.202.10').get_user_id_by_login('ivanov'))
#archived_all_modules()
#reset_archived_modules()

#DbSsku('192.168.202.10').change_password('armdo1','armdo1')

#Remote('192.168.202.10').check_versions_by_manifest('ssku')
#Remote('192.168.207.68').check_versions_by_logs('ssku')

#Remote('192.168.207.68').check_versions('ssku')
#ApiSsku('192.168.202.10').needed_notifications()
#Remote('192.168.202.221').docker_chech()
#Postman().get('/api/data/system/module')
