import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("cats",img)

average = cv.blur(img,(3,3))
cv.imshow("Average Blur",average)

# gaussian blur
gauss = cv.GaussianBlur(img,(3,3),3)
cv.imshow("Gaussian Blur",gauss)

# median blur
median = cv.medianBlur(img,3)
cv.imshow("Median",median)

# Bilateral
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow("Bilateral",bilateral)





cv.waitKey(0)