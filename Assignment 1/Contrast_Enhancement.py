import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
image=cv2.imread('./Assignment 1/boats.bmp',0)
height=image.shape[0]
width=image.shape[1]
hi=[0]*256
ho=[0]*256
image2=np.ones((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        if(image[i][j]<20):
            image2[i][j]=0
        elif(image[i][j]<200):
            image2[i][j]=round(255*((image[i][j]-20)/180))
        else:
            image2[i][j]=255
        hi[image[i][j]]+=1
        ho[image2[i][j]]+=1
graph=[0]*256
for i in range(256):
    if(i<20):
        graph[i]=0
    elif(i<200):
        graph[i]=round(255*((i-20)/180))
    else:
        graph[i]=255
cv2.imshow('Orignal Image',image)
cv2.imshow('Contrast Enhancement Image',image2)
for i in range(256):
    hi[i]=hi[i]/(height*width)
    ho[i]=ho[i]/(height*width)
plt.plot(graph)
plt.title('\nS={0 if R<20;\n (R-20)/180 if 20<R<200;\n 255 if R>200}\n')
plt.xlabel('R')
plt.ylabel('S')
plt.show()
plt.plot(hi)
plt.title('Input Image Histogram')
plt.show()
plt.plot(ho)
plt.title('Output Image Histogram')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()