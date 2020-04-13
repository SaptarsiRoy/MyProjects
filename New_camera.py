import cv2
cam = cv2.VideoCapture(0)
width = 480
height = 640
while True:
    status, photo = cam.read()
    cap_photo = photo[0:width, 0:height]
    cv2.imshow("camera", cap_photo)
    key = cv2.waitKey(1)
    if key == 13:
        break
    elif key == 111:
        if width != 480:
            width += 100
        if height != 640:
            height += 100
    elif key == 105:
        if width != 180:
            width -= 100
        if height != 240:
            height -= 100
cv2.destroyAllWindows()
cam.release()
