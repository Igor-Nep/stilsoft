class Hero:
    
    def __init__(self,money):
        self.money = money

    def can_i_buy(self,price):
        return self.money >= price
    
hero = Hero(400)

print(hero.can_i_buy(350))
print(hero.can_i_buy(500))