import numpy as np
import cv2
import math
import matplotlib.pyplot as plt
image=cv2.imread('./boats.bmp',0)
height=image.shape[0]
width=image.shape[1]
image2=np.ones((height,width),dtype=np.uint8)
ho=[0]*256
hi=[0]*256
for i in range(height):
    for j in range(width):
        hi[image[i][j]]+=1
        image2[i][j]=round(48*math.pow(image[i][j],0.3))
        ho[image2[i][j]]+=1
graph=[0]*256
for i in range(256):
    graph[i]=round(48*math.pow(i,0.3))
cv2.imshow('Orignal Image',image)
plt.plot(graph)
plt.show()
cv2.imshow('Power Law (0.5) Transformation Image',image2)
plt.plot(hi)
plt.title('Histogram of Input')
plt.show()
plt.plot(ho)
plt.title('Histogram of Output')
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()