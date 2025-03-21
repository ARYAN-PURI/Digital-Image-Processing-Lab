import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel('./Assignment 3/data.xlsx')
img=cv2.imread('./Assignment 3/img2.jpeg',1)

rhist=[0]*256
bhist=[0]*256
ghist=[0]*256
rows,cols,channel=img.shape

for i in range(rows):
    for j in range(cols):
        rhist[img[i][j][2]]+=1
        ghist[img[i][j][1]]+=1
        bhist[img[i][j][0]]+=1

for i in range(256):
    rhist[i]/=rows*cols
    ghist[i]/=rows*cols
    bhist[i]/=rows*cols

def equalizemapping(hist):
    map=[0]*256
    map[0]=255*hist[0]
    for i in range(1,256):
        map[i]=map[i-1] + 255*hist[i]
    for i in range(256):
        map[i]=round(map[i])
    return map

rdesiredhist=np.append(np.array(data[0]),0.001902202)
gdesiredhist=np.append(np.array(data[0]),0.003913796)
bdesiredhist=np.append(np.array(data[0]),0.002820014)
rs=equalizemapping(rhist)
gs=equalizemapping(ghist)
bs=equalizemapping(bhist)
rz=equalizemapping(rdesiredhist)
gz=equalizemapping(gdesiredhist)
bz=equalizemapping(bdesiredhist)

def givemapping(s,z):
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
    return mapping

rmapping=givemapping(rs,rz)
gmapping=givemapping(gs,gz)
bmapping=givemapping(bs,bz)

rnewhist=[0]*256
gnewhist=[0]*256
bnewhist=[0]*256
newimg=img.copy()

for i in range(rows):
    for j in range(cols):
        newimg[i][j][2]=rmapping[img[i][j][2]]
        newimg[i][j][1]=gmapping[img[i][j][1]]
        newimg[i][j][0]=bmapping[img[i][j][0]]
        rnewhist[newimg[i][j][2]]+=1
        gnewhist[newimg[i][j][1]]+=1
        bnewhist[newimg[i][j][0]]+=1

for i in range(256):
    rnewhist[i]/=rows*cols
    gnewhist[i]/=rows*cols
    bnewhist[i]/=rows*cols

rans=0
gans=0
bans=0
for i in range(256):
    rans=rans+pow(rdesiredhist[i]-rnewhist[i],2)
    gans=gans+pow(gdesiredhist[i]-gnewhist[i],2)
    bans=bans+pow(bdesiredhist[i]-bnewhist[i],2)

rans=pow(rans,0.5)
gans=pow(gans,0.5)
bans=pow(bans,0.5)
print('The Euclidean distance between two R Channel histograms is:',rans)
print('The Euclidean distance between two G Channel histograms is:',gans)
print('The Euclidean distance between two B Channel histograms is:',bans)
histograms=[rhist,rdesiredhist,rnewhist,ghist,gdesiredhist,gnewhist,bhist,bdesiredhist,bnewhist]
titles=['Input Image Histogram R Channel','Desired Histrogram R Channel','Output Image Histogram R Channel','Input Image Histogram G Channel','Desired Histrogram G Channel','Output Image Histogram G Channel','Input Image Histogram B Channel','Desired Histrogram B Channel','Output Image Histogram B Channel']
for i in range(9):
    j=i+1
    if(j>=4):
        j+=3
    if(j>=10):
        j+=3
    plt.subplot(5,3,j)
    plt.plot(histograms[i])
    plt.title(titles[i])
plt.show()
cv2.imshow('Input Image',img)
cv2.imshow('Output Image',newimg)
cv2.waitKey(0)
cv2.destroyAllWindows()