expl = {True:'Всё норм', False:'Не пойдёт!'}
print(expl[3>2])

dictionary = {'cat':'is Cat'}
dictionary['dog'] = 'is Dog'
print(dictionary)
del dictionary['cat']
print(dictionary)
dictionary['dog'] = 'is Dog1'
print(dictionary)

weather = {
"Москва": True, 
"Новосибирск" : True , 
"Екатеринбург": False, 
"Хабаровск": True,
}

expl = {True:'Есть осадки', False:'Нет осадков'}
location = input()
#print(expl[weather[location]])

#__________________________________________________
students = {
  "Алиса": 70, 
  "Эльдар" : 20 , 
  "Агата": 40, 
  "Ярослав": 84,
}

user_input = input('Агата')
if students[user_input]>=81:
    print(f'{students[user_input]} баллов, оценка A')
elif 80>=students[user_input]>=61:
    print(f'{students[user_input]} баллов, оценка B')
elif 60>=students[user_input]>=0:
    print(f'{students[user_input]} баллов, оценка C')    

#2
keywords = ["Желание", "Семнадцать", "Ржавый", "Пропуск", "Печь" ]

word_count = {}

for i in keywords:
    ln = len(i)
    word_count[i] = ln

# Не удаляйте код ниже: он нужен для проверки.
print('word count '+ word_count )

print(word_count.get(input('Желание')))