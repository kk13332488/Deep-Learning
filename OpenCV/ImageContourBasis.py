import numpy as np
import cv2

def contour(imgfile):
    #Contour finding is similar to find white object at black background. So we muse use gray scale image than color image.
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    #Second parameter is contour subtracting method
    #Third parameter is contour approximation method.
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # targeted image to describe contour, contours, contour index parameter(if -1, draw all the contours, BGR, line thickness)
    cv2.drawContours(img, contours, -1, (0, 0, 255), 1)
    cv2.imshow('thresh', thr)
    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

contour('yuna.jpg')