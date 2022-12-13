# Import required packages
import re
import os
import cv2
import pytesseract

# Loop through the identified contours and write text to string
def readContours(contours, img):

    im2 = img.copy()

    imStr = ""

    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        
        # Draw rectangle on copied image
        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
        # Cropping the text block for giving input to OCR
        cropped = im2[y:y + h, x:x + w]
        
        # Apply OCR on the cropped image
        imText = pytesseract.image_to_string(cropped)

        imStr += imText

    return imStr

# Set up cv2 to read text and call readContours to get string with image text
def readImg(dir, image):
    # Read image from which text needs to be extracted
    img = cv2.imread(dir+image)

    # Convert to gray scale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Perform OTSU threshold
    ret, thresh1 = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)

    # Specify structure shape and kernel size
    rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18))

    # Apply dilation on the threshold image
    dilation = cv2.dilate(thresh1, rect_kernel, iterations = 1)

    # Find contours
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,
                                                    cv2.CHAIN_APPROX_NONE)
    
    # Function call to get string from contours
    imStr = readContours(contours, img)

    return imStr

    # Format keys according to args
def formatKeys(keys, args):
    if(not args.caseSensitive):
        for i in range(len(keys)):
            keys[i] = keys[i].lower()
    return keys

# Format image text according to args
def formatStr(imStr, args):
    if(args.caseSensitive):
        return imStr
    else:
        return imStr.lower()

# search image and output results
def search(dir, keys, ukeys, args, image):
    # Loop through images in dir and check for key in imStr
    print("Scanning " + image + "...\n------------------------------------------------\n")

    # readImg uses OCR to read text on image and return string with text found
    uStr = readImg(dir, image)

    print("Raw image text content: \n\n" + uStr + "\n------------------------------------------------")
    
    # Format img text for key search
    uStr = uStr.replace("\n", " ") # remove newlines
    uStr = re.sub(' +', ' ', uStr) # remove extra spaces

    # Modify image text based on args 
    imStr = formatStr(uStr, args)
    keys = formatKeys(keys, args)

    # Search for key in text
    for i in range(len(keys)):
        if keys[i] in imStr:
            print("Found prase: '" + ukeys[i] + "' in: '" + uStr 
            + "'\nMuting image: " + image + "...\n------------------------------------------------")
            return image
        else:
            print("Couldn't find prase: '" + ukeys[i] + "' in: '" + uStr + "'...\n------------------------------------------------")
        print("Details:\nCaseSensitive = " + str(args.caseSensitive)+ "\n------------------------------------------------")
        return "NO_MUTE"