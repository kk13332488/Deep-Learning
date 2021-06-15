import numpy as np
import cv2

def ShowVideo():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패.')
        return

    ret = cap.set(3,480) #3 : width
    ret = cap.set(4,320) #4 : height

    while True:
        ret, frame = cap.read() #if frame was read without problem, ret value would be 1(True)
        #frame reading check
        if not ret:
            print('비디오 읽기 오류')
            break
        #turn frame into Gray
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('video', gray)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            break
    #Release cap.Videocapture() object the end of project
    cap.release()
    cv2.destroyAllWindows()

ShowVideo()