import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
image=cv2.imread('./Assignment 1/ultrasound.pgm',0)
height=image.shape[0]
width=image.shape[1]
hi=[0]*256
ho=[0]*256
image2=np.ones((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        if(image[i][j]>0):
            image2[i][j]=int(32 * math.log(image[i][j],2))
        else:
            image2[i][j]=0
        hi[image[i][j]]+=1
        ho[image2[i][j]]+=1
graph=[0]*256
for i in range(256):
    graph[i]=int(32 * math.log(i+1,2))
cv2.imshow('Orignal Image',image)
cv2.imshow('Log Transformation Image',image2)
for i in range(256):
    hi[i]=hi[i]/(height*width)
    ho[i]=ho[i]/(height*width)
plt.plot(graph)
plt.title('\nS=clog(1+R)\n')
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