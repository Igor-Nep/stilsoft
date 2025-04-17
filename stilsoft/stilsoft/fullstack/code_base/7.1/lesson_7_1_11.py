order = [
 {"skolko": 5.0, "poroda": "тунец", "sred_razmer": 300},
 {"skolko": 15.0, "poroda": "окунь", "sred_razmer": 250},
 {"skolko": 20.0, "poroda": "щука", "sred_razmer": 460},
]
order_converted = []

for item in range(0, int(len(order))):
    order[item]['count'] = order[item].pop('skolko')
    order[item]['specie'] = order[item].pop('poroda')
    order[item]['avg_size'] = order[item].pop('sred_razmer')
    order[item]['count'] = int(order[item]['count'])
    order[item]['specie'] = str.title(order[item]['specie'])
    order[item]['avg_size'] = int(order[item]['avg_size'] /10)
    order_converted.append(order[item])
    
for item in order_converted:
  for key, value in item.items():
      print(key, value)  

    
