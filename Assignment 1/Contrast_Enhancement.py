import numpy as np
import math
import cv2
import matplotlib.pyplot as plt
image=cv2.imread('./boats.bmp',0)
height=image.shape[0]
width=image.shape[1]
image2=np.ones((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        if(image[i][j]<20):
            image2[i][j]=0
        elif(image[i][j]<200):
            image2[i][j]=round(255*((image[i][j]-20)/180))
        else:
            image2[i][j]=255
graph=[0]*256
for i in range(256):
    if(i<20):
        graph[i]=0
    elif(i<200):
        graph[i]=round(255*((i-20)/180))
    else:
        graph[i]=255
cv2.imshow('Orignal Image',image)
plt.plot(graph)
plt.show()
cv2.imshow('Contrast Enhancement Image',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()