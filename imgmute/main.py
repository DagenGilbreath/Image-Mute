# Import required packages
import argparse
import os
import pytesseract
import requests 
from bs4 import BeautifulSoup 
from imgOcr import search
from muter import mute

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

# TODO: Figure this shit out 
#def getdata(url): 
#    r = requests.get(url) 
#    return r.text 
    
#htmldata = getdata("") 
#soup = BeautifulSoup(htmldata, 'html.parser') 
#for item in soup.find_all('img'):
#    print(item['src'])

# Pytesseract directory from arg
pytdir = args.pytdir

# Tesseract-OCR
pytesseract.pytesseract.tesseract_cmd = pytdir

# Keys to search images for (comma separated)
keys = args.searchKeys.split(',')
# Copy list for output clarity
ukeys = args.searchKeys.split(',')

# Perform search on image (imgOcr.py)
for image in os.listdir(dir):
    result = search(dir, keys, ukeys, args, image)
    if result != "NO_MUTE":
        #TODO: implement mute func
        mute(result)