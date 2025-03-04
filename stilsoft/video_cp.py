from threading import Timer
import shutil
import os
import subprocess

print(os.path.isfile("c:/mc_set")) 
if not os.path.isfile("c:/mc_set"):

    subprocess.call('C:/video_src/ManyCamSetup.exe')
    
    os.system('cls')
    print('Дождитесь установки ManyCam! После определите директории...\n')
    setup_ = input('После завершения установки MnyCam нажмите enter')
    
    inner = input('Введите имя пользователя в системе (например ivanov_i): ')
    outer = input('Директория для резервной копии: ')

    with open('c:/mc_directories', 'a') as file:
        file.write(f'inner={inner}\n')
        file.write(f'outer={outer}')
    with open('c:/mc_set', 'w'):
        pass
else:
    next    

with open('c:/mc_directories', 'r') as file:
    for item in file:
        if 'inner=' in item:
            inner_dir = item[0:5].strip().replace('=','')
        elif 'outer=' in item:
            outer_dir = item[0:5].strip().replace('=','')


def repeater(interval, function):
    Timer(interval, repeater, [interval, function]).start()
    function()

def click_ref():
    shutil.copy(f"C:/Users/{inner_dir}/Videos/ManyCam/My Recording.mp4", outer_dir)
    #shutil.copy(f"{inner}/My Recording.mp4", outer)
    

repeater(5, click_ref)

