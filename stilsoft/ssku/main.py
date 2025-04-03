from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote
import requests, warnings


#ApiSsku().get_sub_zones('/api/data/system/zone')
#Postman().post('/api/data/events/history/list')
ApiSsku().add_suml()
#ApiSsku().mode_archive('write')
#ApiSsku().mode_settings('useMediamtx', True)
DbSsku('192.168.207.68').archive_and_del_all_modules(file='kill_20768')
#DbSsku('192.168.202.10').get_rows_in_massive('select event_code from events.history')
#print(DbSsku('192.168.202.10').get_user_id_by_login('ivanov'))
#archived_all_modules()
#reset_archived_modules()
#DbSsku('192.168.202.10').change_password('armdo1','armdo1')
#Remote('192.168.202.221').push_pack('sdp858i')
#Remote('192.168.202.238').push_lib('libsdp881')
#Remote('192.168.202.10').check_versions_by_manifest('ssku')
#Remote('192.168.202.10').check_versions_by_logs('ssku')
#Remote('192.168.202.10').check_versions('ssku')
#Remote('192.168.202.161').change_versions('ssku')
#ApiSsku().needed_notifications()
#Remote('192.168.202.10').docker_chech()
