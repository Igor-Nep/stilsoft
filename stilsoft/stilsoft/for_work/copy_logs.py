with open('C:/work/logs/sdp850_2/app_serv_node_logs_after_drop.txt', 'r', encoding='utf-8') as app_s_file:
   
    with open('C:/work/logs/sdp850_3/app_serv_node_logs_after_drop.txt','w', encoding='utf-8') as new_app_s_file:
        new_app_s_file.write(str(app_s_file))