response = int(input('Введите количество секунд: '))
days = response // 86400 
hours = response // 3600 % 24
minutes = response // 60 % 60
seconds = response % 60

print(f'Дней: {days}')
print(f'Часов: {hours}')
print(f'Минут: {minutes}')
print(f'Секунд: {seconds}')
