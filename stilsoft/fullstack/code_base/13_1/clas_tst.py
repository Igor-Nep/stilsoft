class Employee:
    raise_coef = 1.1
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.email = f'{self.name}.{self.last}@mail.com'  
        self.pay = pay

    def raise_pay(self):
        self.pay *= self.raise_coef

if __name__ == '__main__':
    emp_1 = Employee('Igor', 'Nemov', 50000)
    #test_case_1
    assert emp_1.email == 'Igor.Nemov@mail.com'

    #test_case_2
    emp_1.raise_pay()
    assert 50000 * Employee.raise_coef == emp_1.pay

    assert emp_1.pay == 55000.00000000001
