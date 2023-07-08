import numpy as np
import cv2

url = "http://172.16.219.240:8080/video"
cap = cv2.VideoCapture(url)

while (cap.isOpened()):
    camera,frame = cap.read()
    try:
        height, width = frame.shape[:2]
        center_x = int(width / 2)
        center_y = int(height / 2)
        cv2.circle(frame, (center_x, center_y), 5, (0, 255, 0), -1)
        cv2.imshow('Imagen',cv2.resize(frame,(600,400)))
        key = cv2.waitKey(1)
        if key == 27:
            break
    except cv2.error:
        print("end")
        break
cv2.imwrite('imagen.jpg',frame)
cap.release()
cv2.destroyAllWindows()

obj=cv2.imread('imagen.jpg',0)
recorte = obj[200:400,130:270]
cv2.imshow('imagen.jpg',recorte)

cap = cv2.VideoCapture(url)
while (cap.isOpened()):
    ret2,frame2 = cap.read()
    cv2.imshow('Deteccion',cv2.resize(frame2,(600,400)))
    if cv2.waitKey(1)==27:
        break
cv2.imwrite('Deteccion.jpg',frame2)
cap.release()
cv2.destroyAllWindows()

img = cv2.imread('Deteccion.jpg',3)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('Deteccion',img)

w,h=recorte.shape[::-1]
deteccion = cv2.matchTemplate(gray,recorte,cv2.TM_CCOEFF_NORMED)
umbral = 0.75
ubi = np.where(deteccion >= umbral)
for pt in zip(*ubi[::-1]):
    cv2.rectangle(img,pt,(pt[0]+w,pt[1]+h), (255,0,0), 1)