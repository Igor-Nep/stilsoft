with open('c:\work\WHPython\log_aec(850).txt', 'r') as f:
    for item in f:
        if 'aec7d32b-0887-47d4-888d-b232798a5a21' in item:
             with open ('C:/work/WHPython/log_only_850.txt', 'a') as l_file:
                l_file.write(f'\n{item}\n')
                print(item)