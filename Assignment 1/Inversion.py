import cv2
import numpy as np
image=cv2.imread('./MR.pgm',0)
height=image.shape[0]
width=image.shape[1]
print(height, width)
image2=np.ones((height,width),dtype=np.uint8)
for i in range(height):
    for j in range(width):
        image2[i][j]=255-image[i][j]
cv2.imshow('Orignal Image',image)
cv2.waitKey(0)
cv2.imshow('Inversion Image',image2)
cv2.waitKey(0)
cv2.destroyAllWindows()