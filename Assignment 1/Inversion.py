import cv2
import numpy as np
import matplotlib.pyplot as plt
image=cv2.imread('./Assignment 1/MR.pgm',0)
height=image.shape[0]
width=image.shape[1]
image2=np.ones((height,width),dtype=np.uint8)
hi=[0]*256
ho=[0]*256
for i in range(height):
    for j in range(width):
        image2[i][j]=255-image[i][j]
        hi[image[i][j]]+=1
        ho[image2[i][j]]+=1
cv2.imshow('Orignal Image',image)
cv2.imshow('Inversion Image',image2)
for i in range(256):
    hi[i]=hi[i]/(height*width)
    ho[i]=ho[i]/(height*width)
plt.plot(hi)
plt.title('Input Image Histogram')
plt.show()
plt.plot(ho)
plt.title('Output Image Histogram')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()