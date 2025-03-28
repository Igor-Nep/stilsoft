from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote
import requests, warnings

#Postman().post('/api/data/events/history/list')
#ApiSsku().add_suml()
#ApiSsku().mode_archive('write')
#DbSsku('192.168.202.10').archive_and_del_all_modules()
#archived_all_modules()
#reset_archived_modules()
#DbSsku('192.168.202.10').change_password('armdo1','armdo1')
#Remote('192.168.202.10').push_pack('object-detector')
Remote('192.168.202.238').push_lib('libsdp881')
#Remote('192.168.202.10').check_versions_by_manifest('ssku')
#Remote('192.168.202.10').check_versions_by_logs('ssku')
#Remote('192.168.202.10').check_versions('ssku')
#Remote('192.168.202.161').change_versions('ssku')
#ApiSsku().needed_notifications()