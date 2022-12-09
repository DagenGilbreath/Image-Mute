# scrape images on timeline
# search for text in key on image
# "im not interested in this tweet" - mutes tweet (hopefully before you see it)
# TODO: Loop as long as session is open
# TODO: integrate twitter API?
# TODO: flesh out

# Import required packages
import os
import sys
from imgOcr import readImg
import pytesseract

# image directory
dir = r'scrape/'

# Pytesseract directory from arg
pytdir = sys.argv[1]

# Keys to search images for (comma separated)
keys = sys.argv[2].split(',')

# Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = pytdir

# Simplify keys to search image text
for i in range(len(keys)):
    keys[i] = keys[i].replace(" ", "").lower()

# Loop through images in dir and check for key in imStr
# TODO: Scrape images (maybe check if text is present in image before going forward)
# TODO: edit logic to account for images being continusouly pulled (pull img into /scrape, while scrape has images, delete image once found / muted)
for image in os.listdir(dir):
    # readImg uses OCR to read text on image and return string with text found (no spaces lowercase)
    imStr = readImg(dir, image)
    
    # Search for key
    for key in keys:
        if key in imStr:
            print("found key '" + key + "' in text '" + imStr +"'")
            print("muting image " + image + "...")
            # TODO: Call block func?
    
    # TODO: remove / delete image from folder? 