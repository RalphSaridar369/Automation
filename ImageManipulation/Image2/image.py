import PIL
from PIL import Image
import os


#change the directory depending on your folder

directory = 'C:/Users/Ralph/PycharmProjects/pythonProject/automation/Image2/New folder'

for img in os.listdir(directory):
        im = directory + "/" +img
        im1= Image.open(im)
        new_name = img.replace(".png",".jpg")
        new_im = im1.rotate(90).resize((128,128))
        new_im.save(f'C:/Users/Ralph/PycharmProjects/pythonProject/automation/Image2/test/{new_name}')