with open('C:/work/logs/node_log10.txt', encoding='utf8') as file:
    for item in file:
        if 'b711fe9d-ad04-4989-96ec-dd931f8dba48' in item:
            with open('C:/work/logs/filtred_node_media.txt', 'a') as _file:
               
                _file.write(item)
        elif '172.18.18.216' in item:
            with open('C:/work/logs/filtred_node_media.txt', 'a') as _file:
               
                _file.write(item)        
                
print ('DONE')
      