print('У меня есть Большие Буквы и маленькие буквы'.upper().count('БУКВЫ'))

old_var='variables with spaces is not good'
new_var = old_var.replace(' ' , '_')
print(new_var)

sample = "маленькая змея Василиса говорит с-с-с-с!"
print(sample.find("М"))
print(sample.title())

s = 'Альфа, Браво, Чарли'
s = s.split(', ')
print(s[1])
print(type(s))

print(' '.join(s))
print('/'.join(s))
print(''.join(s))

message = '''
Всем привет, кто изучает #питон 
вместе с @happysnake
'''
tags = []
people = []
text = message.replace(',', '')
words=text.split(' ')
for word in words:
    if word.startswith('#'):
        tags.append(word)
    elif word[0]=='@':
        people.append(word)
people_join = ' '.join(people)        
tags_join=' '.join(tags)
print(f'peoples: {people_join}')           
print(f'tags: {tags_join}')

code = "Echo Sierra Charlie Alfa Papa Echo"
decode =[]
code_list = code.split(' ')
for i in range(len(code_list)):
  elm = code_list[i]
  decode.append(elm[0])

print (''.join(decode))

data = '5:100'
data = data.split(':')
summ = int(data[0]) * int(data[1])
print(summ)


text = "734 122 мне 877 119 022 кажется 127 0 0 1 за 192 168 нами 255 255 следят 32 32 2 5"
just_words = []
just_digits=[]
text = text.split(' ')
for i in range(len(text)):
  if text[i].isalpha():
    just_words.append(text[i])

  elif text[i].isdigit():
     just_digits.append(text[i])
text_cleaned = ' '.join(just_words)
digits_cleaned = ' '.join(just_digits)
print(text_cleaned)
print(digits_cleaned)