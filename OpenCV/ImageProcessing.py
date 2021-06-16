import numpy as np
import cv2

img = cv2.imread('yuna.jpg', cv2.IMREAD_COLOR)

#approching specific pixel
B = img.item(340, 200, 0)
G = img.item(340, 200, 1)
R = img.item(340, 200, 2)

BGR = [B, G, R]

#show original image
# cv2.imshow('original', img)

#cutting
subimg = img[300:400, 350:750]
# cv2.imshow('cutting', subimg)

#modifying original image
img[300:400, 0:400] = subimg
# cv2.imshow('modified', img)

img2 = cv2.imread('yuna.jpg', cv2.IMREAD_COLOR)

#spliting to each channel
#after spliting, the image woulb be shown gray scale becuase, the array is 1 dimension
b, g, r = cv2.split(img2)
# cv2.imshow('blue channel', b)
# cv2.imshow('green channel', g)
# cv2.imshow('red channel', r)

#merging each channel
merged_img2 = cv2.merge((b,g,r))
# cv2.imshow('merged image', merged_img2)

#spliting to each channel by using numpy indexing
b2 = img[:,:,0]
g2 = img[:,:,1]
r2 = img[:,:,2]
cv2.imshow('blue channel', b2)
cv2.imshow('green channel', g2)
cv2.imshow('red channel', r2)

cv2.waitKey(0)
cv2.destroyAllWindows()