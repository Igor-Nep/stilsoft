from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote
import requests, warnings


#ApiSsku().get_sub_zones('/api/data/system/zone')
ApiSsku('192.168.202.221').add_suml('10.207.0.4',38,44)
#ApiSsku('192.168.207.68').change_ip('10.207.0.4')
#print(ApiSsku().get_node('video'))
#ApiSsku().mode_archive('write')
#ApiSsku('192.168.202.221').mode_settings('useMediamtx', True)
#DbSsku('192.168.202.221').archive_and_del_all_modules(file='kill221_04_2')
#DbSsku('192.168.202.221').archive_and_del_needed_modules(from_n=10000, to_n=10078, file_name='reserved_221.txt')
#DbSsku('192.168.202.221').reset_archived_modules('kill_2021_90more')
#DbSsku('192.168.202.10').get_rows_in_massive('select event_code from events.history')
#print(DbSsku('192.168.202.10').get_user_id_by_login('ivanov'))
#archived_all_modules()
#reset_archived_modules()
#DbSsku('192.168.202.10').change_password('armdo1','armdo1')
#Remote('192.168.207.68').push_pack('sdp858i')
#Remote('192.168.207.68').push_lib('libsdp858i')
#Remote('192.168.202.10').check_versions_by_manifest('ssku')
#Remote('192.168.202.10').check_versions_by_logs('ssku')
#Remote('192.168.202.221').check_versions('ssku')
#Remote('192.168.202.161').change_versions('ssku')
#ApiSsku().needed_notifications()
#Remote('192.168.202.10').docker_chech()