class Hero():

  def __init__(self, name, posessions):
    self.name = name
    self.posessions = posessions
  def __repr__(self):
    return 'Герой Питомир взял с собой меч, плащ, шляпа'
# Не удаляйте код ниже, он нужен для проверки

hero = Hero("Питомир", ["меч", "плащ", "шляпа"]) 
print(hero)