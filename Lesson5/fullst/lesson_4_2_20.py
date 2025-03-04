guests = {
  "Алиса": True, 
  "Эльдар" : False, 
  "Агата": False, 
  "Ярослав": True,
}

for k,v in guests.items():
    if v:
        print(k)

