import cv2 as cv
import numpy as np

img = cv.imread('Photos/boston.jpg')

cv.imshow('Image2',img)

#Translation
def translate(img, x, y):
    transaMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transaMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotate_rotated = rotate(img, -90)

cv.imshow('Rotated Rotated', rotate_rotated)

#Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)   

#Flipping 
# 0=vertical, 1=horizontal, -1=both
flip = cv.flip(img, -1)
cv.imshow('Flip', flip)

# cv.putText(img,'Hello my name is OpenCV',(0,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)
# cv.imshow('Text',img)

#Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)