import cv2 as cv
import numpy as np
from time import sleep

# FPS video
delay = 60

# mengambil source video
cap = cv.VideoCapture("E:\Code\Asistensi\Pedestrian detection\in.mp4")

# ketika video di buka
while cap.isOpened():
    # menerima retun value dari frame
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()

    #  membuat tempo dari delay
    tempo = float(1 / delay)
    sleep(tempo)  # memperlambar video berdasarkan tempo

    # menghitung perbedaan antar frame
    perubahan = cv.absdiff(frame1, frame2)

    # mengubahvideo menjadi hitam putih
    grey = cv.cvtColor(perubahan, cv.COLOR_BGR2GRAY)

    # lalu di blur agar mengurangi noise
    blur = cv.GaussianBlur(grey, (5, 5), 0)

    # menerapkan ambang batas treshold di setiap elemen piksel
    _, thresh = cv.threshold(blur, 20, 255, cv.THRESH_BINARY)

    # dilatasi agar lebih jelas objectnya
    dilatasi = cv.dilate(thresh, None, iterations=5)

    # menampilkan frame
    cv.imshow("Video", frame1)
    cv.imshow("dilatasi", dilatasi)

    # menutup program jika tombol q ditekan
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# menutup program dan menutup window
cap.release()
cv.destroyAllWindows()