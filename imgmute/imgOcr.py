# Import required packages
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