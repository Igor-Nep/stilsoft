keywords = ["Желание", "Семнадцать", "Ржавый", "Пропуск", "Печь" ]

word_count = {}

for i in keywords:
    ln = len(i)
    word_count[i] = ln

# Не удаляйте код ниже: он нужен для проверки.
print('word count ', word_count )

print(word_count.get(input('Желание')))