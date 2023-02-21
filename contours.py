import cv2 as cv

img = cv.imread('Photos/boston.jpg')

cv.imshow('Boston', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

canny = cv.Canny(img, 125, 175)
cv.imshow('Canney', canny)

#cv.RETR_LIST = all contours, 
# cv.RETR_EXTERNAL = external contours, 
# cv.RETR_TREE = contours with hierarchies,  
# cv.RETR_CCOMP = contours with hierarchies, 
# cv.CHAIN_APPROX_NONE = all contours, 
# cv.CHAIN_APPROX_SIMPLE = compresses horizontal, vertical, and diagonal segments and leaves only their end points

contours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)

cv.waitKey(0)