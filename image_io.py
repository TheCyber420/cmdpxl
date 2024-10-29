from PIL import Image
import os


#Constants

TEXT_COLOR = "\033[38;2;{r};{g};{b}m"
BACKGROUND_COLOR = "\033[48;2;{r};{g};{b}m"
RESET = "\033[0m"

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
    image = Image.open(image_path)
    return image

def _create_image(filename, pixels, width, height):
    out = ""
    prev_text_color = ""
    prev_bg_color = ""
    for row in range(0, height, 2):
        for col in range(width):
            top_idx = row * width + col
            bottom_idx = top_idx + width

            new_pixel = ""
            new_pixel, prev_text_color, prev_bg_color = _get_pixel_output(pixels[top_idx], pixels[bottom_idx], prev_text_color, prev_bg_color)

            out += new_pixel
        out += "\n"
    
    out += RESET
    print(out)
            
def _get_pixel_output(top, bottom, prev_text_color, prev_bg_color):
    out = ""
    color = ""
    bg_color = ""

    if len(top) == 3:
        top_pixel = top + (255, 0)
        bottom_pixel = bottom + (255, 0)
    else:
        top_pixel = top
        bottom_pixel = bottom

    if top_pixel[3] == 0 and bottom_pixel[3] == 0:
        pass
    
    elif top_pixel[3] == 0:
        color = TEXT_COLOR.format(r=bottom_pixel[0], g=bottom_pixel[1], b=bottom_pixel[2])

    elif bottom_pixel[3] == 0:
        color = TEXT_COLOR.format(r=top_pixel[0], g=top_pixel[1], b=top_pixel[2])
    else:
        color = TEXT_COLOR.format(r=top_pixel[0], g=top_pixel[1], b=top_pixel[2])
        bg_color = BACKGROUND_COLOR.format(r=bottom_pixel[0], g=bottom_pixel[1], b=bottom_pixel[2])



    if top_pixel[3] == 0 and bottom_pixel[3] == 0:
        out += RESET + " "
        prev_text_color = ""
        prev_bg_color = ""
    
    elif bg_color == prev_bg_color and prev_text_color == color:
        if top_pixel[3] == 0:
            out += BOTTOM_PIXEL
        else:
            out += TOP_PIXEL
    
    elif top_pixel[3] == 0:
        out += RESET + color + BOTTOM_PIXEL
        prev_text_color = prev_text_color
        prev_bg_color = ""

    elif bottom_pixel[3] == 0:
        out += RESET + color + TOP_PIXEL
        prev_text_color = color
        prev_bg_color = ""

    else:
        if prev_text_color != color:
            out += color
            prev_text_color = color
        if prev_bg_color != bg_color:
            out += bg_color
            prev_bg_color = bg_color

        if top_pixel[3] == 0:
            out += BOTTOM_PIXEL
        else:
            out += TOP_PIXEL


    return out, prev_text_color, prev_bg_color



