import sys
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'tesseract'

image = cv2.imread(sys.argv[1])

image = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)

print(text)