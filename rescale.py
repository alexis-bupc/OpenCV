import cv2 as cv

#reading images

img = cv.imread('Photos\image2.jpg')
cv.imshow('Image',img)

#rescale
def rescaleFrame(frame, scale=0.75):
    #Images, Videos, Live Video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width,height)

    return cv.resize(frame, dimensions,interpolation=cv.INTER_AREA)

resized_image = rescaleFrame(img)
cv.imshow('Image', resized_image)

#capture.set

def changeRes(width, height):
    #Live video or WEBCAM
    capture.set(3,width)
    capture.set(4,height)

#reading videos

capture = cv.VideoCapture('Videos/video6.mp4')

while True: 
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame) 

    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()         
cv.waitKey(0)
