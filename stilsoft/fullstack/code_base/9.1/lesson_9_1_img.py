from PIL import Image, ImageDraw

img = Image.new('RGB', (780, 340), 'white')
draw = ImageDraw.Draw(img)

data='1101110001101011000111111'
for x in range(5):
    for y in range(5):
        if data[x + y *5]==1:
            draw.rectangle((x*10, y*10, x*10 + 9, y*10 + 9), fill = 'black')

for x in range(255):
    for y in range(255):
        draw.point((x,y +80), fill=(x,0,y))
        draw.point((x+260,y +80), fill=(y,x,y))
        draw.point((x+520,y +80), fill=(y,y,x))

img.show()