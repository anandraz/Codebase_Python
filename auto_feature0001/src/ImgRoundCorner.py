
from PIL import Image, ImageFilter, ImageEnhance, ImageDraw

"""
Python Library- pip install pillow
This script is to make image round corner 
it take input of Rectangular image and convert that image to round corner
"""
img_path = "auto_feature0001\ImgFolder\Image01.jpg"
def round_corners(im, rad):
    circle = Image.new('L', (rad * 2, rad * 2), 0)
    draw = ImageDraw.Draw(circle)
    draw.ellipse((0, 0, rad * 2, rad * 2), fill=255)
    alpha = Image.new('L', im.size, 255)
    w, h = im.size
    alpha.paste(circle.crop((0, 0, rad, rad)), (0, 0))
    alpha.paste(circle.crop((0, rad, rad, rad * 2)), (0, h - rad))
    alpha.paste(circle.crop((rad, 0, rad * 2, rad)), (w - rad, 0))
    alpha.paste(circle.crop((rad, rad, rad * 2, rad * 2)), (w - rad, h - rad))
    im.putalpha(alpha)
    return im

if __name__ == '__main__':
    im = Image.open(img_path)
    im = round_corners(im, 100)
    im.save('auto_feature0001\ImgFolder\Image01_round.png')