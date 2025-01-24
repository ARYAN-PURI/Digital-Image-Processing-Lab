import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
image=cv2.imread('./Assignment 1/boats.bmp',0)
height=image.shape[0]
width=image.shape[1]
image3=np.ones((height,width),dtype=np.uint8)
image4=np.ones((height,width),dtype=np.uint8)
image5=np.ones((height,width),dtype=np.uint8)
ho3=[0]*256
ho4=[0]*256
ho5=[0]*256
hi=[0]*256
for i in range(height):
    for j in range(width):
        hi[image[i][j]]+=1
        image3[i][j]=round(48*math.pow(image[i][j],0.3))
        image4[i][j]=round(27*math.pow(image[i][j],0.4))
        image5[i][j]=round(14*math.pow(image[i][j],0.5))
        ho3[image3[i][j]]+=1
        ho4[image4[i][j]]+=1
        ho5[image5[i][j]]+=1
graph3=[0]*256
graph4=[0]*256
graph5=[0]*256
for i in range(256):
    graph3[i]=round(48*math.pow(i,0.3))
    graph4[i]=round(27*math.pow(i,0.4))
    graph5[i]=round(14*math.pow(i,0.5))
cv2.imshow('Orignal Image',image)
cv2.imshow('Power Law Transformation (b=0.3) Image',image3)
cv2.imshow('Power Law Transformation (b=0.4) Image',image4)
cv2.imshow('Power Law Transformation (b=0.5) Image',image5)
for i in range(256):
    hi[i]=hi[i]/(height*width)
    ho3[i]=ho3[i]/(height*width)
    ho4[i]=ho4[i]/(height*width)
    ho5[i]=ho5[i]/(height*width)
plt.plot(graph3,label='b=0.3')
plt.plot(graph4,label='b=0.4')
plt.plot(graph5,label='b=0.5')
plt.legend()
plt.title('\nS=c(R^b)\n')
plt.xlabel('R')
plt.ylabel('S')
plt.show()
plt.plot(hi)
plt.title('Histogram of Input')
plt.show()
plt.plot(ho3)
plt.title('Histogram of Output (b=0.3)')
plt.show()
plt.plot(ho4)
plt.title('Histogram of Output (b=0.4)')
plt.show()
plt.plot(ho5)
plt.title('Histogram of Output (b=0.5)')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()