#Import required library
from PIL import Image

#Open Image
image=Image.open('sanki.jpeg')

image.rotate(90).show()
image.rotate(180).show()
image.rotate(-90).show()
