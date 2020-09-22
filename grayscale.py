from PIL import Image, ImageOps 
im1 = Image.open("car.jpg") 
gray=ImageOps.grayscale(im1)
gray.show() 


