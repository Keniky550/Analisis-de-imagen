import cv2
import numpy as np
from tkinter import ttk

cap = cv2.VideoCapture(0)

def getContours(img):
    contours,Hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
        if area>500:
            cv2.drawContours(frame,cnt,-1,(0,255,0),2)
            perimetro = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.015*perimetro,True)
            objCorner = len(approx)
            x, y, w, h = cv2.boundingRect(approx)

            if objCorner == 2:
                objecttype = "Triangulo"
            elif objCorner == 4:
                aspecto = w/float(h)
                if aspecto >0.95 and aspecto < 1.05:
                    objecttype = "Cuadrado"
                else:
                    objecttype = "Rectangulo"
            elif objCorner > 4:
                objecttype = "Circulo"
            else:
                objecttype = "None"
            

            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
            cv2.putText(frame,objecttype,(x+(w//2)-10,y+(h//2)-10),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,255,0))

while (cap.isOpened()):
    ret,frame = cap.read()
    imgGray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    imgBlur = cv2.GaussianBlur(imgGray, (7,7),1)
    imgCanny = cv2.Canny(imgBlur, 50, 50)
    getContours(imgCanny)

 
    try:
        cv2.imshow('Imagen',cv2.resize(frame,(600,400)))
        key = cv2.waitKey(1)
        if (getContours):
            resize_frame = cv2.resize(frame,(600,400))
            image_filename = 'Encontrado.jpg'
            cv2.imwrite(image_filename, resize_frame)
        if key == ord('q'):
            break        
    except cv2.error:
        print("end")
        break

cap.release()
cv2.destroyAllWindows()

