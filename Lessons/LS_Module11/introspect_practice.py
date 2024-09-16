from PIL import Image
from PIL import ImageDraw, ImageFont

im = Image.open('img_1.png')
im = im.resize((180, 180))
# out.show()


def new_photo(name):
    image = Image.open(name)
    w, h = image.size
    return image.resize((w, h))  # тут можно править w и h, но я не захотел


im2 = new_photo('img_2.jpg')

im2.paste(im, (700, 340))
# im2.show()

draw = ImageDraw.Draw(im2)
font = ImageFont.truetype('creepster.otf', 150)
draw.text((40, 350), 'Ему пизда', font=font, fill='red')

im2.show()