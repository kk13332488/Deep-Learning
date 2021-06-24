import numpy as np
import cv2

def CorrectConcave(imgfile):
    img = cv2.imread(imgfile)
    img1 = img.copy()
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    #contours[1] is outer contour
    cnt = contours[1]
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 3)

    #checking the contour is convex hull or not.
    check = cv2.isContourConvex(cnt)

    if not check:
        #convexHull returns concave parts corrected contours
        hull = cv2.convexHull(cnt)
        cv2.drawContours(img1, [hull], 0, (0, 255, 0), 3)
        cv2.imshow('convexhull', img1)

    cv2.imshow('contour', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def CircumscribedRect(imgfile):
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[5]

    # We use boundingRect when we wanna get coordinates that are circumscribing with contour.
    x, y, w, h = cv2.boundingRect(cnt)
    #cv2.rectangle draws a rectangle.
    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 3)

    #minAreaRect is used for figuring out errected contour's coordinates, height and width of smallest rectangle with circumscribing with contour.
    rect = cv2.minAreaRect(cnt)
    #It is used for finding
    box = cv2.boxPoints(rect)
    box = np.int0(box)

    print(box)
    cv2.drawContours(img, [box], 0, (0, 255, 0), 3)

    cv2.imshow('rectangle', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def CircumscribedCircle(imgfile):
    img = cv2.imread('pic/lightening.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = img.shape[:2]

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[5]

    # Drwaing Enclosing circle
    # the return value(coordinates) are float type. Turn it in to int type.
    (x, y), r = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    r = int(r)

    cv2.circle(img, center, r, (255, 0, 0), 3)

    cv2.imshow('fitting', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def CircumscribedEllipse(imgfile):
    img = cv2.imread('pic/lightening.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = img.shape[:2]

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[5]

    ellipse = cv2.fitEllipse(cnt)
    cv2.ellipse(img, ellipse, (0, 255, 0), 3)

    cv2.imshow('fitting', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Fitline(imgfile):
    img = cv2.imread('pic/lightening.jpg')
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    rows, cols = img.shape[:2]

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[5]

    # Drwaing Enclosing circle
    # the return value(coordinates) are float type. Turn it in to int type.
    (x, y), r = cv2.minEnclosingCircle(cnt)
    center = (int(x), int(y))
    r = int(r)

    cv2.circle(img, center, r, (255, 0, 0), 3)

    cv2.imshow('fitting', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
