from PIL import Image
import argparse
from image_io import create_new_sprite

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
        create_new_sprite(args.name)

if __name__ == "__main__":
    main()
