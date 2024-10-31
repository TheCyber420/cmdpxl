from PIL import Image
from filewriter import Filewriter

#Constants
TOP_PIXEL = "▀"
BOTTOM_PIXEL = "▄"

#Public functions
def create_new_sprite(filename, size):    
    image = _read_image(filename, size)
    width , height = image.size
    _create_image(filename, list(image.getdata()), width, height)

def display_image(filename):
    with open(filename, "r") as file:
        print(file.read())

#Private functions
def _read_image(filename, size):
    image_path = f"{filename}"
    image = Image.open(image_path).convert('RGBA')

    if size != None:
        if 'x' in size:
            width, height = map(int, size.split('x'))
            image = image.resize((width, height), Image.LANCZOS)
        else:
            width , height = image.size
            max_size = int(size)
            ratio = width / height

            if width > height:
                new_width = max_size
                new_height = int(max_size / ratio)
            else:
                new_height = max_size
                new_width = int(max_size * ratio)

            image = image.resize((new_width, new_height), Image.LANCZOS)
            

    return image

def _create_image(filename, pixels, width, height):
    writer = Filewriter(filename)
    for row in range(0, height, 2):
        for col in range(width):
            top_idx = row * width + col
            top_pixel = pixels[top_idx]

            bottom_idx = top_idx + width
            if bottom_idx >= width * height:
                bottom_pixel = (0, 0, 0, 0)
            else:
                bottom_pixel = pixels[bottom_idx]

            if bottom_pixel[3] < 10 and top_pixel[3] < 10:
                writer.write_empty()
            elif bottom_pixel[3] < 10:
                writer.write_one_pixel(top_pixel, TOP_PIXEL)
            elif top_pixel[3] < 10:
                writer.write_one_pixel(bottom_pixel, BOTTOM_PIXEL)
            else:
                writer.write_both_pixels(top_pixel, bottom_pixel, TOP_PIXEL)
        writer.write_new_line()


