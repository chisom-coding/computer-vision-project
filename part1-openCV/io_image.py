import os
import cv2

# reading image
image_path = os.path.join('.', 'data', 'bird.jpg')

img = cv2.imread(image_path)

# writing image
cv2.imwrite(os.path.join('.', 'data', 'bird_out.jpg'), img)

# visualize image
cv2.imshow('image', img)
cv2.waitKey(5000)