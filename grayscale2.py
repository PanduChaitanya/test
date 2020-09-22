from PIL import Image
image=Image.open("car.jpg")
gray=image.convert('L')
gray.show()