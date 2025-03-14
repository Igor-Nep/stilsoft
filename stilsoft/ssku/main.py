from db import DbSsku
from api import ApiSsku
from postman import Postman
from remote import Remote
import requests, warnings

#Postman().get('/api/data/system/module')
#ApiSsku().needed_notifications()
#DbSsku('192.168.202.10').archive_and_del_all_modules()
#archived_all_modules()
#reset_archived_modules()
#DbSsku('192.168.202.10').change_password('armdo1','armdo1')
#Remote('192.168.202.30').push_lib('libsdp881')
Remote('192.168.202.10').check_versions()

