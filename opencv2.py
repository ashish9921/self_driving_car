import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image):
    gray = cv2.cvtColor(image_le, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny
def display_line(image,line):
    line_im=np.zeros_like(image)
    if lines is not None:
        for line in lines:
            x1,y1,x2,y2=line.reshape(4)
            cv2.line(line_im,(x1,y1),(x2,y2),(255,0,0),10)
    return line_im


def region_of_in(image):
    height=image.shape[0]
    traingle = np.array([
        [(200,height),(1100,height),(550,250)]
         ])
    mask=np.zeros_like(image)
    cv2.fillPoly(mask,traingle,255)
    masked_image=cv2.bitwise_and(image,mask)

    return masked_image

image=cv2.imread("test_image.jpg")
image_le= np.copy(image)
canny=canny(image_le)
cropped_im=region_of_in(canny)
lines=cv2.HoughLinesP(cropped_im,2,np.pi/180, 100,np.array([]),minLineLength=40,maxLineGap=5)
line_im=display_line(image_le,lines)
combo=cv2.addWeighted(image_le,0.8,line_im,1,1)
cv2.imshow("resum",combo)
cv2.waitKey(0)