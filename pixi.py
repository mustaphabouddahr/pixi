from PIL import Image
from argparse import ArgumentParser, Namespace
import os

from helpers import toWebp

# Creates a parser
parser = ArgumentParser()
parser.add_argument("-p", "--path", help="images path", type=str, default="./")

# run the parser
args: Namespace = parser.parse_args()

print(f"Checking folder: {args.path}")
print(f"Folder exists: {os.path.exists(args.path)}")
print("--------------------------------------")

count = 0

for root, dirs, files in os.walk(args.path):
    for filename in files:
        filepath = os.path.join(root, filename)
        if filename.endswith((".jpg",".jpeg",".png")):
            img = Image.open(filepath)
            width, height = img.size
            

            if width > 1080:
                img.thumbnail((1080, 1080), Image.LANCZOS)
                new_width, new_height = img.size
                new_filename = toWebp(filename)
                img.save(new_filename, "WEBP", quality=80)
                print(f"Resized: {filename} ({width}x{height}) -> {new_filename} ({new_width}x{new_height})")
                count  += 1
            img.close()

        elif (filename.endswith(".webp")):
            img  = Image.open(filepath)
            width,height = img.size

            if width > 1080:
                img.thumbnail((1080,1080), Image.LANCZOS)
                new_height, new_width = img.size
                img.save(filename,"WEBP", qualiy=80)
                print(f"Resized: {filename} {width}x{height}) -> ({new_width}x{new_height})")

            img.close()

print("--------------------------------------")
print(f"Total file resized & converted: {count}")
