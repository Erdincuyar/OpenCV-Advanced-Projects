import cv2 as cv
import matplotlib.pyplot as plt


img = cv.imread("photos/cats.jpg")
cv.imshow("cats",img)

#plt.imshow(img)
#plt.show()

# BGR to Grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# BGR TO HSV
HSV = cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",HSV)

# BGR to LAB
lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)

# BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("rgb",rgb)

# HSV to BGR
Lab_bgr = cv.cvtColor(lab,cv.COLOR_LAB2BGR)
cv.imshow("LAB -----> BGR",Lab_bgr)


cv.waitKey(0)