import cv2
import pytesseract
import pyscreenshot as ImageGrab
from datetime import datetime
import os

#filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S_%f.png")
#screenshot_path = os.path.join(path, filename)

def area_screenshot(x_left,y_top,x_right,y_bottom, path):
	
  filename = datetime.now().strftime("screenshot_%Y%m%d_%H%M%S_%f.png")
  screenshot_path = os.path.join(path, filename)
  im = ImageGrab.grab(bbox=(x_left, y_top, x_right, y_bottom))
  im.save(screenshot_path)
  return filename


# (80, 280, 350,330)

## MUST BE INSTALLED TO PATH https://digi.bib.uni-mannheim.de/tesseract/tesseract-ocr-w64-setup-v5.0.0-alpha.20210506.exe ##
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def img2txt(path, filename):
# Grayscale, Gaussian blur, Otsu's threshold
  screenshot_path = os.path.join(path, filename)
  image = cv2.imread(screenshot_path)
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  blur = cv2.GaussianBlur(gray, (3,3), 0)
  thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

  # Morph open to remove noise and invert image
  kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
  opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=0)
  invert = 255 - opening

  # Perform text extraction
  text = pytesseract.image_to_string(invert, lang='eng', config='--psm 6')
  text = text.split()
  text = " ".join(text)
  text = text.replace('8', 'B').replace('JINSE]','JINSEI').replace('JINSEL','JINSEI').replace('lin','Im').replace('lt','li')
  #print(text)
#  cv2.imshow('thresh', thresh)
#  cv2.imshow('opening', opening)
#  cv2.imshow('invert', invert)
#  cv2.waitKey()  
  return text
#doPush("title",data)



