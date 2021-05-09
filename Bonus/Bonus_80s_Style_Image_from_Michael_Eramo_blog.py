#Totally bitchin pimpin up of an image to 80s MTV style
from PIL import Image

def color(image):
    new_image = Image.new('RGB', image.size)
    new_image_data = []

    image = image.convert('L')

    for color in image.getdata():
        if color < 32:
            new_image_data.app