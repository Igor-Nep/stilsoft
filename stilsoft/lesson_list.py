text = 'Mom, i am graphoman'

let_count = 0
word_count = 0
sp_count = 0



for i in text:
      if i not in [',', ' ', '!']:
             let_count += 1
      elif i == ' ':
             sp_count += 1      
      
if sp_count>0:
            word_count = sp_count+1
elif let_count>0:
            word_count=1            

print(f'Letters: {let_count}')
print(f'Words: {word_count}') 

letters = ''.join(chr(n) for n in range(ord('a'),ord('z')+1))
letters = ''.join(chr(n) for n in range(97,123))
print(type(letters))
