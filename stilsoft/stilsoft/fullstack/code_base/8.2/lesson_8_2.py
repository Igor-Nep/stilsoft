class Fish():
    '''Рыбы в основном молчат и плавают'''
    def __init__(self, name):
        self.name = name

    def swin(self):
        print('I am swiming')

    def __repr__(self):
        return 'Fish ' + self.name


fish = Fish('Dorri')
print(fish.__doc__) 

class Employee:
    '''Unit class, which is prining FIO'''

    def __init__(self, f,i,o):
        self.f = f
        self.i = i
        self.o = o

    def __repr__(self):
        return f'{self.f} {self.i[0]}. {self.o[0]}.'    

employees = [Employee('Питерская','Александра','Алексеевна'), Employee('Меньшова','Дарья','Игоревна'), Employee('Кручина','Ирина','Васильевна')]

for i in range(len(employees)):
    print(employees[i])



print(employees[1].__doc__)