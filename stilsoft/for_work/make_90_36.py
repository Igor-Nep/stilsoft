with open('D:/work/WHPython/mediamtx_9036_nep.yml', 'w') as file:
    file.write('logLevel: info\n')
    file.write('rtspAddress: :8554\n')
    file.write('\n')
    file.write('paths:\n')
    for i in range(1,90):
        file.write(f"  '{i}':\n")
        file.write('    runOnInit: >-\n')
        file.write('      ffmpeg -stream_loop -1 -re -fflags +genpts\n')
        file.write('      -i /home/user/2korng/22.avi\n')
        file.write('      -c copy\n')
        file.write('      -map 0:v\n')
        file.write('      -f rtsp\n')
        file.write('      -rtsp_transport tcp\n')
        file.write(f'      rtsp://localhost:$RTSP_PORT/{i}\n')
        file.write('    runOnInitRestart: yes\n')
        file.write('\n')
with open('D:/work/WHPython/mediamtx_9036_nep.yml', 'a') as file:
    for i in range(1,36):    
        file.write(f"  '{i}_sub':\n")
        file.write('    runOnInit: >-\n')
        file.write('      ffmpeg -stream_loop -1 -re -fflags +genpts\n')
        file.write('      -i /home/user/2korng/sub/nep_sub.mp4\n')
        file.write('      -c copy\n')
        file.write('      -map 0:v\n')
        file.write('      -f rtsp\n')
        file.write('      -rtsp_transport tcp\n')
        file.write(f'      rtsp://localhost:$RTSP_PORT/{i}_sub\n')
        file.write('    runOnInitRestart: yes\n')
        file.write('\n')