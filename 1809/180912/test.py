from PIL import Image

image = Image.open('CITS1.tif')

print (image.__class__)
print (image.format, image.size, image.mode)
