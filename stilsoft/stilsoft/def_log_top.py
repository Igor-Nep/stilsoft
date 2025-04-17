from statistics import median
def check_log_top():
    list_archive_cpu = []
    list_archive_mem = []

    list_media_cpu = []
    list_media_mem = []

    list_node_cpu = []
    list_node_mem = []
        


    print('start top_log:')
    with open('C:/work/logs/top.txt') as file:
        for item in file:
            if 'archive-manager' in item:
                list_archive_cpu.append(float(item[47:54].strip().replace(',','.')))
                list_archive_mem.append(float(item[31:38].strip().replace(',','.'))/1024)
             
            elif 'media-server' in item:
                list_media_cpu.append(float(item[47:54].strip().replace(',','.')))
                list_media_mem.append(float(item[31:38].strip().replace(',','.'))/1024)

            elif 'node_manager' in item:
                list_node_cpu.append(float(item[47:54].strip().replace(',','.')))
                list_node_mem.append(float(item[31:38].strip().replace(',','.'))/1024) 

    with open('C:/work/logs/LOG_VIDEO_TOP.txt', 'a') as _file:
            
            _file.write(f'\n<archive-manager>   пиковое значение CPU: {round(max(list_archive_cpu), 2)}')
            
            if int(round(float(max(list_archive_cpu)),2)) != 0:
                _file.write(f'\n<archive-manager>   среднее значение CPU: {round(sum(list_archive_cpu) / len(list_archive_cpu), 2)}')
            else:
                 _file.write(f'\n<archive-manager>   среднее значение CPU: 0.00')
            if int(round(float(max(list_archive_cpu)),2)) != 0:
                _file.write(f'\n<archive-manager> медианное значение CPU: {round(median(list_archive_cpu), 2)}\n')
            else:
                 _file.write(f'\n<archive-manager> медианное значение CPU: 0.00\n')
            _file.write(f'{'_'*52}\n')
            _file.write(f'\n<archive-manager>   пиковое значение MEM: {round(max(list_archive_mem), 2)} M')
            _file.write(f'\n<archive-manager>   среднее значение MEM: {round(sum(list_archive_mem) / len(list_archive_mem), 2)} M')
            _file.write(f'\n<archive-manager> медианное значение MEM: {round(median(list_archive_mem), 2)} M\n')
            
            _file.write(f'\n{'='*52}\n')
            
            _file.write(f'\n<node manager>      пиковое значение CPU: {round(max(list_node_cpu), 2)}')
            if int(round(float(max(list_node_cpu)),2)) != 0:
                _file.write(f'\n<node manager>      среднее значение CPU: {round(sum(list_node_cpu) / len(list_node_cpu), 2)}')
            else:
                _file.write(f'\n<node manager>      среднее значение CPU: 0.00')
            if int(round(float(max(list_node_cpu)),2) )!= 0:        
                _file.write(f'\n<node manager>    медианное значение CPU: {round(median(list_node_cpu), 2)}\n')
            else:
                _file.write(f'\n<node manager>    медианное значение CPU: 0.00\n')    
            _file.write(f'{'_'*52}')
            _file.write(f'\n<node manager>      пиковое значение MEM: {round(max(list_node_mem), 2)} M')
            _file.write(f'\n<node manager>      среднее значение MEM: {round(sum(list_node_mem) / len(list_node_mem), 2)} M')
            _file.write(f'\n<node manager>    медианное значение MEM: {round(median(list_node_mem), 2)} M\n')
             
            _file.write(f'\n{'='*52}\n')

            _file.write(f'\n<media-server>      пиковое значение CPU: {round(max(list_media_cpu), 2)}')
            if int(round(float(max(list_media_cpu)),2)) != 0:  
                _file.write(f'\n<media-server>      среднее значение CPU: {round(sum(list_media_cpu) / len(list_media_cpu), 2)}')
            else:
                _file.write(f'\n<media-server>      среднее значение CPU: 0.00')
            if int(round(float(max(list_media_cpu)),2))!= 0:         
                _file.write(f'\n<media-server>    медианное значение CPU: {round(median(list_media_cpu), 2)}\n')
            else:
                _file.write(f'\n<media-server>    медианное значение CPU: 0.00\n')    
            _file.write(f'{'_'*52}\n') 
            _file.write(f'\n<media-server>      пиковое значение MEM: {round(max(list_media_mem), 2)} M')
            _file.write(f'\n<media-server>      среднее значение MEM: {round(sum(list_media_mem) / len(list_media_mem), 2)} M')
            _file.write(f'\n<media-server>    медианное значение MEM: {round(median(list_media_mem), 2)} M\n')

            _file.write(f'{'*'*52}')
                        
    print ('DONE')                        
                
           
                         
check_log_top()                             
