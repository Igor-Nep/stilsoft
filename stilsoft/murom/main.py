import sys
sys.path.append("D:\work\WHPython\stilsoft\ssku")
from db import DbMurom
from api import ApiMurom
#from ssku.db import DbSsku
from health import Health


#db = DbMurom('192.168.202.238')
#print(db.get_user_argon_password(db.get_user_id_by_login('newdev')))

#hm = Health('https://gate.synerget.ru:8179').check_pcpu('192.168.202.238',8,3)
ApiMurom().notifications()