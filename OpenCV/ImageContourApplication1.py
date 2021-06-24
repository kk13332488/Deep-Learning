import numpy as np
import cv2

def Centroid(imgfile):
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    contour = contours[0]
    mmt = cv2.moments(contour)

    for key, val in mmt.items():
        print('%s:\t%.5f' %(key, val))

    #cx, cy is centroid (x, y) coordinates.
    cx = int(mmt['m10']/mmt['m00'])
    cy = int(mmt['m01']/mmt['m00'])
    print(cx, cy)

def contour(imgfile):
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[90]
    #contourArea returns contour area
    area = cv2.contourArea(cnt)
    #arcLength returns Contour perimeter
    perimeter = cv2.arcLength(cnt, True)

    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 1)

    print('contour 면적: ', area)
    print('contour 길이: ', perimeter)

    cv2.imshow('contour', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ContourApproximation(imgfile):
    img = cv2.imread(imgfile)
    img1 = cv2.imread(imgfile)
    img2 = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (255, 255, 0), 3)

    # arcLength returns perimeter length of a contour.
    # if parameter is True, closed curve. if False, Opened curve
    epsilon1 = 0.01 * cv2.arcLength(cnt, True) # 1% of original contour length
    epsilon2 = 0.1 * cv2.arcLength(cnt, True) # 10% of original contour length

    # approxPolyDP function reduces the vertexes to make approximated contour from original contour
    approx1 = cv2.approxPolyDP(cnt, epsilon1, True)
    approx2 = cv2.approxPolyDP(cnt, epsilon2, True)

    cv2.drawContours(img1, [approx1], 0, (0, 255, 0), 3)
    cv2.drawContours(img2, [approx2], 0, (0, 255, 0), 3)

    cv2.imshow('contour', img)
    cv2.imshow('Approx1', img1)
    cv2.imshow('Approx2', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

