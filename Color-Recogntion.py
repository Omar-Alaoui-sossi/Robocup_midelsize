import numpy as np
import cv2

cap = cv2.VideoCapture('assets/videoplayback.mp4')
def rescaleFrame(frame,scale=0.3):
     width=int(frame.shape[1]*scale)
     height= int(frame.shape[0]*scale)
     dimensions=(width,height)
     return cv2.resize(frame,dimensions,interpolation=cv2.INTER_AREA)
#frame_resized=rescaleFrame(frame)
#cv2.imshow('resize',frame_resized)

while True:
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
    frame_resized=rescaleFrame(frame)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv_resized=rescaleFrame(hsv)
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)
    mask_resized=rescaleFrame(mask)

    result = cv2.bitwise_and(frame, frame,mask=mask)
    result_resized=rescaleFrame(result)
    cv2.imshow('mask',mask_resized)
    cv2.imshow('hsv',hsv_resized)
    cv2.imshow('result', result_resized)
    cv2.imshow('frame',frame_resized)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
