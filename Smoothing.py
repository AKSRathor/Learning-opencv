# Blurring Technique
import cv2 as cv
img  = cv.imread("Photos/cats.jpg")
# cv.imshow("Cats", img)

# Averaging
average = cv.blur(img, (7,7))
cv.imshow("Blur", average)

# Guassian Blur
gauss = cv.GaussianBlur(img, (99,99), 0)
print(gauss)
cv.imshow("Gaussian Blur", gauss)

# Median Blur

median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

bilateral = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral', bilateral)

cv.waitKey(0)