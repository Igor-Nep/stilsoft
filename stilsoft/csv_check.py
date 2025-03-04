import csv

tar_list=[]
with open('c:/csv/1344.csv', 'r', encoding='utf-8') as file:
    c_file = csv.reader(file)
    for line in c_file:
        
        if 'Потеря связи' in str(line):
            tar_list.append(str(line))
            

with open('c:/csv/11.txt', 'a') as file:
    for i in tar_list:
        file.write(f'{i}\n')
    file.write(f'Target incident count: {len(tar_list)}')
