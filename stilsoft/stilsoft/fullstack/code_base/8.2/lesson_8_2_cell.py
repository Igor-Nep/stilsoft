class Input:
    def __init__(self, name, value = None):
        self.name = name
        self.value = value

class TextInput(Input):
    def is_empty(self):
        return self.value == None

class EmailInput(TextInput):
    def check(self):
        has_at = self.value.count('@') == 1
        has_dot = self.value.count('.') >= 1
        if has_at and has_dot:
            return True
        return False

class PasswordInput(TextInput):
    def check(self):
        if len(self.value)<8:
            return

mailer = EmailInput('first','frist__001@mail.com')
print(mailer.is_empty())
if mailer.check():
    print('found')
else:
    print('not found')

#объединение классов

class Person():
    def eat(self):
        print('Nyam')

class Employee(Person):
    def visit_demo(self):
        print('Go to demo')

class Developer(Employee):
    def code_review(self):
        print('Make code review')

class FrontDev(Developer):
    def code_front(self):
        print('Make front code')

class BackDev(Developer):
    def code_back(self):
        print('Make back code')

class FullstackDev(FrontDev,BackDev):
    pass                

human = FullstackDev()
human.code_front()
human.eat()


#4 supersender групповое наследование

class SMSSender:
    def send_sms(self, message):
        print('Passing SMS ', message)

class PushSender:
    def send_push(self, message):
        print('Passing Push ', message)

class MailSender:
    def send_mail(self, message):
        print('Passing mail ', message)

class SuperSender(SMSSender,PushSender,MailSender):
    def send_all(self, message):
        self.send_sms(message)
        self.send_push(message)
        self.send_mail(message)

sender = SuperSender()
sender.send_all('Zal')

