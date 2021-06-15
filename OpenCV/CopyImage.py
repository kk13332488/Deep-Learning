import numpy as np
import cv2

def CopyImage():
    imgfile = 'yuna.jpg'
    img = cv2.imread(imgfile, cv2.IMREAD_COLOR)
    cv2.imshow('model', img)

    k = cv2.waitKey(0) & 0xFF #save user's typing as k

    cnt = 2
    while cnt < 100:
        if k == 27:
            cv2.destroyAllWindows()
            break
        elif k == ord('c'):
            cv2.imwrite('yuna%d.jpg' %cnt , img)

CopyImage()
