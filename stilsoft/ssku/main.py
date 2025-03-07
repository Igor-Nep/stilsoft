from db import DbSsku
from api import ApiSsku
from remote import Remote

#ApiSsku().add_module_by_json()
#DbSsku('192.168.202.10').archive_and_del_all_modules()
#archived_all_modules()
#reset_archived_modules()
#change_password('armdo1','armdo')
#Remote('192.168.202.10').push_pack('mbeg-plus')
Remote('192.168.202.10').check_versions()