import cv2
import numpy as np
from time import sleep

delay = 60 # FPS Video
cap = cv2.VideoCapture("E:\Kuliah\Asdos\RoadTraffic1.mp4")
# membuat Background subtractor
substraksibg = cv2.bgsegm.createBackgroundSubtractorMOG()

# Menjalankan program
while True:
    ret, frame1 = cap.read()

    tempo = float(1/delay) # membuat tempo dari delay
    sleep(tempo) # memperlambat video berdasarkan tempo

    # mengubah video background menjadi hitam putih (grey)
    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    #  lalu di blur agar mengurangi noise
    blur = cv2.GaussianBlur(grey, (3, 3), 5)
    # apply blur di background
    img_sub = substraksibg.apply(blur)

    # background sebelumnya di dilation
    dilatasi = cv2.dilate(img_sub, np.ones((5, 5)))
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    # dilatasi dua kali agar lebih jelas
    dilatasi1 = cv2.morphologyEx(dilatasi, cv2.MORPH_CLOSE, kernel)
    dilatasi2 = cv2.morphologyEx(dilatasi1, cv2.MORPH_CLOSE, kernel)

    # menampilkan file video
    cv2.imshow("Original video", frame1)
    cv2.imshow("Detector", dilatasi2)

    # memberhentikan program dengan huruf "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()