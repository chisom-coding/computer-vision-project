import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird_out.jpg'))

# converting from bgr to rgb colorspace
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# converting from bgr to gray colorspace
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# converting from bgr to hsv colorspace
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow('img', img)
# cv2.imshow('img_rgb', img_rgb)
# cv2.imshow('img_gray', img_gray)
cv2.imshow('img_hsv', img_hsv)
cv2.waitKey(0)