class Hero:

  def __init__(self, name):
    self.things = []
    pass

  def collect(self, thing):
    self.things.append(thing)


pythomir = Hero("Питомир")
pythomir.collect("Усы хитрости")
pythomir.collect("Рукавички пряморукости")

if len(pythomir.things) == 2:
  print("Проверка пройдена")
else: 
  print("Добавление в список things работает некорректно")