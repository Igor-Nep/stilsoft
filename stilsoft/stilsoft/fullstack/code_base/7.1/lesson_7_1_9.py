fish = [

{"specie": "Белуга", "water": "fresh"},
{"specie": "Карась", "water": "fresh"},
{"specie": "Красноперка", "water": "fresh"},

{"specie": "Морской окунь", "water": "sea"},
{"specie": "Тунец", "water": "sea"},
{"specie": "Скумбрия", "water": "sea"},

]

sea_water = []
fresh_water = []

for item in range(0, int(len(fish))):
    if fish[item]['water']=='fresh':
        fresh_water.append(fish[item]['specie'])
    else:
        sea_water.append(fish[item]['specie'])

print('Морские: ', end='')
print(*sea_water, sep=', ')
print('Пресноводные: ', end='')
print(*fresh_water, sep=', ') 