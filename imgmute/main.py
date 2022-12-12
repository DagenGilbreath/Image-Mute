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

# Format keys
for i in range(len(keys)):
    keys[i] = keys[i].replace(" ", "").lower()

# Loop through images in dir and check for key in imStr
# TODO: Scrape images (maybe check if text is present in image before going forward)
# TODO: edit logic to account for images being continusouly pulled (pull img into /scrape, while scrape has images, delete image once found / muted)
for image in os.listdir(dir):
    print("Scanning " + image + "...\n------------------------------------------------\n")

    # readImg uses OCR to read text on image and return string with text found
    imStr = readImg(dir, image)

    print("Content: \n\n" + imStr + "\n------------------------------------------------")
    
    # Format img text for key search
    imStr = imStr.replace("\n", "").replace(" ", "").lower()

    # Search for key
    for key in keys:
        if key in imStr:
            print("Found prase: '" + key + "' in image: '" + image 
            + "'\nMuting image: " + image + "...\n------------------------------------------------")
            # TODO: Call block func?
    
    # TODO: remove / delete image from folder? 