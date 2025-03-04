from db import DbSsku
from api import ApiSsku
from api import ByInputSsku
from remote import Remote
with open("C:\work\WHPython\stilsoft\ssku/config_ssku.json", 'r') as file:
    import json
    file_text = json.load(file)
    print(f"file_text = {file_text}")
    base_url = file_text["base_url"]

#print(ApiSsku(base_url).add_module_by_json())
#DbSsku('192.168.202.10').archive_and_del_all_modules()
#archived_all_modules()
#reset_archived_modules()
#change_password('armdo1','armdo')
#Remote('192.168.202.238').push_lib('user', 'stilsoft', 'libsdp8122')
ApiSsku(base_url).needed_notifications()