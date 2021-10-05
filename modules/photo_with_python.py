import datetime
import cv2


t = datetime.datetime.now()
camera = cv2.VideoCapture(0)
for i in range(20):
    return_value, image = camera.read()
cv2.imwrite(f"{t.second,t.minute,t.hour,t.day,t.month}.png",image)
del(camera)
