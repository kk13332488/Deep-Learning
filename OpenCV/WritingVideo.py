import numpy as np
import cv2

def WriteVideo():
    try:
        print('카메라를 구동합니다.')
        cap = cv2.VideoCapture(0)
    except:
        print('카메라 구동 실패')
        return
    fps = 20.0
    width = int(cap.get(3))
    height = int(cap.get(4))
    fcc = cv2.VideoWriter_fourcc('D', 'I', 'V', 'X')

    out = cv2.VideoWriter('mycam.avi', fcc, fps, (width, height))
    print('녹화를 시작합니다')

    while True:
        ret, frame = cap.read()

        if not ret:
            print('비디오 읽기 오류')
            return
        cv2.imshow('video', frame)
        out.write(frame)

        k = cv2.waitKey(1) & 0xFF
        if k == 27:
            print('녹화를 종료합니다')
            break
    cap.release()
    out.release()
    cv2.destroyAllWindows()

WriteVideo()
