import numpy as np
import cv2

def Bluring(imgfile):
    img = cv2.imread(imgfile)

    kernel = np.ones((5, 5), np.float32)/25
    blurredImg = cv2.filter2D(img, -1, kernel)

    cv2.imshow('original', img)
    cv2.imshow('blur', blurredImg)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def onMouse(x):
    pass

def bluring(imgfile):
    img = cv2.imread(imgfile)

    cv2.namedWindow('Blur pane')
    cv2.createTrackbar('Blur mode', 'Blur pane', 0, 2, onMouse)
    cv2.createTrackbar('Blur', 'Blur pane', 0, 5, onMouse)

    mode = cv2.getTrackbarPos('Blur mode', 'Blur pane')
    val = cv2.getTrackbarPos('Blur', 'Blur pane')

    while True:
        #Transform val to odd number(0,1,2... to 1,3,5...)
        val = val * 2 + 1

        try:
            if mode == 0:
                blur = cv2.blur(img, (val, val))
            elif mode == 1:
                #GaussianBlur is preferred to gaussian noise image
                #GaussianBlur is depended to nearby pixels
                blur = cv2.GaussianBlur(img, (val, val), 0)
            elif mode == 2:
                #medianBlur is preferred to salt-pepper noise image
                blur = cv2.medianBlur(img, val)
            else:
                break
            cv2.imshow('Blur pane', blur)
        except:
            break

        k = cv2.waitKey(0) & 0xFF
        if k == 27:
            break

        mode = cv2.getTrackbarPos('Blur_mode', 'Blurpane')
        val = cv2.getTrackbarPos('Blur', 'Blurpane')

    cv2.destroyAllWindows()

bluring('yuna.jpg')
