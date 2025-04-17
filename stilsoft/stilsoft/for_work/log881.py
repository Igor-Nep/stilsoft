string_index = 0
find_frases = ['pos_01','pos_02','pos_03','pos_04','pos_05','pos_06','pos_07']
with open(f'C:\Users\nepretimov_i\Desktop\patrol02\log_881_ptr.txt', 'a') as file:
    string_index+=1
    if string_index == 1 or string_index == 2:
        frase = find_frases[0]
    elif string_index == 3 or string_index == 4:
        frase = find_frases[1]
    elif string_index == 5 or string_index == 6:
        frase = find_frases[2]        
    
