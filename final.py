#pip install pytesseract
#pip install opencv-python
import cv2  
import numpy as np 
from pytesseract import Output
import pytesseract
import cv2

img = cv2.imread('img1.jpg')
mask = cv2.threshold(img, 120,250, cv2.THRESH_BINARY_INV)[1][:,:,0]
dst = cv2.inpaint(img, mask, 20, cv2.INPAINT_TELEA)

rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
results = pytesseract.image_to_data(rgb, output_type=Output.DICT)
cord = []
for i in range(0, len(results["text"])):

    x = results["left"][i]
    y = results["top"][i]
    w = results["width"][i]
    h = results["height"][i]
    text = results["text"][i]
    conf = int(results["conf"][i])
    
    if conf > .3:
        # text = "".join([c if ord(c) < 128 else "" for c in text]).strip()
        cv2.rectangle(dst, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cord.append([x,y,w,h])
    
print(cord)

cv2.imshow('image', dst)  


if cv2.waitKey(0) & 0xff == 27:  
    cv2.destroyAllWindows()  

