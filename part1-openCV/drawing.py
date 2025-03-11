import os

import cv2

img = cv2.imread(os.path.join('.', 'data', 'whiteboard.jpg'))

print(img.shape)

# line
cv2.line(img,(50, 100), (80, 150), (0, 255, 0), 3)

# rectangle
cv2.rectangle(img, (80, 130), (160, 210), (255, 0, 0), -1)

# circle
cv2.circle(img, (150, 100), 50, (0, 0, 255), 2)

cv2.putText(img, 'Whats up!', (50, 80), cv2.FONT_HERSHEY_SIMPLEX, 1,  (255, 0, 150), 3)

cv2.imshow('img', img)
cv2.waitKey(0)