from PIL import Image, ImageFilter
import random


users = {
    'Непретимов': 'Игорь',
    'Самохвалов': 'Евгений',
    'Горемыкин': 'Олег',
    'Зимоглядов': 'Денис',
    'Мартынов': 'Илья',
     }


collage_width = 0
collage_height = 0

a = 0


for k, v in users.items():
     file = f'c:/work/selen_images/{k}_{v}.jpg'
     with Image.open(file) as file:
         collage_width += file.width
         if file.height >= collage_height:
             collage_height = file.height

collage = Image.new('RGB',(collage_width, collage_height), (250,250,250))
collage.save('c:/work/selen_images/collage.jpg')

up_down = [0, 400, 200]
rotator =[4, -4, 3, -3]

for k, v in users.items():
     add_file = f'c:/work/selen_images/{k}_{v}.jpg'
     with Image.open(add_file) as ad_image:
        width, height = ad_image.size
        ad1_image = ad_image.convert('L')
        add_image = ad1_image.filter(ImageFilter.SMOOTH)
        add_image = add_image.filter(ImageFilter.FIND_EDGES)
        #add_image = ad1_image.rotate(int(random.choice(rotator)))
        #paste_image = add_image.resize((int(width/1), int(height/1)))
            
        try:
             collage = Image.open('c:/work/selen_images/collage.jpg')
             collage.paste(add_image,(a, int(random.choice(up_down))))
             a+=add_image.width
             print(collage_height)
           
             collage.save('c:/work/selen_images/collage.jpg')
            
        except IOError:
            pass

#collage.show()

