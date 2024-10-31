from PIL import Image
from pathlib import Path
from image_io import create_new_sprite, display_image
import argparse
import os

def main(): 

    parser = argparse.ArgumentParser(
        description="CLI utility to convert images into pixel-art",
        prog="cmdpxl",
        usage="cmdpxl [OPTION] [IMAGE NAME]",
        add_help=False
    )

    parser.add_argument(
        "-h",
        "--help",
        action="help",
        help="Show this help message and exit"
    )

    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Name of the image you want to display"
    )

    parser.add_argument(
        "-a",
        "--add",
        type=str,
        help="Converts an image to ascii format and saves it to be displayed later"
    )

    parser.add_argument(
        "-l",
        "--list",
        help="List the names of the images available for output"
    )

    args = parser.parse_args()


    if args.name:
        image_path = "output/" + args.name + ".txt"
        display_image(image_path)
        pass
    
    if args.add:
        #create_new_sprite(args.add)
        full_path = Path(args.add).resolve()

        print(full_path)
        if not full_path.is_file():
            print(f"An error has occured\nFile {args.add} not found")
        else:
            create_new_sprite(full_path)


if __name__ == "__main__":
    main()
