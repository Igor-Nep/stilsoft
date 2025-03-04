from statistics import median
import paramiko
from time import sleep
import os
#https://conf.stilsoft.ru/pages/viewpage.action?pageId=254051945


def make_logs(host='192.168.202.9', write_time = 30):
    top_log = 1
    docker_log = 1
    print('make_logs() START')
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, port=22, username='user', password='stilsoft')
    print(f'Подключено к {host}\nmake docker stats logs: ',end='')
    sleep(0.5)
    #if docker_log == 1:
    ssh.exec_command(f'docker stats > /home/user/Desktop/docker.txt')
    sleep(write_time)
    ssh.exec_command("\x03")
    sftp_client = ssh.open_sftp()
    sftp_client.get('/home/user/Desktop/docker.txt', 'C:\work\logs\docker.txt')
    print('DONE \nmake top logs: ',end='')
    sleep(0.5)
    #if top_log == 1:    
    ssh.exec_command(f'top -b > /home/user/Desktop/top.txt')
    sleep(write_time)
    ssh.exec_command("\x03")
    sftp_client = ssh.open_sftp()
    sftp_client.get('/home/user/Desktop/top.txt', 'C:/work/logs/top.txt')
    print('DONE')
    
    print('make_logs() FINISHED')
    

def check_log_docker(cores = 32):
    all_cont = 1
    archive = 1
    media = 1
    node = 1
    webrtc = 1
    signal = 1
    autoheal = 1
    detector = 1
    cadvisor = 1 
    with open('C:/work/logs/docker.txt') as file:
        print('file is open')
        print('check_log_docker()')
        print('START')
                
        list_archive_cpu = []
        list_archive_mem = []

        list_media_cpu = []
        list_media_mem = []
        
        list_node_cpu = []
        list_node_mem = []

        list_webrtc_cpu = []
        list_webrtc_mem = []
        
        list_signal_cpu = []
        list_signal_mem = []

        list_autoheal_cpu = []
        list_autoheal_mem = []

        list_detector_cpu = []
        list_detector_mem = []

        list_cadvisor_cpu = []
        list_cadvisor_mem = []

        docker_data = {}

        print('collect data: ', end='           ')
        for item in file:
            
            if 'archive-manager' in item:
                try:
                    list_archive_cpu.append(float(item[45:55].strip().replace('%',''))/cores)
                except:
                    #print('collect arcive_cpu: FAILED')
                    next    
                 
                try:
                    list_archive_mem.append(float(item[56:64].strip().replace('G','').replace('M','')))
                    archive_mem_liter = item[62:64]
                    change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                    for i in change_list:
                        archive_mem_liter = archive_mem_liter.replace(i, '')
                except:
                    #print('collect arcive_mem: FAILED')
                    next    

            elif 'node-manager' in item:
                try:
                    list_node_cpu.append(float(item[45:55].strip().replace('%',''))/cores)
                except:
                    print('collect node_cpu: FAILED')
                    next    
                 
                try:
                    list_node_mem.append(float(item[56:64].strip().replace('G','').replace('M','')))
                    node_mem_liter = item[62:64]
                    change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                    for i in change_list:
                        node_mem_liter = node_mem_liter.replace(i, '')
                except:
                    #print('collect node_mem: FAILED')
                    next    
                    
                             
            elif 'media-server' in item:
                try:
                    list_media_cpu.append(float(item[43:55].strip().replace('%',''))/cores)
                except:
                    #print('collect media_cpu: FAILED')
                    next    
                try:
                    list_media_mem.append(float(item[58:64].strip().replace('G','').replace('M','')))
                    media_mem_liter = item[62:64]
                    change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                    for i in change_list:
                        media_mem_liter = media_mem_liter.replace(i, '')
                except:
                    #print('collect media_mem: FAILED')
                    next
                        

            elif 'webrtc' in item:
                try:
                    list_webrtc_cpu.append(float(item[43:55].strip().replace('%',''))/cores)
                except:
                    #print('collect webrtc_cpu: FAILED')
                    next    
                try:
                    list_webrtc_mem.append(float(item[58:64].strip().replace('G','').replace('M','').replace('i','')))
                    webrtc_mem_liter = item[62:64]
                    change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                    for i in change_list:
                        webrtc_mem_liter = webrtc_mem_liter.replace(i, '')
                except:
                    #print('collect media_mem: FAILED')
                    next            

            elif 'signalling-server' in item:
                    try:
                        list_signal_cpu.append(float(item[43:55].strip().replace('%',''))/cores)
                    except:
                        #print('collect signal_cpu: FAILED')
                        next    
                    try:
                        list_signal_mem.append(float(item[58:64].strip().replace('G','').replace('M','')))
                        signal_mem_liter = item[62:64]
                        change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                        for i in change_list:
                            signal_mem_liter = signal_mem_liter.replace(i, '')   
                    except:
                        #print('collect signal_mem: FAILED')
                        next

            elif 'detector-api' in item: 
                    try:
                        list_detector_cpu.append(float(item[43:55].strip().replace('%',''))/cores)
                    except:
                        #print('collect detector_cpu: FAILED')
                        next    
                    try:
                        list_detector_mem.append(float(item[58:64].strip().replace('G','').replace('M','')))
                        detector_mem_liter = item[62:64]
                        change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                        for i in change_list:
                            detector_mem_liter = detector_mem_liter.replace(i, '') 
                    except:
                        #print('collect detector_mem: FAILED')
                        next
                
            elif 'autoheal-service' in item: 
                    try:
                        list_autoheal_cpu.append(float(item[43:55].strip().replace('%',''))/cores)
                    except:
                        #print('collect autoheal_cpu: FAILED')
                        next    
                    try:
                        list_autoheal_mem.append(float(item[58:64].strip().replace('G','').replace('M','')))
                        autoheal_mem_liter = item[62:64]
                        change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                        for i in change_list:
                            autoheal_mem_liter = autoheal_mem_liter.replace(i, '')    
                    except:
                        #print('collect autoheal_mem: FAILED')
                        next      

            elif 'cadvisor' in item:
                    try:
                        list_cadvisor_cpu.append(float(item[43:55].strip().replace('%',''))/cores)
                    except:
                        #print('collect cadvisor_cpu: FAILED')
                        next    
                    try:
                        list_cadvisor_mem.append(float(item[58:64].strip().replace('G','').replace('M','')))
                        cadvisor_mem_liter = item[62:64]
                        change_list = ['1','2','3','4','5','6','7','8','9','0','i','B','.',',']
                        for i in change_list:
                            cadvisor_mem_liter = cadvisor_mem_liter.replace(i, '')    
                    except:
                        #print('collect cadvisor_mem: FAILED')
                        next
        #print(archive)
        #if archive == 1:
        
        
        archive_max_cpu = round(max(list_archive_cpu), 2)
        archive_avg_cpu = round(sum(list_archive_cpu) / len(list_archive_cpu), 2)
        archive_median_cpu = round(median(list_archive_cpu), 2)
        archive_max_mem = round(max(list_archive_mem), 2)
        archive_avg_mem = round(sum(list_archive_mem) / len(list_archive_mem), 2)
        archive_median_mem = round(median(list_archive_mem), 2)
        docker_data['a_max_cpu'] = archive_max_cpu
        docker_data['a_avg_cpu'] = archive_avg_cpu
        docker_data['a_med_cpu'] = archive_median_cpu
        docker_data['a_max_mem'] = archive_max_mem
        docker_data['a_avg_mem'] = archive_avg_mem 
        docker_data['a_med_mem'] = archive_median_mem
        docker_data['a_m_l'] = archive_mem_liter

        #elif node == 1:
        node_max_cpu = round(max(list_node_cpu), 2)
        node_avg_cpu = round(sum(list_node_cpu) / len(list_node_cpu), 2)
        node_median_cpu = round(median(list_node_cpu), 2)
        node_max_mem = round(max(list_node_mem), 2)
        node_avg_mem = round(sum(list_node_mem) / len(list_node_mem), 2)
        node_median_mem = round(median(list_node_mem), 2)
        docker_data['n_max_cpu'] = node_max_cpu
        docker_data['n_avg_cpu'] = node_avg_cpu
        docker_data['n_med_cpu'] = node_median_cpu
        docker_data['n_max_mem'] = node_max_mem
        docker_data['n_avg_mem'] = node_avg_mem
        docker_data['n_med_mem'] = node_median_mem
        docker_data['n_m_l'] = node_mem_liter

    #elif media == 1:
        media_max_cpu = round(max(list_media_cpu), 2)
        media_avg_cpu = round(sum(list_media_cpu) / len(list_media_cpu), 2)
        media_median_cpu = round(median(list_media_cpu), 2)
        media_max_mem = round(max(list_media_mem), 2)
        media_avg_mem = round(sum(list_media_mem) / len(list_media_mem), 2)
        media_median_mem = round(median(list_media_mem), 2)
        docker_data['m_max_cpu'] = media_max_cpu
        docker_data['m_avg_cpu'] = media_avg_cpu
        docker_data['m_med_cpu'] = media_median_cpu
        docker_data['m_max_mem'] = media_max_mem
        docker_data['m_avg_mem'] = media_avg_mem
        docker_data['m_med_mem'] = media_median_mem
        docker_data['m_m_l'] = media_mem_liter

    #elif webrtc == 1:
        webrtc_max_cpu = round(max(list_webrtc_cpu), 2)
        webrtc_avg_cpu = round(sum(list_webrtc_cpu) / len(list_webrtc_cpu), 2)
        webrtc_median_cpu = round(median(list_webrtc_cpu), 2)
        webrtc_max_mem = round(max(list_webrtc_mem), 2)
        webrtc_avg_mem = round(sum(list_webrtc_mem) / len(list_webrtc_mem), 2)
        webrtc_median_mem = round(median(list_webrtc_mem), 2)
        docker_data['w_max_cpu'] = webrtc_max_cpu
        docker_data['w_avg_cpu'] = webrtc_avg_cpu
        docker_data['w_med_cpu'] = webrtc_median_cpu
        docker_data['w_max_mem'] = webrtc_max_mem
        docker_data['w_avg_mem'] = webrtc_avg_mem 
        docker_data['w_med_mem'] = webrtc_median_mem
        docker_data['w_m_l'] = webrtc_mem_liter

   # elif signal == 1:
        signal_max_cpu = round(max(list_signal_cpu), 2)
        signal_avg_cpu = round(sum(list_signal_cpu) / len(list_signal_cpu), 2)
        signal_median_cpu = round(median(list_signal_cpu), 2)
        signal_max_mem = round(max(list_signal_mem), 2)
        signal_avg_mem = round(sum(list_signal_mem) / len(list_signal_mem), 2)
        signal_median_mem = round(median(list_signal_mem), 2)
        docker_data['s_max_cpu'] = signal_max_cpu
        docker_data['s_avg_cpu'] = signal_avg_cpu
        docker_data['s_med_cpu'] = signal_median_cpu
        docker_data['s_max_mem'] = signal_max_mem
        docker_data['s_avg_mem'] = signal_avg_mem 
        docker_data['s_med_mem'] = signal_median_mem
        docker_data['s_m_l'] = signal_mem_liter

    #elif detector == 1:
        detector_max_cpu = round(max(list_detector_cpu), 2)
        detector_avg_cpu = round(sum(list_detector_cpu) / len(list_detector_cpu), 2)
        detector_median_cpu = round(median(list_detector_cpu), 2)
        detector_max_mem = round(max(list_detector_mem), 2)
        detector_avg_mem = round(sum(list_detector_mem) / len(list_detector_mem), 2)
        detector_median_mem = round(median(list_detector_mem), 2)
        docker_data['d_max_cpu'] = detector_max_cpu
        docker_data['d_avg_cpu'] = detector_avg_cpu
        docker_data['d_med_cpu'] = detector_median_cpu
        docker_data['d_max_mem'] = detector_max_mem
        docker_data['d_avg_mem'] = detector_avg_mem 
        docker_data['d_med_mem'] = detector_median_mem
        docker_data['d_m_l'] = detector_mem_liter  

    #elif autoheal == 1:
        autoheal_max_cpu = round(max(list_autoheal_cpu), 2)
        autoheal_avg_cpu = round(sum(list_autoheal_cpu) / len(list_autoheal_cpu), 2)
        autoheal_median_cpu = round(median(list_autoheal_cpu), 2)
        autoheal_max_mem = round(max(list_autoheal_mem), 2)
        autoheal_avg_mem = round(sum(list_autoheal_mem) / len(list_autoheal_mem), 2)
        autoheal_median_mem = round(median(list_autoheal_mem), 2)
        docker_data['au_max_cpu'] = autoheal_max_cpu
        docker_data['au_avg_cpu'] = autoheal_avg_cpu
        docker_data['au_med_cpu'] = autoheal_median_cpu
        docker_data['au_max_mem'] = autoheal_max_mem
        docker_data['au_avg_mem'] = autoheal_avg_mem 
        docker_data['au_med_mem'] = autoheal_median_mem
        docker_data['au_m_l'] = autoheal_mem_liter  

    #elif cadvisor == 1:
        cadvisor_max_cpu = round(max(list_cadvisor_cpu), 2)
        cadvisor_avg_cpu = round(sum(list_cadvisor_cpu) / len(list_cadvisor_cpu), 2)
        cadvisor_median_cpu = round(median(list_cadvisor_cpu), 2)
        cadvisor_max_mem = round(max(list_cadvisor_mem), 2)
        cadvisor_avg_mem = round(sum(list_cadvisor_mem) / len(list_cadvisor_mem), 2)
        cadvisor_median_mem = round(median(list_cadvisor_mem), 2)
        docker_data['c_max_cpu'] = cadvisor_max_cpu
        docker_data['c_avg_cpu'] = cadvisor_avg_cpu
        docker_data['c_med_cpu'] = cadvisor_median_cpu
        docker_data['c_max_mem'] = cadvisor_max_mem
        docker_data['c_avg_mem'] = cadvisor_avg_mem 
        docker_data['c_med_mem'] = cadvisor_median_mem
        docker_data['c_m_l'] = cadvisor_mem_liter                         
    
    print('DONE')                    
    print ('FINISHED') 
    return (docker_data)


def check_log_top(cores = 32):
    archive = 0
    media = 1
    node = 0
    

    list_archive_cpu = []
    list_archive_mem = []

    list_media_cpu = []
    list_media_mem = []

    list_node_cpu = []
    list_node_mem = []
        


    print('\ncheck_log_top()')
    print('START')
    with open('C:/work/logs/top.txt') as file:
        print('collect data: ', end='           ')
        for item in file:
            
            if archive == 1:
                if 'archive-man' in item:
                    
                    list_archive_cpu.append(float(item[47:54].strip().replace(',','.'))/cores)
                    list_archive_mem.append(float(item[31:38].strip().replace(',','.').replace('m',''))/1024) #
             
            elif media == 1:
                if 'media-ser' in item:
                    list_media_cpu.append(float(item[47:54].strip().replace(',','.'))/cores)
                    change_list = ['m','g','i','b']
                    pre_item = (item[31:38].strip().replace(',','.'))
                    for i in change_list:
                       pre_item = pre_item.replace(i, '')
                    list_media_mem.append(float(pre_item))#/1024 - определить литеру кроме цифр и раздеоителей в диапазоне захвата, в переменной коэффициент в зависимости от определенной литеры подставлять значения
                    #определить значение лит_мем как аппер найденой литеры
            elif node == 1:  
                if 'node_man' in item:
                    list_node_cpu.append(float(item[47:54].strip().replace(',','.'))/cores)
                    list_node_mem.append(float(item[31:38].strip().replace(',','.').replace('m',''))/1024) 
    print('DONE')

    top_data = {}

    if archive == 1:
        archive_max_cpu = round(max(list_archive_cpu), 2)
        archive_avg_cpu = round(sum(list_archive_cpu) / len(list_archive_cpu), 2)
        archive_median_cpu = round(median(list_archive_cpu), 2)
        archive_max_mem = round(max(list_archive_mem), 2)
        archive_avg_mem = round(sum(list_archive_mem) / len(list_archive_mem), 2)
        archive_median_mem = round(median(list_archive_mem), 2)
        top_data['a_max_cpu'] = archive_max_cpu
        top_data['a_avg_cpu'] = archive_avg_cpu
        top_data['a_med_cpu'] = archive_median_cpu
        top_data['a_max_mem'] = archive_max_mem
        top_data['a_avg_mem'] = archive_avg_mem 
        top_data['a_med_mem'] = archive_median_mem
        
    elif node == 1:
        node_max_cpu = round(max(list_node_cpu), 2)
        node_avg_cpu = round(sum(list_node_cpu) / len(list_node_cpu), 2)
        node_median_cpu = round(median(list_node_cpu), 2)
        node_max_mem = round(max(list_node_mem), 2)
        node_avg_mem = round(sum(list_node_mem) / len(list_node_mem), 2)
        node_median_mem = round(median(list_node_mem), 2)
        top_data['n_max_cpu'] = node_max_cpu
        top_data['n_avg_cpu'] = node_avg_cpu
        top_data['n_med_cpu'] = node_median_cpu
        top_data['n_max_mem'] = node_max_mem
        top_data['n_avg_mem'] = node_avg_mem
        top_data['n_med_mem'] = node_median_mem
     
    elif media == 1:    
        media_max_cpu = round(max(list_media_cpu), 2)
        media_avg_cpu = round(sum(list_media_cpu) / len(list_media_cpu), 2)
        media_median_cpu = round(median(list_media_cpu), 2)
        media_max_mem = round(max(list_media_mem), 2)
        media_avg_mem = round(sum(list_media_mem) / len(list_media_mem), 2)
        media_median_mem = round(median(list_media_mem), 2)
        top_data['m_max_cpu'] = media_max_cpu
        top_data['m_avg_cpu'] = media_avg_cpu
        top_data['m_med_cpu'] = media_median_cpu
        top_data['m_max_mem'] = media_max_mem
        top_data['m_avg_mem'] = media_avg_mem
        top_data['m_med_mem'] = media_median_mem

    
    with open('C:/work/logs/LOG_VIDEO_TOP.txt', 'a') as _file:
            if archive == 1:
                print('write <archive-manager>: ',end='')
                _file.write(f'\n<archive-manager>   пиковое значение CPU: {archive_max_cpu}')
                
                if int(round(float(max(list_archive_cpu)),2)) != 0:
                    _file.write(f'\n<archive-manager>   среднее значение CPU: {archive_avg_cpu}')
                else:
                    _file.write(f'\n<archive-manager>   среднее значение CPU: 0.00')
                if int(round(float(max(list_archive_cpu)),2)) != 0:
                    _file.write(f'\n<archive-manager> медианное значение CPU: {archive_median_cpu}\n')
                else:
                    _file.write(f'\n<archive-manager> медианное значение CPU: 0.00\n')
                _file.write(f'{'_'*52}\n')
                _file.write(f'\n<archive-manager>   пиковое значение MEM: {archive_max_mem} M')
                _file.write(f'\n<archive-manager>   среднее значение MEM: {archive_avg_mem} M')
                _file.write(f'\n<archive-manager> медианное значение MEM: {archive_median_mem} M\n')
                print('DONE')
                _file.write(f'\n{'='*52}\n')

            elif node == 1:    
                print('write <node-manager>: ',end='   ')
                _file.write(f'\n<node manager>      пиковое значение CPU: {node_max_cpu}')
                if int(round(float(max(list_node_cpu)),2)) != 0:
                    _file.write(f'\n<node manager>      среднее значение CPU: {node_avg_cpu}')
                else:
                    _file.write(f'\n<node manager>      среднее значение CPU: 0.00')
                if int(round(float(max(list_node_cpu)),2) )!= 0:        
                    _file.write(f'\n<node manager>    медианное значение CPU: {node_median_cpu}\n')
                else:
                    _file.write(f'\n<node manager>    медианное значение CPU: 0.00\n')    
                _file.write(f'{'_'*52}')
                _file.write(f'\n<node manager>      пиковое значение MEM: {node_max_mem} M')
                _file.write(f'\n<node manager>      среднее значение MEM: {node_avg_mem} M')
                _file.write(f'\n<node manager>    медианное значение MEM: {node_median_mem} M\n')
                print('DONE')
                _file.write(f'\n{'='*52}\n')

            elif media == 1:    
                print('write <media-server>: ',end='   ')
                _file.write(f'\n<media-server>      пиковое значение CPU: {media_max_cpu}')
                if int(round(float(max(list_media_cpu)),2)) != 0:  
                    _file.write(f'\n<media-server>      среднее значение CPU: {media_avg_cpu}')
                else:
                    _file.write(f'\n<media-server>      среднее значение CPU: 0.00')
                if int(round(float(max(list_media_cpu)),2))!= 0:         
                    _file.write(f'\n<media-server>    медианное значение CPU: {media_median_cpu}\n')
                else:
                    _file.write(f'\n<media-server>    медианное значение CPU: 0.00\n')    
                _file.write(f'{'_'*52}\n') 
                _file.write(f'\n<media-server>      пиковое значение MEM: {media_max_mem} M')
                _file.write(f'\n<media-server>      среднее значение MEM: {media_avg_mem} M')
                _file.write(f'\n<media-server>    медианное значение MEM: {media_median_mem} M\n')
                print('DONE')
                _file.write(f'{'*'*52}')
                        
    print ('FINISHED')
    print(list_media_mem)
    return(top_data)


def common_log():
    doc_log = check_log_docker()
    top_log = check_log_top()
    print('common_log() START')
    archive = 0
    media = 1
    node = 0
    
    
    if archive == 1:
        doc_a_max_c = len(str(doc_log['a_max_cpu']))
        doc_a_avg_c = len(str(doc_log['a_avg_cpu']))
        doc_a_med_c = len(str(doc_log['a_med_cpu']))
        doc_a_max_m = len(str(doc_log['a_max_mem']))
        doc_a_avg_m = len(str(doc_log['a_avg_mem']))
        doc_a_med_m = len(str(doc_log['a_med_mem']))
        top_a_max_c = len(str(top_log['a_med_cpu']))
        top_a_avg_c = len(str(top_log['a_avg_cpu']))
        top_a_med_c = len(str(top_log['a_med_cpu']))
    
    elif node == 1:
        doc_n_max_c = len(str(doc_log['n_med_cpu']))
        doc_n_avg_c = len(str(doc_log['n_avg_cpu']))
        doc_n_med_c = len(str(doc_log['n_med_cpu']))
        doc_n_max_m = len(str(doc_log['n_max_mem']))
        doc_n_avg_m = len(str(doc_log['n_avg_mem']))
        doc_n_med_m = len(str(doc_log['n_med_mem']))
        top_n_max_c = len(str(top_log['n_med_cpu']))
        top_n_avg_c = len(str(top_log['n_avg_cpu']))
        top_n_med_c = len(str(top_log['n_med_cpu']))
    
    elif media == 1:
        doc_m_max_c = len(str(doc_log['m_med_cpu']))
        doc_m_avg_c = len(str(doc_log['m_avg_cpu']))
        doc_m_med_c = len(str(doc_log['m_med_cpu']))
        doc_m_max_m = len(str(doc_log['m_max_mem']))
        doc_m_avg_m = len(str(doc_log['m_avg_mem']))
        doc_m_med_m = len(str(doc_log['m_med_mem']))
        top_m_max_c = len(str(top_log['m_med_cpu']))
        top_m_avg_c = len(str(top_log['m_avg_cpu']))
        top_m_med_c = len(str(top_log['m_med_cpu']))

    with open('C:/work/logs/COMMON_LOG.txt', 'a') as file:
        file.write(f'{'='*56}\n')
        file.write(f'{' '*21}CPU (%){' '*15}MEM\n')
        file.write(f'{' '*18}docker |  top{' '*7}docker |  top\n')
        if archive == 1:
            file.write('archive-manager\n')
            file.write(f'ПИКОВОЕ{' '*(17-doc_a_max_c)}{doc_log['a_max_cpu']} | {top_log['a_max_cpu']}{' '*(15-top_a_max_c-doc_a_max_m)}{doc_log['a_max_mem']} {doc_log['a_m_l']} | {top_log['a_max_mem']} M\n')
            file.write(f'СРЕДНЕЕ{' '*(17-doc_a_avg_c)}{doc_log['a_avg_cpu']} | {top_log['a_avg_cpu']}{' '*(15-top_a_avg_c-doc_a_avg_m)}{doc_log['a_avg_mem']} {doc_log['a_m_l']} | {top_log['a_avg_mem']} M\n')
            file.write(f'МЕДИАННОЕ{' '*(15-doc_a_med_c)}{doc_log['a_med_cpu']} | {top_log['a_med_cpu']}{' '*(15-top_a_med_c-doc_a_med_m)}{doc_log['a_med_mem']} {doc_log['a_m_l']} | {top_log['a_med_mem']} M\n')
            file.write(f'{'-'*56}\n')
        elif media == 1:
            file.write('media-server\n')
            file.write(f'ПИКОВОЕ{' '*(17-doc_m_max_c)}{doc_log['m_max_cpu']} | {top_log['m_max_cpu']}{' '*(15-top_m_max_c-doc_m_max_m)}{doc_log['m_max_mem']} {doc_log['m_m_l']} | {top_log['m_max_mem']} M\n')
            file.write(f'СРЕДНЕЕ{' '*(17-doc_m_avg_c)}{doc_log['m_avg_cpu']} | {top_log['m_avg_cpu']}{' '*(15-top_m_avg_c-doc_m_avg_m)}{doc_log['m_avg_mem']} {doc_log['m_m_l']} | {top_log['m_avg_mem']} M\n')
            file.write(f'МЕДИАННОЕ{' '*(15-doc_m_med_c)}{doc_log['m_med_cpu']} | {top_log['m_med_cpu']}{' '*(15-top_m_med_c-doc_m_med_m)}{doc_log['m_med_mem']} {doc_log['m_m_l']} | {top_log['m_med_mem']} M\n')
            file.write(f'{'-'*56}\n')
        elif media == 1:
            file.write('node-manager\n')
            file.write(f'ПИКОВОЕ{' '*(17-doc_n_max_c)}{doc_log['n_max_cpu']} | {top_log['n_max_cpu']}{' '*(15-top_n_max_c-doc_n_max_m)}{doc_log['n_max_mem']} {doc_log['n_m_l']} | {top_log['n_max_mem']} M\n')
            file.write(f'СРЕДНЕЕ{' '*(17-doc_n_avg_c)}{doc_log['n_avg_cpu']} | {top_log['n_avg_cpu']}{' '*(15-top_n_avg_c-doc_n_avg_m)}{doc_log['n_avg_mem']} {doc_log['n_m_l']} | {top_log['n_avg_mem']} M\n')
            file.write(f'МЕДИАННОЕ{' '*(15-doc_n_med_c)}{doc_log['n_med_cpu']} | {top_log['n_med_cpu']}{' '*(15-top_n_med_c-doc_n_med_m)}{doc_log['n_med_mem']} {doc_log['n_m_l']} | {top_log['n_med_mem']} M\n')
            file.write(f'{'-'*56}\n')
    print('common_log() FINISHED')
    #os.remove("C:/work/logs/top.txt")
    #os.remove("C:/work/logs/docker.txt")        


def only_docker_log():
    doc_log = check_log_docker()
    print('only_docker_logs() START')
       
    doc_a_max_c = len(str(doc_log['a_max_cpu']))
    doc_a_avg_c = len(str(doc_log['a_avg_cpu']))
    doc_a_med_c = len(str(doc_log['a_med_cpu']))
    doc_a_max_m = len(str(doc_log['a_max_mem']))
    doc_a_avg_m = len(str(doc_log['a_avg_mem']))
    doc_a_med_m = len(str(doc_log['a_med_mem']))
    
    doc_n_max_c = len(str(doc_log['n_med_cpu']))
    doc_n_avg_c = len(str(doc_log['n_avg_cpu']))
    doc_n_med_c = len(str(doc_log['n_med_cpu']))
    doc_n_max_m = len(str(doc_log['n_max_mem']))
    doc_n_avg_m = len(str(doc_log['n_avg_mem']))
    doc_n_med_m = len(str(doc_log['n_med_mem']))
    
    doc_m_max_c = len(str(doc_log['m_med_cpu']))
    doc_m_avg_c = len(str(doc_log['m_avg_cpu']))
    doc_m_med_c = len(str(doc_log['m_med_cpu']))
    doc_m_max_m = len(str(doc_log['m_max_mem']))
    doc_m_avg_m = len(str(doc_log['m_avg_mem']))
    doc_m_med_m = len(str(doc_log['m_med_mem']))

    doc_w_max_c = len(str(doc_log['w_med_cpu']))
    doc_w_avg_c = len(str(doc_log['w_avg_cpu']))
    doc_w_med_c = len(str(doc_log['w_med_cpu']))
    doc_w_max_m = len(str(doc_log['w_max_mem']))
    doc_w_avg_m = len(str(doc_log['w_avg_mem']))
    doc_w_med_m = len(str(doc_log['w_med_mem']))

    doc_s_max_c = len(str(doc_log['s_med_cpu']))
    doc_s_avg_c = len(str(doc_log['s_avg_cpu']))
    doc_s_med_c = len(str(doc_log['s_med_cpu']))
    doc_s_max_m = len(str(doc_log['s_max_mem']))
    doc_s_avg_m = len(str(doc_log['s_avg_mem']))
    doc_s_med_m = len(str(doc_log['s_med_mem']))

    doc_au_max_c = len(str(doc_log['au_med_cpu']))
    doc_au_avg_c = len(str(doc_log['au_avg_cpu']))
    doc_au_med_c = len(str(doc_log['au_med_cpu']))
    doc_au_max_m = len(str(doc_log['au_max_mem']))
    doc_au_avg_m = len(str(doc_log['au_avg_mem']))
    doc_au_med_m = len(str(doc_log['au_med_mem']))

    doc_d_max_c = len(str(doc_log['d_med_cpu']))
    doc_d_avg_c = len(str(doc_log['d_avg_cpu']))
    doc_d_med_c = len(str(doc_log['d_med_cpu']))
    doc_d_max_m = len(str(doc_log['d_max_mem']))
    doc_d_avg_m = len(str(doc_log['d_avg_mem']))
    doc_d_med_m = len(str(doc_log['d_med_mem']))

    doc_c_max_c = len(str(doc_log['c_med_cpu']))
    doc_c_avg_c = len(str(doc_log['c_avg_cpu']))
    doc_c_med_c = len(str(doc_log['c_med_cpu']))
    doc_c_max_m = len(str(doc_log['c_max_mem']))
    doc_c_avg_m = len(str(doc_log['c_avg_mem']))
    doc_c_med_m = len(str(doc_log['c_med_mem']))
    

        

    with open('C:/work/logs/ONLY_DOCKER_LOG.txt', 'a') as file:
        file.write(f'{'='*56}\n')
        file.write(f'{' '*21}CPU (%){' '*15}MEM\n')
               
        file.write('archive-manager\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_a_max_c)}{doc_log['a_max_cpu']}{' '*(22-doc_a_max_m)}{doc_log['a_max_mem']} {doc_log['a_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_a_avg_c)}{doc_log['a_avg_cpu']}{' '*(22-doc_a_avg_m)}{doc_log['a_avg_mem']} {doc_log['a_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_a_med_c)}{doc_log['a_med_cpu']}{' '*(22-doc_a_med_m)}{doc_log['a_med_mem']} {doc_log['a_m_l']}\n')
        file.write(f'{'-'*56}\n')
        
        file.write('media-server\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_m_max_c)}{doc_log['m_max_cpu']}{' '*(22-doc_m_max_m)}{doc_log['m_max_mem']} {doc_log['m_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_m_avg_c)}{doc_log['m_avg_cpu']}{' '*(22-doc_m_avg_m)}{doc_log['m_avg_mem']} {doc_log['m_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_m_med_c)}{doc_log['m_med_cpu']}{' '*(22-doc_m_med_m)}{doc_log['m_med_mem']} {doc_log['m_m_l']}\n')
        file.write(f'{'-'*56}\n')
       
        file.write('node-manager\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_n_max_c)}{doc_log['n_max_cpu']}{' '*(22-doc_n_max_m)}{doc_log['n_max_mem']} {doc_log['n_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_n_avg_c)}{doc_log['n_avg_cpu']}{' '*(22-doc_n_avg_m)}{doc_log['n_avg_mem']} {doc_log['n_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_n_med_c)}{doc_log['n_med_cpu']}{' '*(22-doc_n_med_m)}{doc_log['n_med_mem']} {doc_log['n_m_l']}\n')
        file.write(f'{'-'*56}\n')

        file.write('webrtc-www\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_w_max_c)}{doc_log['w_max_cpu']}{' '*(22-doc_w_max_m)}{doc_log['w_max_mem']} {doc_log['w_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_w_avg_c)}{doc_log['w_avg_cpu']}{' '*(22-doc_w_avg_m)}{doc_log['w_avg_mem']} {doc_log['w_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_w_med_c)}{doc_log['w_med_cpu']}{' '*(22-doc_w_med_m)}{doc_log['w_med_mem']} {doc_log['w_m_l']}\n')
        file.write(f'{'-'*56}\n')

        file.write('signalling server\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_s_max_c)}{doc_log['s_max_cpu']}{' '*(22-doc_s_max_m)}{doc_log['s_max_mem']} {doc_log['s_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_s_avg_c)}{doc_log['s_avg_cpu']}{' '*(22-doc_s_avg_m)}{doc_log['s_avg_mem']} {doc_log['s_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_s_med_c)}{doc_log['s_med_cpu']}{' '*(22-doc_s_med_m)}{doc_log['s_med_mem']} {doc_log['s_m_l']}\n')
        file.write(f'{'-'*56}\n')

        file.write('autoheal-service\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_au_max_c)}{doc_log['au_max_cpu']}{' '*(22-doc_au_max_m)}{doc_log['au_max_mem']} {doc_log['au_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_au_avg_c)}{doc_log['au_avg_cpu']}{' '*(22-doc_au_avg_m)}{doc_log['au_avg_mem']} {doc_log['au_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_au_med_c)}{doc_log['au_med_cpu']}{' '*(22-doc_au_med_m)}{doc_log['au_med_mem']} {doc_log['au_m_l']}\n')
        file.write(f'{'-'*56}\n')

        file.write('detector-api\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_d_max_c)}{doc_log['d_max_cpu']}{' '*(22-doc_d_max_m)}{doc_log['d_max_mem']} {doc_log['d_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_d_avg_c)}{doc_log['d_avg_cpu']}{' '*(22-doc_d_avg_m)}{doc_log['d_avg_mem']} {doc_log['d_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_d_med_c)}{doc_log['d_med_cpu']}{' '*(22-doc_d_med_m)}{doc_log['d_med_mem']} {doc_log['d_m_l']}\n')
        file.write(f'{'-'*56}\n')

        file.write('cadvisor\n')
        file.write(f'ПИКОВОЕ{' '*(17-doc_c_max_c)}{doc_log['c_max_cpu']}{' '*(22-doc_c_max_m)}{doc_log['c_max_mem']} {doc_log['c_m_l']}\n')
        file.write(f'СРЕДНЕЕ{' '*(17-doc_c_avg_c)}{doc_log['c_avg_cpu']}{' '*(22-doc_c_avg_m)}{doc_log['c_avg_mem']} {doc_log['c_m_l']}\n')
        file.write(f'МЕДИАННОЕ{' '*(15-doc_c_med_c)}{doc_log['c_med_cpu']}{' '*(22-doc_c_med_m)}{doc_log['c_med_mem']} {doc_log['c_m_l']}\n')
        file.write(f'{'-'*56}\n')

    print('only_docker_logs() FINISHED')    
    #os.remove("C:/work/logs/docker.txt") 


make_logs()
common_log()
only_docker_log()
print()