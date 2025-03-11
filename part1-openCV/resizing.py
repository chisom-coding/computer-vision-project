import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird_out.jpg'))

resized_img = cv2.resize(img, (600, 371))

print(img.shape)
print(resized_img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_image', resized_img)
cv2.waitKey(0)