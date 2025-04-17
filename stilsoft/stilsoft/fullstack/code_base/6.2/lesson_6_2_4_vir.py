
vc = 'print("I am virus")'

with open ('knb.py', 'a') as file:
    file.write(f'\n{vc}\n')