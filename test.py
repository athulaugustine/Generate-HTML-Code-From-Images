from PIL import Image, ImageEnhance, ImageFilter
import pytesseract
#spytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\tesseract.exe'
for i in range(5):
	name="nithin"+str(i+1)+'.png'
	text = pytesseract.image_to_string(Image.open(name))
	print "Text of image "+str(i+1) 
	print(text)