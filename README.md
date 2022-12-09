# Image Muter for Twitter

Python script to mute images on Twitter based on text content in the image using Tessaract OCR. Currently Windows only. 

DIRECTIONS:
- Install [Tessaract OCR](https://github.com/UB-Mannheim/tesseract/](https://github.com/UB-Mannheim/tesseract/wiki) 

- Run main.py with the directory of your tesseract.exe and the phrases you wish to mute (comma separated)
  - EX) python main.py C:/Users/name/AppData/Local/Tesseract-OCR/tesseract.exe "annoying phrase","another phrase"
