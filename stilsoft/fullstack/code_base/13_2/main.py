class Employee:
    raise_coef = 1.1
    def __init__(self, name, last, pay):
        self.name = name
        self.last = last
        self.__pay = pay



    def f_string(self, data_string):
        self.name, self.surname, self.pay = data_string.split(' ')
        self.pay = int(self.pay)
        return self.name, self.surname, self.pay    

    @classmethod
    def from_string(cls, data_string):
        name, last, pay = data_string.split(' ')
        pay = int(pay)
        return cls(name,last,pay)
    
    @classmethod
    def set_raise_amount(cls, new_coef):

        cls.raise_coef = new_coef

    @staticmethod
    def is_workday():
        from datetime import datetime
        now = datetime.now()
        if now.weekday() == 5 or now.weekday() == 6:
            return False
        return True
    
    @property
    def email(self):
        return f'{self.name}.{self.last}@mail.com'
    
    @property
    def pay(self):
        return self.__pay
    
    
    def raise_pay(self):
        self.__pay = self.raise_coef
          

if __name__ == '__main__':
    emp_1 = Employee('Igor', 'Nemov', 50000)
    #test_case_1
    assert emp_1.email == 'Igor.Nemov@mail.com'

    #test_case_2
    emp_1.raise_pay()
    assert 50000 * Employee.raise_coef == emp_1.__pay

    assert emp_1.pay == 55000.00000000001

    #testcase 3# New object

    emp_2 = Employee.from_string(data_string='Ivan Boroda 100000')
    assert isinstance(emp_2, Employee)
    assert emp_2.name == 'Ivan'
    assert emp_2.last == 'Boroda'
    assert emp_2.pay == 100000

    #testcase 4 # test raise amount
    Employee.set_raise_amount(2)
    assert Employee.raise_coef == 2
    assert emp_1.raise_coef == 2
    assert emp_2.raise_coef == 2

    #testcase 5 # is workday
    assert Employee.is_workday() == True

    #testcase 6 # property get email
    assert emp_1.email == 'Igor.Nemov@mail.com'



