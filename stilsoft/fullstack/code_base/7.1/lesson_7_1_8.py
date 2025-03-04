employees = [

 {"fio": "Киселёв Всеволод Эдуардович", "vaccinated": True},
 {"fio": "Довлатова Эмилия Ефимовна", "vaccinated": False},
 {"fio": "Аверин Мартын Егорович", "vaccinated": True},
 {"fio": "Князева Августа Егоровна", "vaccinated": False}, 
 {"fio": "Шанская Аграфена Семёновна", "vaccinated": True},
 {"fio": "Куприна Марина Викторовна", "vaccinated": False},
 {"fio": "Селезнёв Константин Игоревич", "vaccinated": False},   
]

vaccinated = []
not_vaccinated = []

for item in range(0, int(len(employees))):
    if employees[item]['vaccinated']:
        vaccinated.append(employees[item]['fio'])
    else:
        not_vaccinated.append(employees[item]['fio'])

print('Вакцинированные:')
for i in vaccinated:
    print(i)
print('Остальные:')
for i in not_vaccinated:
    print(i)    