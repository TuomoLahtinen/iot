import time
from picamera import PiCamera

import matplotlib
import numpy as np
import cv2
from matplotlib import pyplot as plt

cam = PiCamera()
cam.start_preview()
time.sleep(5)
cam.capture('naamakuva.jpg')
cam.stop_preview()
time.sleep(5)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
img = cv2.imread('parsta.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img2 = img

faces = face_cascade.detectMultiScale(gray, 1.3, 5)
for (x,y,w,h) in faces:
    img2 = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray)
    for (ex,ey,ew,eh) in eyes:
        img2 = cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
plt.imsave('tunnistus_Pikamera.png', img2)