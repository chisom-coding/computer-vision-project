import os
import cv2

img = cv2.imread(os.path.join('.', 'data', 'bird_out.jpg'))

cropped_img = img[120:600, 420:1000]

print(img.shape)
print(cropped_img.shape)


cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)