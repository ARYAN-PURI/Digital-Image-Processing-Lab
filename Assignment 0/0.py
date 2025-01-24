import cv2
import matplotlib.pyplot as plt
image=cv2.imread('./boats.bmp',1)
hr=[0]*256
hg=[0]*256
hb=[0]*256
rows=image.shape[0]
cols=image.shape[1]
for i in range(0,rows):
    for j in range(0,cols):
        hr[image[i][j][2]]+=1
        hg[image[i][j][1]]+=1
        hb[image[i][j][0]]+=1

plt.plot(hr)
plt.title('Red Intensity Distribution')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.show()
plt.plot(hg)
plt.title('Green Intensity Distribution')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.show()
plt.plot(hb)
plt.title('Blue Intensity Distribution')
plt.xlabel('Intensity Value')
plt.ylabel('Frequency')
plt.show()


