with open('D:\work\WHPython\stilsoft\ssku\mediamtx-servers.txt', 'r') as file:
    mtx_lines = file.readlines()
for i, line in enumerate(mtx_lines):
    if 'webrtc: http://' in line:
        print('find webrtc line')
        current_mtx_ip = line.split(':')[-2].strip('//')
        print(f'current ip = {current_mtx_ip}')
        print('start change:')
        mtx_lines[i] = line.replace(current_mtx_ip,'000000')
        print(mtx_lines)
        break
with open('D:/work/WHPython/stilsoft/ssku/mediamtx-servers.txt', 'w') as file:
    file.writelines(mtx_lines)
