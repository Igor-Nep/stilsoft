from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote
import requests, warnings

#DbSsku('192.168.202.221').archive_and_del_all_modules(file='kill_221_04_11_1')
#ApiSsku('192.168.207.68').add_suml('192.168.202.200',0,31)
#ApiSsku('192.168.202.221').mode_archive("splitInterval","1m")
#Remote('192.168.202.221').docker_restart('archive-manager')

#Remote('192.168.202.221').docker_logs(write_time=20,cores=48)
Remote('192.168.202.221').atop_logs(write_time=10, param='bond0')
Remote('192.168.202.221').atop_logs(write_time=10, param='eth0')
Remote('192.168.202.221').atop_logs(write_time=10, param='eth1')

#ApiSsku().get_sub_zones('/api/data/system/zone')
#ApiSsku('192.168.202.221').change_ip('10.207.0.4')
#print(ApiSsku('192.168.202.221').get_node('video'))
#ApiSsku('192.168.202.221').mode_archive("mode","write")
#ApiSsku('192.168.202.221').mode_settings('useMediamtx', True)
#DbSsku('192.168.202.221').archive_and_del_needed_modules(from_n=10000, to_n=10078, file_name='reserved_221.txt')
#DbSsku('192.168.202.221').reset_archived_modules('kill_2021_90more')
#DbSsku('192.168.202.10').get_rows_in_massive('select event_code from events.history')
#print(DbSsku('192.168.202.10').get_user_id_by_login('ivanov'))
#archived_all_modules()
#reset_archived_modules()
#DbSsku('192.168.202.10').change_password('armdo1','armdo1')
#Remote('192.168.207.68').push_pack('sdp858i')
#Remote('192.168.202.9').push_lib('libsdp858i')
#Remote('192.168.202.10').check_versions_by_manifest('ssku')
#Remote('192.168.202.10').check_versions_by_logs('ssku')
#Remote('192.168.202.161').change_versions('ssku')
#Remote('192.168.202.221').check_versions('ssku')
#ApiSsku().needed_notifications()
#Remote('192.168.202.221').docker_chech()
#Postman().get('/api/data/system/module')