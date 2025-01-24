import cv2
import numpy as np
import math
import matplotlib.pyplot as plt
image=cv2.imread('./ultrasound.pgm',0)
height=image.shape[0]
width=image.shape[1]
image2=np.ones((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        if(image[i][j]>0):
            image2[i][j]=int(32 * math.log(image[i][j],2))
        else:
            image2[i][j]=0
graph=[0]*256
for i in range(256):
    graph[i]=int(32 * math.log(i+1,2))
cv2.imshow('Orignal Image',image)
cv2.imshow('Log Transformation Image',image2)
plt.plot(graph)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()