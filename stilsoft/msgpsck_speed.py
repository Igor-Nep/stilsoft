import msgpack
import json
import datetime

data = {
    "list_1": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_1": "acbdefghijklmnopqrstuvwxyz",
    "dict_1": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_2": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_2": "acbdefghijklmnopqrstuvwxyz",
    "dict_2": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_3": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_3": "acbdefghijklmnopqrstuvwxyz",
    "dict_3": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_4": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_4": "acbdefghijklmnopqrstuvwxyz",
    "dict_4": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_5": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_5": "acbdefghijklmnopqrstuvwxyz",
    "dict_5": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_6": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_6": "acbdefghijklmnopqrstuvwxyz",
    "dict_6": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_7": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_7": "acbdefghijklmnopqrstuvwxyz",
    "dict_7": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_8": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_8": "acbdefghijklmnopqrstuvwxyz",
    "dict_8": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_9": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_9": "acbdefghijklmnopqrstuvwxyz",
    "dict_9": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_10": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_10": "acbdefghijklmnopqrstuvwxyz",
    "dict_10": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_11": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_11": "acbdefghijklmnopqrstuvwxyz",
    "dict_11": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_12": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_12": "acbdefghijklmnopqrstuvwxyz",
    "dict_12": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_13": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_13": "acbdefghijklmnopqrstuvwxyz",
    "dict_13": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_14": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_14": "acbdefghijklmnopqrstuvwxyz",
    "dict_14": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_15": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_15": "acbdefghijklmnopqrstuvwxyz",
    "dict_15": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_16": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_16": "acbdefghijklmnopqrstuvwxyz",
    "dict_16": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_17": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_17": "acbdefghijklmnopqrstuvwxyz",
    "dict_17": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_18": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_18": "acbdefghijklmnopqrstuvwxyz",
    "dict_18": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_19": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_19": "acbdefghijklmnopqrstuvwxyz",
    "dict_19": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_20": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_20": "acbdefghijklmnopqrstuvwxyz",
    "dict_20": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_21": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_21": "acbdefghijklmnopqrstuvwxyz",
    "dict_21": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_22": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_22": "acbdefghijklmnopqrstuvwxyz",
    "dict_22": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_23": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_23": "acbdefghijklmnopqrstuvwxyz",
    "dict_23": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_24": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_24": "acbdefghijklmnopqrstuvwxyz",
    "dict_24": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_25": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_25": "acbdefghijklmnopqrstuvwxyz",
    "dict_25": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_26": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_26": "acbdefghijklmnopqrstuvwxyz",
    "dict_26": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_27": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_27": "acbdefghijklmnopqrstuvwxyz",
    "dict_27": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_28": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_28": "acbdefghijklmnopqrstuvwxyz",
    "dict_28": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_29": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_29": "acbdefghijklmnopqrstuvwxyz",
    "dict_29": {"pac": "ker", "suck": "my dick", "number": 88},
    "list_30": [1, 2, 3, 4, 5, 6, 7, 8, 9, "abc"],
    "string_30": "acbdefghijklmnopqrstuvwxyz",
    "dict_30": {"pac": "ker", "suck": "my dick", "number": 88},
    }

start_time = datetime.datetime.now()
with open('data.msgpack', 'wb') as file:
    pack_data = msgpack.packb(data)
    file.write(pack_data)
end_time = datetime.datetime.now()
print(f'Конвертация в msgpack и запись в файл\n Время: {end_time-start_time}')

start_time = datetime.datetime.now()
with open('data.json', 'w') as file:
    pack_data = json.dump(data)
    file.write(pack_data)
end_time = datetime.datetime.now()
print(f'Конвертация в json и запись в файл\n Время: {end_time-start_time}')


with open("data.msgpack", "rb") as file:
    byte_data = file.read()
data_loaded = msgpack.unpackb(byte_data)
end_time = datetime.datetime.now()
print(f'Чтение msgpack из файла\n Время: {end_time-start_time}')

with open("data.msgpack", "rb") as file:
    byte_data = file.read()

end_time = datetime.datetime.now()
print(f'Чтение json из файла\n Время: {end_time-start_time}')