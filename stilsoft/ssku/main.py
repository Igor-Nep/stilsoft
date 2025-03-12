from db import DbSsku
from api import ApiSsku
from remote import Remote
import requests, warnings

#ApiSsku().needed_notifications()
#DbSsku('192.168.202.10').archive_and_del_all_modules()
#archived_all_modules()
#reset_archived_modules()
#change_password('armdo1','armdo')
#Remote('192.168.202.10').push_pack('object-detector')
Remote('192.168.207.68').check_versions()
