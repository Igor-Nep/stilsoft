import random 
from random import randint

print(randint(10, 1000))
my_list = [2,5,6,8,9]
random.shuffle(my_list)
print(my_list)

name = 'Alice'
items = random.sample(name, 3)
result = ''.join(items)
print(result)
gifts = ['candy', 'chocolate', 'coke', 'balls', 'chess']
index = randint(0, len(gifts) - 1)
gift = gifts[index]
print(f'Your gist is {gift}')

random.shuffle(gifts)
gift = gifts[0]
print(f'Your gist is {gift}')

gift = random.sample(gifts, 1)[0]
print(f'Your gist is {gift}')

def alpha_tango():
    my_str = 'Papa Yankee Tango Hotel Oscar November'
    list_str = my_str.split()

    new_str = ''
    for word in list_str:
        new_str += word[0]
    print(my_str)
    print(list_str)    
    print(new_str)

def random_gift():
    gifts = ['candy', 'chocolate', 'coke', 'balls', 'chess']
    
    gift = random.sample(gifts, 1)[0]
    print(f'Your gist is {gift}')   


#while True:
    #input()
    #random_gift()


text = "The quick brown fox jumps over the lazy dog"


def text_length():
    n = 0
    for i in range(len(text)):
      if text[i] != ' ':
         n+=1
    return n

def text_length_full():
    n = 0
    for i in range(len(text)):
      n+=1
    return n

def text_word_count():
    sp = 0
    for i in range(len(text)):
      if text[i] == ' ':
        sp+=1
    return sp+1    

# Не удаляйте код ниже, он нужен для вызова и тестирования функции

print(text_length())
print(text_length_full())
print(text_word_count())