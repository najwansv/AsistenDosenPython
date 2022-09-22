import cv2
import numpy as np
from time import sleep

# Mengambil source file
cap = cv2.VideoCapture("E:\Kuliah\Asdos\RoadTraffic.mp4")

# Menjalankan program
while True:
    ret, frame1 = cap.read()

    # menampilkan file video
    cv2.imshow("original video", frame1)

    # memberhentikan program dengan huruf "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()