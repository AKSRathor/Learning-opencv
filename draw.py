import cv2 as cv
import numpy as np 
# img = cv.imread("Photos/cat.jpg")
blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1) Paint the image a certain color
# blank[:] = 0,255,0
# cv.imshow('Green', blank)

# 2) Draw a rectangle
# cv.rectangle(blank, (0,0), (250, 250), (0, 255, 0), thickness=2)
# cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0, 255, 0), thickness= cv.FILLED) #same for -1 as thickness
# cv.imshow("Rectangle", blank)

# 3) Draw a circle

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=3) #midpoint 250,250 = shape//2, radius = 40, (0,0,255) = color(red)
cv.imshow('Circle', blank)

# 4) Draw a line
cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3) #start from (0,0), to (250,250), color = white
cv.imshow("line", blank)

# 5) Write text on a image
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,255,0), 2) #text, font-position, font-family, font-scale, font-color, font-thickness
cv.imshow('Text', blank)

cv.waitKey(0)
