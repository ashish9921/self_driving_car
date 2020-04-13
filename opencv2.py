import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image_le, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_in(image):
    height=image.shape[0]
    traingle = np.array([
        [(200,height),(1100,height),(550,250)]
         ])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,traingle,255)
    return mask

image=cv2.imread("test_image.jpg")
image_le= np.copy(image)
canny=canny(image_le)
cv2.imshow("resum",region_of_in(canny) )
cv2.waitKey(0)