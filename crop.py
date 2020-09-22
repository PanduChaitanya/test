from PIL import Image
image = Image.open("car.jpg") 
  
crop= image.crop((30, 700, 900, 800))
crop.show()
 
