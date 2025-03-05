from db import DbSsku
from api import ApiSsku
from remote import Remote

#ApiSsku().needed_notifications()
#DbSsku('192.168.202.10').archive_and_del_all_modules()
#archived_all_modules()
#reset_archived_modules()
#change_password('armdo1','armdo')
#Remote('192.168.202.238').push_pack('user', 'stilsoft', 'sdp881')
#print(Remote('192.168.202.10').cat('/home/user/rigel/server-app/origin/backend/component-registry/registry/origin', 'package.json'))
Remote('192.168.202.10').check_versions()