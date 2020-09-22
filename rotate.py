from PIL import Image

image=Image.open('car.jpg')

image.rotate(90).show()
image.rotate(180).show()
image.rotate(-90).show()
