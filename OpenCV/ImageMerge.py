import numpy as np
import cv2

def addImage(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    img1 = img1[:701, :, :]

    cv2.imshow('img1', img1)
    cv2.imshow('img2', img2)

    #just add pixel value
    add_img1 = img1 + img2
    #add pixel value but, if the value is over 255 all the value are limited to 255
    add_img2 = cv2.add(img1, img2)

    cv2.imshow('img1 + img2', add_img1)
    cv2.imshow('add(img1, img2)', add_img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def onMouse(x):
    pass

def imgBlending(imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    img1 = img1[:701, :, :]

    cv2.namedWindow('ImgPane')
    cv2.createTrackbar('Mixing', 'ImgPane', 0, 100, onMouse)
    mix = cv2.getTrackbarPos('Mixing', 'ImgPane')

    while True:
        img = cv2.addWeighted(img1, float(100-mix)/100, img2, float(mix)/100, 0)
        cv2.imshow('imgPane', img)

        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break

        mix = cv2.getTrackbarPos('Mixing', 'ImgPane')
    cv2.destroyAllWindows()

def bitOperation(hpos, vpos, imgfile1, imgfile2):
    img1 = cv2.imread(imgfile1)
    img2 = cv2.imread(imgfile2)

    rows, cols, channels = img2.shape
    roi = img1[vpos:rows+vpos, hpos:cols+hpos]

    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    img1_bg = cv2.bitwise_and(roi, roi, mask = mask_inv)

    img2_fg = cv2.bitwise_and(img2, img2, mask = mask)

    #dst will be black-removed image from img1
    dst = cv2.add(img1_bg, img2_fg)
    img1[vpos:rows+vpos, hpos:cols+hpos] = dst

    cv2.imshow('result', img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

bitOperation(10, 10, 'yuna.jpg', 'logo.jpg')

