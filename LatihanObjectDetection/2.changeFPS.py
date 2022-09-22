import cv2
import numpy as np
from time import sleep

delay = 60 # FPS Video
cap = cv2.VideoCapture("E:\Kuliah\Asdos\RoadTraffic1.mp4")

# Menjalankan program
while True:
    ret, frame1 = cap.read()

    tempo = float(1/delay) # membuat tempo dari delay
    sleep(tempo) # memperlambat video berdasarkan tempo

    # menampilkan file video
    cv2.imshow("Original video", frame1)

    # memberhentikan program dengan huruf "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()