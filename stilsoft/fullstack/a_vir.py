vc = 'print("I am virus")'

with open ('knb.py') as file:
    content = file.read()

    if vc in content:
        print('visus is found')