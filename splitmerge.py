import cv2 as cv
import numpy as np

img = cv.imshow("Photos/park.jpg")
cv.imshow("park",img)

blank = np.zeros(img.shape [:2],dtype="uint8")
blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])


b, g, r = cv.split(img)

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b, g, r])
cv.imshow("Merged İmage",merged)

cv.waitKey(0)
