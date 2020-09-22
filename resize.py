from PIL import Image


image=Image.open('car.jpg')
image.resize((300,60))
image.show()