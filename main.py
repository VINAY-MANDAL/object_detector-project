import cv2 as cv
from camera import get_camera
from detector import detect

cap = get_camera()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    detected_frame = detect(frame)
    cv.imshow("Object Detecotor", detected_frame)

    if cv.waitKey(1) == ord('q'):
        break

cap.release()
cv.destroyAllWindows()


