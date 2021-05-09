#Totally bitchin pimpin up of an image to 80s MTV style
# Props to course instructor Michael Eramo for this piece of code. Got this from his blog

from PIL import Image

def color(image):
    '''Converts image to 80s color scheme style photo. Hello Nostalgia'''

    new_image = Image.new('RGB', image.size) #Settiing up the new image
    new_image_data = []

    image = image.convert('L') #converting to grayscale

    for color in image.getdata(): #using only 8 colors - RGB, CYM and W,B to create new pixel values
        if color < 32:
            new_image_data.append((0,0,0))
        elif color < 64:
            new_image_data.append((0,0,255))
        elif color < 96:
            new_image_data.append((0,255,0))
        elif color < 128:
            new_image_data.append((0,255,255))
        elif color < 160:
            new_image_data.append((255,0,0))
        elif color < 192:
            new_image_data.append((255,0,255))
        elif color < 224:
            new_image_data.append((255,255,0))
        else:
            new_image_data.append((255,255,255))
    
    new_image.putdata(new_image_data)
    return new_image

base_photo = r'mountains.jpg' #put in your image here
base_image = Image.open(base_photo)

new_image = color(base_image)
new_image.save(r'pimpedup_80s_style.jpg')