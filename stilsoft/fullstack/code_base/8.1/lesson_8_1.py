class Hero:

  def __init__(self, name, things):
    self.name = name
    self.things = things
    print(f'Я {self.name}, у меня есть {self.things}')

  def iter_things(self):
    for thing in self.things:
      print(thing)

  def go_right(self):
    print(f"{self.name} Я иду направо")

  def go_left(self):
    print("Я иду налево")

  def observe(self):
    print("Я осматриваюсь")

hero_1 = Hero('Печений', ['Голова','Лапки','Пуговичка','Масочка'])
hero_1.go_right()
hero_1.iter_things()