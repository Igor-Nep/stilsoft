class Bottle:

	def __init__(self, color, volume):
		self.col = color
		self.vol = volume
		

bottle_1 = Bottle("Красная", 0.7)
bottle_2 = Bottle('Белая', 0.3)
bottle_3 = Bottle('Черная', 0.1)

# Не удаляйте этот код, он нужен для проверки

print(bottle_1.col, bottle_1.vol)
print(bottle_2.col, bottle_2.vol)
print(bottle_3.col, bottle_3.vol)