import cv2
import matplotlib.pyplot as plt
import numpy as np

imgInput=cv2.imread('./Assignment 2/image.png',0)
rows,cols=imgInput.shape

ihist=[0]*256
for i in range(rows):
    for j in range(cols):
        ihist[imgInput[i][j]]+=1

for i in range(256):
    ihist[i]/=(rows*cols)

trns=[0]*256
trns[0]=255*ihist[0]
for i in range(1,256):
    trns[i]=trns[i-1]+255*ihist[i]

imgOutput=np.zeros((rows,cols),dtype=np.uint8)
ohist=[0]*256
for i in range(rows):
    for j in range(cols):
        imgOutput[i][j]=round(trns[imgInput[i][j]])
        ohist[imgOutput[i][j]]+=1

for i in range(256):
    ohist[i]/=(rows*cols)

plt.plot(ihist)
plt.title('Histogram of Input Image')
plt.show()
plt.plot(ohist)
plt.title('Histogram of Output Image')
plt.show()
cv2.imshow('ImageInput',imgInput)
cv2.imshow('ImageOutput',imgOutput)
cv2.waitKey(0)
cv2.destroyAllWindows()