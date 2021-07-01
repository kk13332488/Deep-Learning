import numpy as np
import cv2

def tmpMatching(TargetIMG,imgfile, thr):
    img=cv2.imread(TargetIMG)
    imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    template=cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    w, h=template.shape[::-1]

    res=cv2.matchTemplate(imgray, template, cv2.TM_CCOEFF_NORMED)

    #locations which values are bigger than threshold.
    loc=np.where(res>=thr)

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img,pt,(pt[0]+w, pt[1]+h), (0,0,255), 2)

    cv2.imshow('res', res)
    cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

tmpMatching('pic/neoguri.jpg', 'pic/carrot.jpg', 0.8)
