
from PIL import Image, ImageDraw
import os 

"""
Prerequisite Python Library- 
pip install pillow
pip install os

This script to convert Rectangular shape image into smooth round corner shape image.
"""
img_input = "F:\\Codebase_Python\\auto_feature0001\\ImgFolder\\InputImage"
img_output = "F:\\Codebase_Python\\auto_feature0001\\ImgFolder\\OutputImage" 

img_Name_list = os.listdir(img_input)

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
    for i  in range(0, len(img_Name_list)):
        if img_Name_list[i].endswith(('.png', '.jpg', '.jpeg')):
            im = Image.open(f"{img_input}\\{img_Name_list[i]}")
            im = round_corners(im, 100)
            im.save(f"{img_output}\\Image_round{i}.png")
