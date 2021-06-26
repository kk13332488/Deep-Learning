import numpy as np
import cv2

def ImgRegul(imgfile):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)
    hist, bins = np.histogram(img.ravel(), 256, [0, 256])

    # cumsum means cumulative sum.
    cdf = hist.cumsum()

    # masked_equal makes turn 0 element of array into --(meanlessless value)
    cdf_m = np.ma.masked_equal(cdf, 0)
    # histogram regularizaion equation
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max()-cdf_m.min())
    # Fill masked values 0 again
    cdf = np.ma.filled(cdf_m, 0).astype('uint8')

    img2 = cdf[img]

    cv2.imshow('Histogram Equalizaion', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def ImgRegul2(imgfile):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    #equalizeHist works like what written in the code above, but it cannot deal with color image. Only gray scale.
    equ = cv2.equalizeHist(img)
    #attach res array to img array.
    res = np.hstack((img, equ))
    cv2.imshow('equalizer', res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

ImgRegul2('pic/CongealedImg.jpg')