#from PIL import Image
#im = Image.open("bride.jpg")
#im.rotate(45).show()
#print(im.format, im.size, im.mode)

from PIL import Image
from PIL import ImageFilter
import pytesseract
imageObject=Image.open('2012100516042359.png');
imfilter = imageObject.filter(ImageFilter.GaussianBlur)
imfilter.show()
'''
print (imageObject);
print (pytesseract.image_to_string(imageObject))
'''
