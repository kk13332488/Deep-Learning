import numpy as np
import cv2

def Transform(imgfile):
    img = cv2.imread(imgfile)
    h, w = img.shape[:2]

    #fx, fy are width, height each. Original image's size is 1.
    #INTER_AREA interpolation method is prefered when downsize images.
    #When we want to upsize, use cv2.INTER_CUBIC + cv2.INTER_LINEAR
    img2 = cv2.resize(img, None, fx=0.5, fy=1, interpolation=cv2.INTER_AREA)
    img3 = cv2.resize(img, None, fx=1, fy=0.5, interpolation=cv2.INTER_AREA)
    img4 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    cv2.imshow('original', img)
    cv2.imshow('fx=0.5', img2)
    cv2.imshow('fy=0.5', img3)
    cv2.imshow('fx=0.5, fy=0.5', img4)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Translation(imgfile):
    img = cv2.imread(imgfile)
    h, w = img.shape[:2]

    #Image translation matrix.
    #shape is M = |1 0 t_x|
    #             |0 1 y_x|
    #In this function, we translate image x axis as 100, y axis as 50
    M = np.float32([[1,0,100],[0,1,50]])
    #Using cv2.warpAffine, we can shift image like M*Transpose(img)
    #(w, h) is the size to print
    img2 = cv2.warpAffine(img, M, (w, h))
    cv2.imshow('Shifted Image', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def Rotation(imgfile):
    img = cv2.imread(imgfile)
    h, w = img.shape[:2]

    # Standard is (w/2, h/2). It means the center of Image(Centroid).
    # Return value is Matrix
    M1 = cv2.getRotationMatrix2D((w/2, h/2), 45, 1) #45 degree rotation
    M2 = cv2.getRotationMatrix2D((w/2, h/2), 90, 1) #90 degree rotation

    img2 = cv2.warpAffine(img, M1, (w, h))
    img3 = cv2.warpAffine(img, M2, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('45-Rotated', img2)
    cv2.imshow('90-Rotated', img3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def AffineTransform(imgfile):
    img = cv2.imread(imgfile)
    h, w = img.shape[:2]

    #Coordinates to transform
    pts1 = np.float32([[50,50],[200,50],[20,200]])
    #Coordinates which transformed from below
    pts2 = np.float32([[10,100],[200,50],[100,250]])

    M = cv2.getAffineTransform(pts1, pts2)

    img2 = cv2.warpAffine(img, M, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('Affine-Transform', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def PerspectiveTransform(imgfile):
    img = cv2.imread(imgfile)
    h, w = img.shape[:2]

    pts1 = np.float32([[0,0],[300,0],[0,300],[300,300]])
    pts2 = np.float32([[56, 65],[368, 52],[28, 387],[389, 390]])

    M = cv2.getPerspectiveTransform(pts1, pts2)

    img2 = cv2.warpPerspective(img, M, (w, h))

    cv2.imshow('original', img)
    cv2.imshow('Perspective-Transformed', img2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

PerspectiveTransform('yuna.jpg')

