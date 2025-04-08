with open('D:/work/WHPython/mediamtx_real_12.yml', 'w') as file:
    file.write('logLevel: info\n')
    file.write('rtspAddress: :8554\n')
    file.write('protocols: [tcp]\n')
    file.write('\n')
    file.write('paths:\n')
    for i in range(90):
        if i <10:
            cam_pref = 1000
        elif  9<i<100:
            cam_pref = 100
        elif  99<i<1000:
            cam_pref = 10
        elif  999<i<10000:
            cam_pref = 1
        file.write(f"  '{i}':\n")
        file.write('    runOnInit: >-\n')
        file.write('      ffmpeg -re -rtsp_transport tcp\n')
        file.write('      -i rtsp://admin:admin@172.16.16.141:554/stream\n')
        file.write('      -c copy\n') 
        file.write('      -f rtsp\n')
        file.write('      -rtsp_transport tcp\n')
        file.write('      -stimeout 5000000\n')
        file.write('      -timeout 5000000\n')
        file.write('      -analyzeduration 10000000\n')
        file.write('      -probesize 10000000\n')
        file.write(f'      rtsp://localhost:8554/{i}\n')
        file.write('    runOnInitRestart: yes\n')
        file.write('\n')
        file.write(f"  '{i}_sub':\n")
        file.write('    runOnInit: >-\n')
        file.write('      ffmpeg -re -rtsp_transport tcp\n')
        file.write('      -i rtsp://admin:admin@172.16.16.141:554/stream\n')
        file.write('      -c copy\n')
        file.write('      -map 0\n')
        file.write('      -f rtsp\n')
        file.write('      -rtsp_transport tcp\n')
        file.write('      -stimeout 5000000\n')
        file.write('      -timeout 5000000\n')
        file.write('      -analyzeduration 10000000\n')
        file.write('      -probesize 10000000\n')
        file.write(f'      rtsp://localhost:8554/{i}\n')
        file.write('    runOnInitRestart: yes\n')
        file.write('\n')