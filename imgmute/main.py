# Import required packages
import argparse
import os
import sys
import re
import pytesseract
from imgOcr import readImg

# TODO: fix args currently not working

# Optional args
parser = argparse.ArgumentParser(
    prog = "ImageMute",
    description = "Mute images on Twitter based on text content found within",
    epilog = "Built with OpenCV and beautifulsoup"
)
parser.add_argument('-c', '--caseSensitive', help='Parse text / phrase with case sensitivity', action='store_true')
parser.add_argument('pytdir', help='The directory of Pytesseract.exe')
parser.add_argument('searchKeys', help='Phrases to search image text content for in order to mute the image. Surround each phrase in quotes and seperate with commas.')
args = parser.parse_args()

# image directory
dir = r'scrape/'

# Pytesseract directory from arg
pytdir = args.pytdir

# Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = pytdir

# Keys to search images for (comma separated)
keys = args.searchKeys.split(',')
# Copy list for output clarity
ukeys = args.searchKeys.split(',')

# Format keys according to args
def formatKeys(keys):
    if(not args.caseSensitive):
        for i in range(len(keys)):
            keys[i] = keys[i].lower()
    return keys

# Format image text according to args
def formatStr(imStr):
    if(args.caseSensitive):
        return imStr
    else:
        return imStr.lower()

# dir: pytesseract directory
# keys: search phrases specified in args
# ukeys: copy of keys that keeps format for printing
def search(dir, keys, ukeys):
    # Loop through images in dir and check for key in imStr
    for image in os.listdir(dir):
        print("Scanning " + image + "...\n------------------------------------------------\n")

        # readImg uses OCR to read text on image and return string with text found
        uStr = readImg(dir, image)

        print("Raw image text content: \n\n" + uStr + "\n------------------------------------------------")
        
        # Format img text for key search
        uStr = uStr.replace("\n", " ") # remove newlines
        uStr = re.sub(' +', ' ', uStr) # remove extra spaces

        # Modify iamge text based on args 
        imStr = formatStr(uStr)
        keys = formatKeys(keys)

        # Search for key in text
        for i in range(len(keys)):
            if keys[i] in imStr:
                print("Found prase: '" + ukeys[i] + "' in: '" + uStr 
                + "'\nMuting image: " + image + "...\n------------------------------------------------")
            else:
                print("Couldn't find prase: '" + ukeys[i] + "' in: '" + uStr + "'...\n------------------------------------------------")
            print("Details:\nCaseSensitive = " + str(args.caseSensitive)+ "\n------------------------------------------------")

search(dir, keys, ukeys)