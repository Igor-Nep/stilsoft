import msgpack


with open('C:\work\msgpack\msgp1', "rb") as data_file:
    unpack = msgpack.unpack(data_file)

print(unpack)    