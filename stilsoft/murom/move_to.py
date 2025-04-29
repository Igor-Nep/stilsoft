import requests,msgpack
from db import DbMurom
from time import sleep

http_url = 'http://192.168.202.30:8189'
pu_id = DbMurom('192.168.202.30').get_module_id('sdp881')
head = {'Content-type': 'application/x-msgpack'}


#speed = [1.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9]

#pan = [-20 if i % 2 == 0 else 20 for i in range(len(speed))]
#pause = [11, 11, 8, 6, 4, 4, 3, 3, 3, 2]

#hbty
speed = [1.5,1.5,1.8,1.5,0.3,2.1, 0.5,0.5,0.6,0.5,0.2,0.1, 0.5,0.5,0.5,0.6,0.5,0.1,0.7,0.6, 0.4,0.4,0.3,0.1,0.2,0.1]
pan=[10,-5,5,-5,10,-10]
#pan = [-20 if i % 2 == 0 else 20 for i in range(len(speed))]
pause = [3,3,3,3,3,5,2,2,2,2,2,4,2,2,2,2,2,2,2,4,2,2,2,2,2,4]

pan_ = [100.0,200.0]
speed_ = [0.19, 0.19]

for i in range(len(pan)):
    msp = msgpack.packb({"position": {"pan": pan[i]},"velocity": {"pan": speed[i],"tilt": 0.0,"zoom": 0.0,"focus": 0.0}})
    print(str(pan[i])+' '+str(speed[-i]))
    requests.post(http_url+f'/api/modules/{pu_id}/PTZMoveTo', headers=head, data=msp)
    sleep(pause[i])
    