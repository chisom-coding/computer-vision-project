import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'office_worker.jpg'))

k_size = 7
blurred_img = cv2.blur(img, (k_size, k_size))
gaussian_blur_img = cv2.GaussianBlur(img, (k_size, k_size), 5)
# good for denoising images
median_blur_img = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('blurred_img', blurred_img)
cv2.imshow('gaussian_blur_img', gaussian_blur_img)
cv2.imshow('median_blur_img', median_blur_img)
cv2.waitKey(0)