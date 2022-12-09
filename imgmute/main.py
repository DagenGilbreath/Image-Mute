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

# Pytesseract directory from arg
pytdir = sys.argv[1]
print(pytdir)

# Tesseract-OCR
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dgilbreath\AppData\Local\Tesseract-OCR\tesseract.exe'
pytesseract.pytesseract.tesseract_cmd = pytdir

# image directory
dir = r'scrape/'

# Key to search image text
key = "Text"

# Remove white space (simplify formatting)
key = key.replace(" ", "").lower()

# TODO: Scrape images (maybe check if text is present at all before going forward)

# TODO: use while loop once images are being continusouly pulled
for image in os.listdir(dir):
    # readImg uses OCR to read text on image and return string with text found (no spaces lowercase)
    s = readImg(dir, image)
    
    # Search for key
    if key in s:
        print("found!")
        
        # TODO: Call block func?
    
    # TODO: remove / delete image from folder? 