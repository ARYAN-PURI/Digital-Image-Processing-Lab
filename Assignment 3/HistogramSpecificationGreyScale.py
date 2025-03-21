import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('./Assignment 3/data.xlsx')
img=cv2.imread('./Assignment 3/img.ppm',0)

hist=[0]*256
rows,cols=img.shape

for i in range(rows):
    for j in range(cols):
        hist[img[i][j]]+=1

for i in range(256):
    hist[i]/=rows*cols

def equalizemapping(hist):
    map=[0]*256
    map[0]=255*hist[0]
    for i in range(1,256):
        map[i]=map[i-1] + 255*hist[i]
    for i in range(256):
        map[i]=round(map[i])
    return map

desiredhist=np.append(np.array(data[0]),0.001902202)
s=equalizemapping(hist)
z=equalizemapping(desiredhist)

mapping=[0]*256
for i in range(256):
    j=0
    while(j<256):
        if(s[i]==z[j]):
            mapping[i]=j
            break
        if(z[j]>s[i]):
            if((z[j]-s[i])>(s[i]-z[j-1])):
                mapping[i]=j-1
            else:
                mapping[i]=j
            break
        j=j+1

newhist=[0]*256
newimg=img.copy()
for i in range(rows):
    for j in range(cols):
        newimg[i][j]=mapping[img[i][j]]
        newhist[newimg[i][j]]+=1

for i in range(256):
    newhist[i]/=rows*cols

ans=0
for i in range(256):
    ans=ans+pow(desiredhist[i]-newhist[i],2)

ans=pow(ans,0.5)
print('The Euclidean distance between two histograms is:',ans)
histograms=[hist,desiredhist,newhist]
titles=['Input Image Histogram','Desired Histrogram','Output Image Histogram']
for i in range(3):
    plt.subplot(1,3,i+1)
    plt.plot(histograms[i])
    plt.title(titles[i])
plt.show()
cv2.imshow('Input Image',img)
cv2.imshow('Output Image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()


