from PIL import Image, ImageFilter


img = Image.open("car.jpg")
blurred = img.filter(ImageFilter.BLUR)

blurred.show()