#creating my camera
import cv2
cam = cv2.VideoCapture(0)
while True:
    status, photo = cam.read()
    cv2.imshow("Camera", photo)#display photo
    if cv2.waitKey(1) == 27:#holds the screen for a sec
        break
cv2.destroyAllWindow()
cam.release()
