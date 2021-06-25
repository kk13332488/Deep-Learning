import numpy as np
import cv2

def FindConcave(imgfile):
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]

    hull = cv2.convexHull(cnt)
    cv2.drawContours(img, [hull], 0, (0, 0, 255), 2)

    # coordinates of points which convex hull and original contour contacts.
    hull = cv2.convexHull(cnt, returnPoints=False)
    # Function below returns 4 values.
    # 1. start index of Convex hull
    # 2. Index of next connecting part for compose convex hull
    # 3. The index on the contour that is farthest from the straight line that connects the start index and the junction index
    # 4. Approximate distance to farthest point
    defects = cv2.convexityDefects(cnt, hull)

    for i in range(np.shape(defects)[0]):
        sp, ep, fp, dist = defects[i, 0]
        start_point = tuple(cnt[sp][0])
        end_point = tuple(cnt[ep][0])
        farthest_point = tuple(cnt[fp][0])

        cv2.circle(img, farthest_point, 5, (0, 255, 0), -1)
    cv2.imshow('defects', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ShortDist(imgfile):
    img = cv2.imread(imgfile)
    imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ret, thr = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cnt = contours[0]
    cv2.drawContours(img, [cnt], 0, (0, 255, 0), 2)

    outside = (55,70)
    inside = (140, 150)

    #if parameter of pointPolygonTest is True, the function returns most short distance between point and contour.
    dist1 = cv2.pointPolygonTest(cnt, outside, True)
    dist2 = cv2.pointPolygonTest(cnt, inside, True)

    print('Contour에서 (%d, %d)까지 거리: %.3f' %(outside[0], outside[1], dist1))
    print('Contour에서 (%d, %d)까지 거리: %.3f' % (inside[0], inside[1], dist1))

    cv2.circle(img, outside, 3, (0, 255, 0), -1)
    cv2.circle(img, inside, 3, (255, 0, 255), -1)

    cv2.imshow('defects', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()



def MatchShape():
    imgfile_list = ['pic/Star.jpg', 'pic/Star2.jpg', 'pic/Star3.jpg']

    wins = map(lambda x: 'img' + str(x), range(3))
    wins = list(wins)
    imgs = []
    contour_list = []

    i = 0
    for imgfile in imgfile_list:
        img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
        imgs.append(img)

        ret, thr = cv2.threshold(img, 127, 255, 0)
        contours, _ = cv2.findContours(thr, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        contour_list.append(contours[0])
        i += 1
    for i in range(2):
        cv2.imshow(wins[i+1], imgs[i+1])
        #matchshapes() function compare two polygons or contours
        ret = cv2.matchShapes(contour_list[0], contour_list[i+1], 1, 0.0)

        print(ret)
    cv2.waitKey(0)
    cv2.destroyAllWindows()