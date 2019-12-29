from PIL import Image
import pytesseract
import sys
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
print("Please wait finding text.......................")
print(pytesseract.image_to_string(Image.open("img.png"),lang='eng'))	