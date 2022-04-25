import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("Photos/cats 2.jpg")
cv.imshow("cats",img)

#gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
#cv.imshow("gray",gray)

blank = np.zeros(img.shape[:2],dtype="uint8")
circle =cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)

mask = cv.bitwise_and(img,img,mask=circle)
cv.imshow("masked",mask)
# Grayscale Histogram
#gray_hist = cv.calcHist([img],[0],mask,[256],[0,256])

#plt.figure()
#plt.title("GrayScale Histogram")
#plt.xlabel("Bins")
#plt.ylabel("# of pixels")
#plt.xlim([0,256])
#plt.plot(gray_hist)
#plt.show()

# Colour Histogram
plt.figure()
plt.title("GrayScale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
colors = ("b","g","r")
for i, col in enumerate(colors):
    hist = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()



cv.waitKey(0)

