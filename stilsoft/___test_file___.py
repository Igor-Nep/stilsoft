import json
import msgpack
import datetime
import os

smp_data =[{
    'name':'John',
    'age': 30,
    'cars':[
        {'model':'2110'},
        {'model':'2107'}
    ],
} for _ in range(10000)]

now = datetime.datetime.now()
with open('sample.json', 'w') as f:
    json.dump(smp_data, f)
print('json', datetime.datetime.now() - now)    
 

now = datetime.datetime.now()
with open('sample.msgpack', 'wb') as f:
    msgpack.dump(smp_data, f)
print('msgpack', datetime.datetime.now() - now)    

print('json', os.path.getsize('sample.json')/1024/1024)
print('msgpack', os.path.getsize('sample.msgpack')/1024/1024)


#now = datetime.datetime.now()
#with open('sample.msgpack', 'rb') as f:
#    msgpack.unpack(f)
#print('msgpack', datetime.datetime.now() - now) 
df  =msgpack.packb(smp_data)
print(df)