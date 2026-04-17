from PIL import Image
from argparse import ArgumentParser, Namespace
import os

from helpers import toWebp

# Creates a parser
parser = ArgumentParser()
parser.add_argument("-p", "--path", help="images path", type=str, default="./")
parser.add_argument("-q", "--quality", help="compression quality", type=int, default=80)

# run the parser
args: Namespace = parser.parse_args()

print(f"Checking folder: {args.path}")
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
                new_filename = toWebp(filename, root)
                img.save(new_filename, "WEBP", quality=args.quality)
                os.remove(filepath)
                print(f"{filename} ({width}x{height}) -> {new_filename} ({new_width}x{new_height})")
                
            img.close()
            count  += 1

        if (filename.endswith(".webp")):
            img  = Image.open(filepath)
            width,height = img.size

            if width > 1080:
                img.thumbnail((1080,1080), Image.LANCZOS)
                new_height, new_width = img.size
                img.save(filename,"WEBP", quality=args.quality)
                print(f"{filename} {width}x{height}) -> ({new_width}x{new_height})")

            img.close()
            count  += 1
        

print("--------------------------------------")
print(f"Total file resized & converted: {count}")
