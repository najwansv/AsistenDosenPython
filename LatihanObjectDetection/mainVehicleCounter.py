import cv2
import numpy as np
from time import sleep

# minimum lebar dan tinggi contour
min_lebar = 80
min_tinggi = 80

deteksi = [] # membuat array untuk deteksi

pos_garis = 550 #Posisi Garis
offset = 5 # nilai toleransi
jumlahmobil = 0

# membuat fungsi untuk mencari titik tengah dari bounding
def posisi_tengah(x, y, w, h):
    x1 = int(w / 2)
    y1 = int(h / 2)
    cx = x + x1
    cy = y + y1
    return cx, cy

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

    # membuat contour
    contour, h = cv2.findContours(dilatasi2, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # membuat garis
    cv2.line(frame1, (0, pos_garis), (1400, pos_garis), (255, 150, 10), 3)

    # bounding contour dari vehicle yang bergerak
    for (i, c) in enumerate(contour):
        (x, y, w, h) = cv2.boundingRect(c)
        validasi_countour = (w >= min_lebar) and (h >= min_tinggi)
        if not validasi_countour:
            continue

        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)  # membuat persegi
        titiktengah = posisi_tengah(x, y, w, h) # menentukan titik tengah persegi
        deteksi.append(titiktengah)
        cv2.circle(frame1, titiktengah, 20, (0, 0, 255), -1) # membuat lingkaran ditengah persegi

    for (x, y) in deteksi:
        if y < (pos_garis + offset) and y > (pos_garis - offset):
            # jumlah mobil bertambah 1
            jumlahmobil += 1 # jumlah mobil bertambah 1
            # garis akan berubah warna
            cv2.line(frame1, (0, pos_garis), (1400, pos_garis), (10, 127, 255), 3) # garis berubah warna

        # jika sudah melewati garis deteksi dihilangkan
        deteksi.remove((x, y))
        # hasil di print di console
        print("Jumlah mobil yang terdeteksi saat ini: " + str(jumlahmobil))
        # hasil di print pada frame 1
        cv2.putText(frame1, "Kendaraan: " + str(jumlahmobil), (750, 50), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    # menampilkan file video
    cv2.imshow("Original video", frame1)
    cv2.imshow("Detector", dilatasi2)

    # memberhentikan program dengan huruf "q"
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()