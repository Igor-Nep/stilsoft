
top_log = 1
docker_log = 1

avg_gui_cpu = 0.0
max_gui_cpu = 0.0

avg_med_cpu = 0.0
max_med_cpu = 0.0
d_avg_med_cpu = 0.0
d_max_med_cpu = 0.0

avg_med_mem = 0.0
max_med_mem = 0.0
d_avg_med_mem = 0.0
d_max_med_mem = 0.0

avg_arc_cpu = 0.0
max_arc_cpu = 0.0
d_avg_arc_cpu = 0.0
d_max_arc_cpu = 0.0

avg_arc_mem = 0.0
max_arc_mem = 0.0
d_avg_arc_mem = 0.0
d_max_arc_mem = 0.0

avg_nod_cpu = 0.0
max_nod_cpu = 0.0
d_avg_nod_cpu = 0.0
d_max_nod_cpu = 0.0
    
avg_gui_mem = 0.0
max_gui_mem = 0.0
d_avg_gui_mem = 0.0
d_max_gui_mem = 0.0

avg_nod_mem = 0.0
max_nod_mem = 0.0
d_avg_nod_mem = 0.0
d_max_nod_mem = 0.0

n_med_cpu = 0
n_arc_cpu = 0
n_arc_mem = 0

n_med_mem = 0
n_nod_cpu = 0
n_nod_mem = 0
n_gui_cpu = 0
n_gui_mem = 0

d_n_med_mem = 0
d_n_med_cpu = 0

d_n_arc_cpu = 0
d_n_arc_mem = 0

d_n_nod_cpu = 0
d_n_nod_mem = 0

if top_log == 1:
    print('start top_log:')
    with open('C:/work/logs/top.txt') as file:
      for item in file:
             if 'gunicorn' in item:
               n_gui_cpu += 1
               inc = float(item[47:53].strip().replace(',','.'))
               avg_gui_cpu += inc
               if inc >= max_gui_cpu:
                    max_gui_cpu = inc
               
               n_gui_mem += 1
               inc = float(item[31:38].strip().replace(',','.'))/1024
               avg_gui_mem += inc
               if inc >= max_gui_mem:
                    max_gui_mem = inc
                    
             
             elif 'archive-manager' in item:
               n_arc_cpu += 1
               inc = float(item[47:53].strip().replace(',','.'))
               avg_arc_cpu += inc
               if inc >= max_arc_cpu:
                    max_arc_cpu = inc

               n_arc_mem += 1
               inc = float(item[31:38].strip().replace(',','.'))/1024
               avg_arc_mem += inc
               if inc >= max_arc_mem:
                    max_arc_mem = inc
                         
             elif 'node_manager' in item:
               n_nod_cpu += 1
               inc = float(item[47:53].strip().replace(',','.'))
               avg_nod_cpu += inc
               if inc >= max_nod_cpu:
                    max_nod_cpu = inc

               n_nod_mem += 1
               inc = float(item[31:38].strip().replace(',','.'))/1024
               avg_nod_mem += inc
               if inc >= max_nod_mem:
                    max_nod_mem = inc

             elif 'media-server' in item:
               n_med_cpu += 1
               inc = float(item[47:53].strip().replace(',','.'))
               avg_med_cpu += inc
               if inc >= max_med_cpu:
                    max_med_cpu = inc

               n_med_mem += 1
               inc = float(item[31:38].strip().replace(',','.'))/1024
               avg_med_mem += inc
               if inc >= max_med_mem:
                    max_med_mem = inc                          
print('Количество обработанных строк по:')
print(f'gunicorn cpu        [{n_gui_cpu}]')
print(f'gunicorn mem        [{n_gui_mem}]')
print(f'archive-manager cpu [{n_arc_cpu}]')
print(f'archive-manager mem [{n_arc_mem}]')
print(f'node-manager cpu    [{n_nod_cpu}]')
print(f'node-manager mem    [{n_nod_mem}]')
print(f'media-server cpu    [{n_med_cpu}]')
print(f'media-server mem    [{n_med_mem}]')
print('stop top_log.')
if docker_log == 1:
    print('strat docker_log:')
    with open('C:/work/logs/docker.txt') as file:
        for item in file:
            if 'archive-manager' in item:
               
               d_n_arc_cpu += 1
               try:
               
                   inc = float(item[38:42].strip())
                   d_avg_arc_cpu += inc
                   if inc >= d_max_arc_cpu:
                       d_max_arc_cpu = inc

                   d_n_arc_mem += 1
                   inc = float(item[48:53].strip().rstrip('GMKib'))
                   d_avg_arc_mem += inc
                   if inc >= d_max_arc_mem:
                       d_max_arc_mem = inc
                   d_arc_mem_lit = item[53]   
               except:
                   next                         
            elif 'node-manager' in item:
               d_n_nod_cpu += 1
               inc = float(item[38:42].strip())
               d_avg_nod_cpu += inc
               if inc >= d_max_nod_cpu:
                    d_max_nod_cpu = inc

               d_n_nod_mem += 1
               inc = float(item[48:53].strip().rstrip('GMKib'))
               d_avg_nod_mem += inc
               if inc >= d_max_nod_mem:
                    d_max_nod_mem = inc
               d_nod_mem_lit = item[53]

            elif 'media-server' in item:
               d_n_med_cpu += 1
               inc = float(item[48:52].strip())
               d_avg_med_cpu += inc
               if inc >= d_max_med_cpu:
                    d_max_med_cpu = inc

               d_n_med_mem += 1
               inc = float(item[48:53].strip().rstrip('GMKib'))
               d_avg_med_mem += inc
               if inc >= d_max_med_mem:
                    d_max_med_mem = inc
               d_med_mem_lit = item[53]

    print('Количество обработанных строк по:')
    print(f'archive-manager cpu [{d_n_arc_cpu}]')
    print(f'archive-manager mem [{d_n_arc_mem}]')
    print(f'node-manager cpu    [{d_n_nod_cpu}]')
    print(f'node-manager mem    [{d_n_nod_mem}]')
    print(f'media-server cpu    [{d_n_med_cpu}]')
    print(f'media-server mem    [{d_n_med_mem}]')
    print('stop docker_log.')

with open('C:/work/logs/filtered_log.txt', 'a') as _file:
        _file.write(f'\n{'=' * 68}')
        _file.write('\nДанные по логу TOP:\n')
        _file.write(f'\n<gunicorn>        пиковое / среднее значение CPU:  {round(max_gui_cpu, 2)} / {round(avg_gui_cpu / n_gui_cpu, 2)}')
        _file.write(f'\n<gunicorn>        пиковое / среднее значение MEM:  {round(max_gui_mem, 2)}M / {round(avg_gui_mem / n_gui_mem, 2)}M\n')
        _file.write(f'\n{'-' * 68}')
        _file.write(f'\n<archive-manager> пиковое / среднее значение CPU:  {round(max_arc_cpu, 2)} / {round(avg_arc_cpu / n_arc_cpu, 2)}')
        _file.write(f'\n<archive-manager> пиковое / среднее значение MEM:  {round(max_arc_mem, 2)}M / {round(avg_arc_mem / n_arc_mem, 2)}M\n')
        _file.write(f'\n<node-manager>    пиковое / среднее значение CPU:  {round(max_nod_cpu, 2)} / {round(avg_nod_cpu / n_nod_cpu, 2)}')
        _file.write(f'\n<node-manager>    пиковое / среднее значение MEM:  {round(max_nod_mem, 2)}M / {round(avg_nod_mem / n_nod_mem, 2)}M\n')
        _file.write(f'\n<media-server>    пиковое / среднее значение CPU:  {round(max_med_cpu, 2)} / {round(avg_med_cpu / n_med_cpu, 2)}')
        _file.write(f'\n<media-server>    пиковое / среднее значение MEM:  {round(max_med_mem, 2)}M / {round(avg_med_mem / n_med_mem, 2)}M\n')
        
        _file.write(f'\n{'=' * 68}')
        _file.write('\nДанные по логу DOCKER:\n')
        _file.write(f'\n<archive-manager> пиковое / среднее значение CPU:  {round(d_max_arc_cpu, 2)} / {round(d_avg_arc_cpu / d_n_arc_cpu, 2)}')
        _file.write(f'\n<archive-manager> пиковое / среднее значение MEM:  {round(d_max_arc_mem, 2)}{d_arc_mem_lit} / {round(d_avg_arc_mem / d_n_arc_mem, 2)}{d_arc_mem_lit}\n')
        _file.write(f'\n<node-manager>    пиковое / среднее значение CPU:  {round(d_max_nod_cpu, 2)} / {round(d_avg_nod_cpu / d_n_nod_cpu, 2)}')
        _file.write(f'\n<node-manager>    пиковое / среднее значение MEM:  {round(d_max_nod_mem, 2)}{d_nod_mem_lit} / {round(d_avg_nod_mem / d_n_nod_mem, 2)}{d_nod_mem_lit}\n')
        _file.write(f'\n<media-server>    пиковое / среднее значение CPU:  {round(d_max_med_cpu, 2)} / {round(d_avg_med_cpu / d_n_med_cpu, 2)}')
        _file.write(f'\n<media-server>    пиковое / среднее значение MEM:  {round(d_max_med_mem, 2)}{d_med_mem_lit} / {round(d_avg_med_mem / d_n_med_mem, 2)}{d_med_mem_lit}\n')
        
       
        _file.write(f'{'_' * 68}')
                     
print ('DONE')
