import cv2 as cv 
img= cv.imread("Photos/park.jpg")
cv.imshow('Cat', img)

# Converting to grayscale
# gray =  cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow("gray cat", gray)
# Blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT) #3,3 is kernel
cv.imshow('Blur image', blur)

# Edge cascade
canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)
Canny_less_edge = cv.Canny(blur, 125, 175)
# cv.imshow("Canny Blur image", Canny_less_edge)

# Dilating the image
dilated = cv.dilate(canny, (7,7), iterations=1)
cv.imshow("Dilated", dilated)

# Erode the image
eroded = cv.erode(dilated, (3,3), iterations=5)
cv.imshow("Eroded Image", eroded)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
cv.imshow("Resized", resized)

#Cropping
cropped = img[50:200, 200:400]
cv.imshow("Cropped", cropped)

cv.waitKey(0)