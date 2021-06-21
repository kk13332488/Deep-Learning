import numpy as np
import cv2
import matplotlib.pyplot as plt

def grad(imgfile):
    img = cv2.imread(imgfile, cv2.IMREAD_GRAYSCALE)

    #Horizontal, Vertical exploration at the same time
    laplacian = cv2.Laplacian(img, cv2.CV_64F)
    #Beware using CV_64F. If we use CV_8F, we can't find the boundary(changing form white to black) because 8bit turn minus to 0(8bit do not use minus).
    #Horizontal exploration
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3) #src, ddepth(image datatype), dx(differential order), dy, ksize
    #Vertical exploration
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('Laplacian'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('Sobel X'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('Sobel Y'), plt.xticks([]), plt.yticks([])

    plt.show()

grad('yuna.jpg')

