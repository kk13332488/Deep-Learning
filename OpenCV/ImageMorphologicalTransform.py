import numpy as np
import cv2

def Morph(imgfile):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    #The more big the kernel size, erosion or dilation will be more effective.
    kernel = np.ones((3, 3), np.uint8)

    #The more iterations we repeat, erosion or dilation will be more effective.
    erosion = cv2.erode(img, kernel, iterations = 1)
    dilation = cv2.dilate(img, kernel, iterations = 1)

    cv2.imshow('original', img)
    cv2.imshow('erosion', erosion)
    cv2.imshow('dilation', dilation)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Recovering(imgfile):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    kernel = np.ones((5,5), np.uint8)

    #opening = do erosion then dilation
    #closing = do dilation then erosion
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
    gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)

    cv2.imshow('opening', opening)
    cv2.imshow('closing', closing)
    cv2.imshow('gradient', gradient)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def makeKernel():
    #fill all the element for 1
    M1 = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
    #fill all the element like epllipse
    M2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    #fill all the element like cross
    M3 = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))

    print(M1)
    print(M2)
    print(M3)

makeKernel()