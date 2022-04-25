import cv2 as cv

img = cv.imread("photos/cats.jpg")
cv.imshow("cats",img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)

# simple thresholding
threshold,thresh =cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("simple threshold",thresh)

# simple thresholding inverse
threshold,thresh_inv =cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("simple threshold Inverse",thresh_inv)

# adaptive thresholding

adaptive = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,5,11)
cv.imshow("adaptive thresholding",adaptive)

cv.waitKey(0)