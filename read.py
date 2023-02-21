import cv2 as cv

#img = cv.imread('Photos\image5.png')
#cv.imshow('Image', img)

#reading videos

capture = cv.VideoCapture('D:/OPENCV/Videos/video6.mp4')

while True: 
    isTrue, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()

cv.waitKey(0)
