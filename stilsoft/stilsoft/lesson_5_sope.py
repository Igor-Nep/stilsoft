the_int = 0
the_float = 0.0
the_str = "-"
the_bool = False
the_list = [0]
the_dict = {0:0}

def the_change():
   the_int = 1
   the_float = 1.0
   the_str = "+"
   the_bool = True
   the_list.append(1)
   the_dict[1] = 1

the_change()

print(the_int)
print(the_float)
print(the_str)
print(the_bool)
print(the_list)
print(the_dict)

#5_2func-s

def check(prices, tip = 10):
   summ_ = sum(prices)
   total = summ_ * (100 + tip) / 100

   return total

print(check([100, 300, 500])) 
print(check([100, 300, 500], 0))
print(check([100, 300, 500], 20))
      