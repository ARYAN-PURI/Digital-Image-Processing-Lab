import cv2
import numpy as np
import random
import matplotlib.pyplot as plt

img=cv2.imread('./Assignment 5/Scene.jpg',0)
rows,cols=img.shape
imgOut=np.zeros((rows,cols),dtype=np.uint8)

a=[]
for i in range(rows):
    for j in range(cols):
        a.append([i,j])

random.shuffle(a)

for i in range(0,rows*cols-1,2):
    imgOut[a[i][0]][a[i][1]]=img[a[i+1][0]][a[i+1][1]]
    imgOut[a[i+1][0]][a[i+1][1]]=img[a[i][0]][a[i][1]]
cv2.imshow('Input',img)
cv2.imshow('OutPut',imgOut)
cv2.waitKey(0)

def Ostumethod(img):
    ihist=[0]*256
    rows,cols=img.shape
    for i in range(rows):
        for j in range(cols):
            ihist[img[i][j]]+=1
    
    for i in range(256):
        ihist[i]/=(rows*cols)
    
    Mg=0
    for i in range(256):
        Mg+=(i*ihist[i])
    
    P1=[0]*256
    M=[0]*256
    
    P1[0]=ihist[0]
    M[0]=0
    Sigma2B=[0]*256
    maxk=0
    
    for k in range(1,254):
        P1[k]=P1[k-1] + ihist[k]
        M[k]=M[k-1] + ihist[k]*k
        Sigma2B[k]= (pow(P1[k]*Mg - M[k], 2) / (P1[k]*(1-P1[k])))
        if(Sigma2B[maxk]<Sigma2B[k]):
            maxk=k
    return Sigma2B

Sigma2B1=Ostumethod(img)
Sigma2B2=Ostumethod(imgOut)

plt.subplot(1,2,1)
plt.title('Variation of Sigma2B with k in Orignal Image')
plt.plot(Sigma2B1)

plt.subplot(1,2,2)
plt.title('Variation of Sigma2B with k in Randomize Image')
plt.plot(Sigma2B2)
plt.show()

cv2.destroyAllWindows()
