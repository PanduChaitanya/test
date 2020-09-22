from PIL import Image


image=Image.open('car.jpg')
resize=image.resize((300,60))
resize.show()
