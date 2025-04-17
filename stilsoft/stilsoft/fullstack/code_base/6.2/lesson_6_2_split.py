with open('C:\work\WHPython\stilsoft\students.txt') as file:
    for student_data in file:
        #data = student_data.rstrip('\n').split(':')
        #name = data[0]
        #language = data[1]

        name, language = student_data.rstrip('\n').split(':')
        print(f'{name} learn {language}!')

#shopping_list
row_index = 0
items_count = 0
items_summ = 0
with open('C:\work\WHPython\stilsoft\shopping_list.txt', encoding="utf-8") as file:
    for item_data in file:
        row_index += 1
        if item_data.count(':') < 2:
            print(f'in string {row_index} error')
            continue

        item, quantity, price = item_data.strip().split(':')
        items_count += 1
        items_summ += int(price) * int(quantity)

    print(f'In list {items_count} positions with {items_summ} rub')



with open('C:/work/WHPython/log945.txt', encoding="utf-8") as file:
    for item in file:
        if '9451284b-149c-4c67-a4bf-8bd0b9244b2e' in item:
            with open('C:/work/WHPython/log_only_945.txt', 'w') as file:
                file.write(f'{item}\n')
