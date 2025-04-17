
#У вас есть текст, в котором встречаются #хештеги. Напишите функцию get_hash(text). Верните все хештеги одним списком.
def get_hashtags(text):

    words = text.split(" ")
    hashtags = []
    for word in words:
        if word[0] == '#':
            hashtags.append(word[1:])
    return hashtags


# Не удаляйте код ниже, он нужен для проверки    

words = input()
result = get_hashtags(words)
print(result)