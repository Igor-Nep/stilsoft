with open('writed_data.txt', 'wt') as file: #write, text
    file.write('Hello\n')
    file.write('World\n')
    file.write('newline text\n')

user_language = input('Какой язык учите? ')
user_time = input('Как давно? ')
user_institution = input('Где? ')

with open('answers.txt', 'w') as file:
    file.write(f'{user_language}\n')
    file.write(f'{user_time}\n')
    file.write(f'{user_institution}\n')

print('Ответы записаны')

for i in range(10):
    with open('answers.txt', 'w') as file:
        file.write(f'{user_language}\n')