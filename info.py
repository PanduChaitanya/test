from PIL import Image
image=Image.open('car.jpg')
print("Format: {0}\nSize: {1}\nMode: {2}".format(image.format, image.size, image.mode))