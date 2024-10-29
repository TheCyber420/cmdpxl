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
    image = Image.open(image_path).convert('RGBA')
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

    filename_out = "output/" + os.path.splitext(filename)[0] + ".txt"
    with open(filename_out, "w") as file:
        file.write(out)

    print(out)
            
def _get_pixel_output(top_pixel, bottom_pixel, prev_text_color, prev_bg_color):
    out = ""
    if top_pixel[3] == 0 and bottom_pixel[3] == 0:
        if prev_bg_color == "" and prev_text_color == "":
            out += " "
        else:
            prev_text_color = ""
            prev_bg_color = ""
            out += RESET + " "

    elif top_pixel[3] == 0:
        if prev_bg_color == "":
            color = TEXT_COLOR.format(r=bottom_pixel[0], g=bottom_pixel[1], b=bottom_pixel[2])
            if color == prev_text_color:
                out += BOTTOM_PIXEL
            else:
                out += color + BOTTOM_PIXEL
                prev_text_color = color
        else:
            out += RESET
            color = TEXT_COLOR.format(r=bottom_pixel[0], g=bottom_pixel[1], b=bottom_pixel[2])
            out += color + BOTTOM_PIXEL
            if color != prev_text_color:
                prev_text_color = color

    elif bottom_pixel[3] == 0:
        if prev_bg_color == "":
            color = TEXT_COLOR.format(r=top_pixel[0], g=top_pixel[1], b=top_pixel[2])
            if color == prev_text_color:
                out += TOP_PIXEL
            else:
                out += color + TOP_PIXEL
                prev_text_color = color
        else:
            out += RESET
            color = TEXT_COLOR.format(r=top_pixel[0], g=top_pixel[1], b=top_pixel[2])
            out += color + TOP_PIXEL
            if color != prev_text_color:
                prev_text_color = color
        
    else:
        text_color = TEXT_COLOR.format(r=top_pixel[0], g=top_pixel[1], b=top_pixel[2])
        bg_color = BACKGROUND_COLOR.format(r=bottom_pixel[0], g=bottom_pixel[1], b=bottom_pixel[2])

        if text_color != prev_text_color:
            out += text_color
            prev_text_color = text_color

        if bg_color != prev_bg_color:
            out += bg_color
            prev_bg_color = bg_color

        out += TOP_PIXEL
        

    return out, prev_text_color, prev_bg_color



