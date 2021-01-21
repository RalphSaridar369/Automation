# Imports PIL module
# Mainly this file is to change a certain property in a large number of jpgs/pngs

from PIL import Image,ImageChops,ImageFilter

# open method used to open different extension image file
im1= "logo.png"
i = Image.open(im1)

new_i=i.resize((640,480))
new_i.save("resized.png")

new_i=i.rotate(90)
new_i.save("rotated.png")



# This method will show image in any image viewer
