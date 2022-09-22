import cv2 as cv
import numpy as np
from time import sleep

# FPS video
delay = 60

# mengambil source video
cap = cv.VideoCapture("E:\Code\Asistensi\Pedestrian detection\in.mp4")


# ketika video di buka
while cap.isOpened():
    ret, frame1 = cap.read()

    #  membuat tempo dari delay
    tempo = float(1 / delay)
    sleep(tempo)  # memperlambar video berdasarkan tempo

    # menampilkan frame
    cv.imshow("Video", frame1)

    # menutup program jika tombol q ditekan
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# menutup program dan menutup window
cap.release()
cv.destroyAllWindows()