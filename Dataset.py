import cv2
import numpy as np
import imutils
import os

url='https://192.168.3.58:8080/video'

Datos = 'n'
if not os.path.exists(Datos):
    print('Carpeta creada: ',Datos)
    os.makedirs(Datos)

cap = cv2.VideoCapture(url)

x1, y1 = 190, 80
x2, y2 = 1200, 1000

count = 0
while True:

    ret, frame = cap.read()
    
    if ret == False: break
    imAux = frame.copy()
    cv2.rectangle(frame,(x1,y1),(x2,y2),(255,0,0),2)

    objeto = imAux[y1:y2,x1:x2]
    objeto = imutils.resize(objeto,width=50)
    #print(objeto.shape)

    k = cv2.waitKey(1)
    if k == ord('s'):
        cv2.imwrite(Datos+'/objeto_{}.jpg'.format(count),objeto)
        print('Imagen guardada:'+'/objeto_{}.jpg'.format(count))
        count = count +1
    if k == 27:
        break
    

    cv2.imshow('Imagen',cv2.resize(frame,(600,400)))
    #cv2.imshow('frame',frame)
    cv2.imshow('objeto',objeto)

cap.release()
cv2.destroyAllWindows()