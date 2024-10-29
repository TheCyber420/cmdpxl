from PIL import Image
from filewriter import Filewriter
import os

#Constants
TOP_PIXEL = "▀"
BOTTOM_PIXEL = "▄"

#Public functions
def create_new_sprite(filename):
    if not os.path.exists(f"input/{filename}"):
        print(f"An error has occured:\nFile {filename} not found")
        return
    
    image = _read_image(filename)
    width , height = image.size
    _create_image(filename, list(image.getdata()), width, height)

def display_image(filename):
    pass

#Private functions
def _read_image(filename):
    image_path = f"input/{filename}"
    image = Image.open(image_path).convert('RGBA')
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

            if top_pixel[0] == 25 and top_pixel[1] == 255 and top_pixel[2] == 255:
                print(top_pixel)

            if bottom_pixel[0] == 255 and bottom_pixel[1] == 255 and bottom_pixel[2] == 255:
                print(bottom_pixel)

            if bottom_pixel[3] < 10 and top_pixel[3] < 10:
                writer.write_empty()
            elif bottom_pixel[3] < 10:
                writer.write_one_pixel(top_pixel, TOP_PIXEL)
            elif top_pixel[3] < 10:
                writer.write_one_pixel(bottom_pixel, BOTTOM_PIXEL)
            else:
                writer.write_both_pixels(top_pixel, bottom_pixel, TOP_PIXEL)
        writer.write_new_line()


