import cv2
import numpy as np
image=cv2.imread('./Assignment 1/MR.pgm',0)
image=cv2.resize(image,(512,512))
height=image.shape[0]
width=image.shape[1]
image2=np.ones((int(height/2),int(width/2)),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        if(i%2==0):
            if(j%2==0):
                image2[int(i/2)][int(j/2)]=image[i][j]
cv2.imshow('Orignal Image',image)
cv2.imshow('Sub Sampled Image',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()