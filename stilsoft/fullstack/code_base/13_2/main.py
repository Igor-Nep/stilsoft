class Employee:
    raise_coef = 1.1
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.email = f'{self.name}.{self.last}@mail.com'  
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef

    def f_string(self, data_string):
        self.name, self.surname, self.pay = data_string.split(' ')
        self.pay = int(self.pay)
        return self.name, self.surname, self.pay    

    #@classmethod
    def from_string(self, data_string):
        name, surname, pay = data_string.split(' ')
        pay = int(pay)
        return name,surname,pay

if __name__ == '__main__':
    emp_1 = Employee('Igor', 'Nemov', 50000)
    #test_case_1
    assert emp_1.email == 'Igor.Nemov@mail.com'

    #test_case_2
    emp_1.raise_pay()
    assert 50000 * Employee.raise_coef == emp_1.pay

    assert emp_1.pay == 55000.00000000001

    #testcase 3# New object

    emp_2 = Employee.f_string(data_string='Ivan Boroda 100000')
    assert isinstance(emp_2, Employee)
    assert emp_2.name == 'Ivan'
    assert emp_2.last == 'Boroda'
    assert emp_2.pay == 100000
