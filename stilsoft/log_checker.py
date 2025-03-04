from statistics import median

with open('C:/work/logs/media.txt') as file:

    media_serv = 1
    
    avg_med_cpu = 0.0
    max_med_cpu = 0.0

    avg_med_mem = 0.0
    max_med_mem = 0.0

    avg_arc_cpu = 0.0
    max_arc_cpu = 0.0

    avg_arc_mem = 0.0
    max_arc_mem = 0.0

    avg_nod_cpu = 0.0
    max_nod_cpu = 0.0
    
    avg_nod_mem = 0.0
    max_nod_mem = 0.0

    n_med_cpu = 0
    n_arc_cpu = 0
    n_arc_mem = 0

    n_med_mem = 0
    n_nod_cpu = 0
    n_nod_mem = 0

    med_mem = ''
    arc_mem = ''
    nod_mem = ''
    

    list_archive_cpu= []
    list_archive_mem= []

    list_media_cpu = []
    list_media_mem = []
    
    list_node_cpu = []
    list_node_mem = []

    for item in file:
        if 'archive-manager' in item:
            try:
                inc = float(item[38:42])
                list_archive_cpu.append(inc) 
                avg_arc_cpu += inc
                n_arc_cpu += 1
                if inc >= max_arc_cpu:
                    max_arc_cpu = inc
            except:
                next    
            try:
                inc = float(item[48:52])
                list_archive_mem.append(inc)
                avg_arc_mem += inc
                n_arc_mem += 1
                if inc >= max_arc_mem:
                    max_arc_mem = inc
                arc_mem = item[53]    
            except:
                next    


        elif 'node-manager' in item:
            try:
                inc = float(item[38:42])
                list_node_cpu.append(inc)
                avg_nod_cpu += inc
                n_nod_cpu += 1
                if inc >= max_nod_cpu:
                    max_nod_cpu = inc
            except:
                next    
            try:
                inc = float(item[48:52])
                list_media_mem.append(inc)
                avg_nod_mem += inc
                n_nod_mem += 1
                if inc >= max_nod_mem:
                    max_nod_mem = inc
                cpu_mem = item[53]    
            except:
                next
        
        elif media_serv == 1:
            if 'media-server' in item:
                try:
                    inc = float(item[38:42])
                    list_media_cpu.append(inc)
                    avg_med_cpu += inc
                    n_med_cpu += 1
                    if inc >= max_med_cpu:
                        max_med_cpu = inc
                except:
                    next    
                try:
                    inc = float(item[48:52])
                    list_media_mem.append(inc)
                    avg_med_mem += inc
                    n_med_mem += 1
                    if inc >= max_med_mem:
                        max_med_mem = inc
                    med_mem = item[53]    
                except:
                    next



with open('C:/work/11/14/log_archive.txt', 'a') as _file:
        _file.write(f'\n<archive-manager>  п иковое значение CPU: {max_arc_cpu}')
        _file.write(f'\n<archive-manager>   среднее значение CPU: {round(avg_arc_cpu / n_arc_cpu, 2)}\n')
        _file.write(f'\n<archive-manager>   пиковое значение MEM: {max_arc_mem} {arc_mem}')
        _file.write(f'\n<archive-manager>   среднее значение MEM: {round(avg_arc_mem / n_arc_mem, 2)} {arc_mem}\n')
        _file.write(f'\n<archive-manager> медианное значение CPU: ({median(list_archive_cpu)}\n')
        _file.write(f'\n<archive-manager> медианное значение MEM: ({median(list_archive_mem)}\n')
       
        
        _file.write(f'\n<node manager>      пиковое значение CPU: {max_nod_cpu}')
        _file.write(f'\n<node manager>      среднее значение CPU: {round(avg_nod_cpu / n_nod_cpu, 2)}\n')
        _file.write(f'\n<node manager>      пиковое значение MEM: {max_nod_mem} {cpu_mem}')
        _file.write(f'\n<node manager>      среднее значение MEM: {round(avg_nod_mem / n_nod_mem, 2)} {cpu_mem}\n')
        _file.write(f'\n<node manager>    медианное значение CPU: {median(list_node_cpu)}\n')
        _file.write(f'\n<node manager>    медианное значение MEM: {median(list_node_mem)}\n')

        if media_serv == 1:
             _file.write(f'\n<media-server>    пиковое значение CPU: {max_med_cpu}')
             _file.write(f'\n<media-server>    среднее значение CPU: {round(avg_med_cpu / n_med_cpu, 2)}\n')
             _file.write(f'\n<media-server>    пиковое значение MEM: {max_med_mem} {med_mem}')
             _file.write(f'\n<media-server>    среднее значение MEM: {round(avg_med_mem / n_med_mem, 2)} {med_mem}\n')
             _file.write(f'\n<media-server>    среднее значение CPU: {median(list_media_cpu)}\n')
             _file.write(f'\n<media-server>    среднее значение MEM: {median(list_media_mem)}\n')


        _file.write(f'{'_'*52}')
                     
print ('DONE') 
             


      