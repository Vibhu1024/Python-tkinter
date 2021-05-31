import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
img = Image.open("C:\\Users\\HP\\PycharmProjects\\pythonProject\\download.png")
text = tess.image_to_string(img)
print(text)