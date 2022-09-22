import cv2 as cv
import numpy as np
from time import sleep

# FPS video
delay = 60

# mengambil source video
cap = cv.VideoCapture("Pedestrian.mp4")

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

    # mencari contour
    contours, _ = cv.findContours(dilatasi, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # bounding contour
    for contour in contours:
        (x, y, w, h) = cv.boundingRect(contour)
        if cv.contourArea(contour) < 900:
            continue

        # membuat persegi
        cv.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # membuat tulisan "Pedestrian pada bounding rectangle"
        cv.putText(frame1, "Pedestrian".format(x, y), (x, y), cv.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    # menampilkan frame
    cv.imshow("Video", frame1)

    # menampilkan hasil return frame ke dua
    framel = frame2
    ret, frame2 = cap.read()

    # menutup program jika tombol q ditekan
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# menutup program dan menutup window
cap.release()
cv.destroyAllWindows()