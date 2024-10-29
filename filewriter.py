from pathlib import Path

#Constants

TEXT_COLOR = "\033[38;2;{r};{g};{b}m"
BACKGROUND_COLOR = "\033[48;2;{r};{g};{b}m"
RESET = "\033[0m"

class Filewriter:
    prev_bg_color = ""
    prev_text_color = ""
    def __init__(self, filename) -> None:
        new_filename = "output/" + Path(filename).stem + ".txt"
        self.filename = new_filename
        with open(new_filename, "w"):
            pass

    def write_empty(self):
        with open(self.filename, "a") as file:
            if self.prev_bg_color != "" or self.prev_text_color != "":
                file.write(RESET + " ")
                self.prev_bg_color = ""
                self.prev_text_color = ""
            else:
                file.write(" ")

    def write_one_pixel(self, color, pixel):
        with open(self.filename, "a") as file:
            if self.prev_bg_color != "":
                file.write(RESET)
                self.prev_bg_color = ""
                self.prev_text_color = ""
            
            new_color = TEXT_COLOR.format(r=color[0], g=color[1], b=color[2])

            if new_color != self.prev_text_color:
                file.write(new_color)
                self.prev_text_color = new_color
            
            file.write(pixel)

    def write_both_pixels(self, top_color, bottom_color, pixel):
        with open(self.filename, "a") as file:
            top_color_str = TEXT_COLOR.format(r=top_color[0], g=top_color[1], b=top_color[2])
            bot_color_str = BACKGROUND_COLOR.format(r=bottom_color[0], g=bottom_color[1], b=bottom_color[2])
            
            if top_color_str != self.prev_text_color:
                self.prev_text_color = top_color_str
                file.write(top_color_str)
            
            if bot_color_str != self.prev_bg_color:
                self.prev_bg_color = bot_color_str
                file.write(bot_color_str)

            file.write(pixel)

    def write_new_line(self):
        with open(self.filename, "a") as file:
            file.write("\n")