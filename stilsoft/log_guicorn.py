with open('C:/work/11/14/LOG_TOP.txt') as file:
    avg_gui_cpu = 0.0
    max_gui_cpu = 0.0
    n_gui_cpu = 0
    
    for item in file:
        if 'gunicorn' in item:
            n_gui_cpu += 1
            inc = float(item[49:52].replace(',','.'))
            avg_gui_cpu += inc
            if inc >= max_gui_cpu:
                 max_gui_cpu = inc
        
with open('C:/work/11/14/log_gnui.txt', 'a') as _file:
        _file.write(f'\n<guicorn> пиковое значение CPU: {max_gui_cpu}')
        _file.write(f'\n<guicorn> среднее значение CPU: {round(avg_gui_cpu / n_gui_cpu, 2)}\n')
       
        _file.write(f'{'_'*52}')
                     
print ('DONE')


      