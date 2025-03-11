import cv2

# reading webcam
webcam = cv2.VideoCapture(0)

# visualizing webcam
while True:
    ret, frame = webcam.read()

    # closes the window when letter 'q' is clicked
    cv2.imshow('frame', frame)
    if cv2.waitKey(40) & 0xFF == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()

