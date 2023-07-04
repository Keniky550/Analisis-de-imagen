import cv2
import numpy as np
import tkinter as tk
from tkinter import ttk

url ="https://192.168.3.58:8080/video"
captura = cv2.VideoCapture(url)
while (captura.isOpened()):
    camera,frame = captura.read()
    try:
        cv2.imshow('Imagen',cv2.resize(frame,(600,400)))
        key = cv2.waitKey(1)
        if key == ord('q'):
            break
        elif key == ord('c'):
            resize_frame = cv2.resize(frame,(600,400))
            cv2.imwrite('imagen.jpg',resize_frame)
    except cv2.error:
        print("end")
        break

cv2.destroyAllWindows()

#Código para crear un input en ventana

def guardar_datos():
    global forma, color

    forma = combobox1.get()
    color = combobox2.get()

    print({'forma': forma, 'color':color})
    ventana.destroy()

ventana = tk.Tk()
ventana.title("Características del objeto")

etiqueta1 = tk.Label(ventana, text="Forma:")
combobox1 = ttk.Combobox(ventana,values=["circulo", "cuadrado", "triangulo", "rectangulo","pentagono", "hexagono"])
etiqueta2 = tk.Label(ventana, text="Color:")
combobox2 = ttk.Combobox(ventana,values=["rojo", "azul", "naranja", "amarillo", "verde","rosa","violeta"])
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)

etiqueta1.pack()
combobox1.pack()
etiqueta2.pack()
combobox2.pack()
boton_guardar.pack()

ventana.geometry('400x300')
ventana.mainloop()

#Parametrizamos los colores
# Rojo
rojoBajo1 = np.array([0, 100, 20], np.uint8)
rojoAlto1 = np.array([10, 255, 255], np.uint8)
rojoBajo2 = np.array([175, 100, 20], np.uint8)
rojoAlto2 = np.array([180, 255, 255], np.uint8)

# Naranja
naranjaBajo = np.array([11, 100, 20], np.uint8)
naranjaAlto = np.array([19, 255, 255], np.uint8)

#Amarillo
amarilloBajo = np.array([20, 100, 20], np.uint8)
amarilloAlto = np.array([32, 255, 255], np.uint8)

#Verde
verdeBajo = np.array([36, 100, 20], np.uint8)
verdeAlto = np.array([70, 255, 255], np.uint8)

#Violeta
violetaBajo = np.array([130, 100, 20], np.uint8)
violetaAlto = np.array([145, 255, 255], np.uint8)

#Rosa
rosaBajo = np.array([146, 100, 20], np.uint8)
rosaAlto = np.array([170, 255, 255], np.uint8)

#Azul
azulBajo = np.array([100,100,20],np.uint8)
azulAlto = np.array([125,255,255],np.uint8)

#Iniciar variables
img = cv2.imread("imagen.jpg")
imagenHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
canny = cv2.Canny(gray,10,150)
canny = cv2.dilate(canny,None,iterations=1)
canny = cv2.erode(canny,None,iterations=1)

# Se buscan los colores en la imagen, segun los límites altos 
# y bajos dados
maskRojo1 = cv2.inRange(imagenHSV, rojoBajo1, rojoAlto1)
maskRojo2 = cv2.inRange(imagenHSV, rojoBajo2, rojoAlto2)
maskRojo = cv2.add(maskRojo1, maskRojo2)
maskNaranja = cv2.inRange(imagenHSV, naranjaBajo, naranjaAlto)
maskAmarillo = cv2.inRange(imagenHSV, amarilloBajo, amarilloAlto)
maskVerde = cv2.inRange(imagenHSV, verdeBajo, verdeAlto)
maskVioleta = cv2.inRange(imagenHSV, violetaBajo, violetaAlto)
maskRosa = cv2.inRange(imagenHSV, rosaBajo, rosaAlto)
maskAzul = cv2.inRange(imagenHSV,azulBajo,azulAlto)

#Encontrar contornos
contornoAmarillo = cv2.findContours(maskAmarillo.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoVioleta = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoNaranja = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoRosa= cv2.findContours(maskRosa,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoAzul = cv2.findContours(maskAzul, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

#Trabajando con las figuras
ctns,_=cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

#Fusionar contornos


for c in  ctns:
    epsilon = 0.001*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    print(len(approx))
    #cv2.drawContours(img,[approx],0,(0,255,0),2)
    #cv2.imshow("Figuras", img)
    #cv2.waitKey(0)
    if forma =='':
        if color == "": cv2.drawContours(img,[approx],-1,(0,255,0),2)
        elif color == "rojo": cv2.drawContours(img,contornoRojo,-1,(0,255,0),2)
        elif color == "naranja": cv2.drawContours(img,contornoNaranja,-1,(0,255,0),2)
        elif color == "amarillo": cv2.drawContours(img,contornoAmarillo,-1,(0,255,0),2)
        elif color == "verde": cv2.drawContours(img,contornoVerde,-1,(0,255,0),2)
        elif color == "violeta": cv2.drawContours(img,contornoVioleta,-1,(0,255,0),2)
        elif color == "rosa": cv2.drawContours(img,contornoRosa,-1,(0,255,0),2)
        elif color == "azul": cv2.drawContours(img,contornoAzul,-1,(0,255,0),2)

    elif forma == 'triangulo' and len(approx) == 3:
        if color == "": 
            cv2.drawContours(img,[approx],-1,(0,255,0),2)
        elif color == "rojo": 
           on_forma = cv2.findContours(img,contornoRojo,-1,(0,255,0),2)
        elif color == "naranja": 
            con_forma = cv2.findContours(img,contornoNaranja,-1,(0,255,0),2)
        elif color == "amarillo": 
            con_forma = cv2.findContours(img,contornoAmarillo,-1,(0,255,0),2)
        elif color == "verde": 
            con_forma = cv2.findContours(img,contornoVerde,-1,(0,255,0),2)
        elif color == "violeta": 
            con_forma = cv2.findContours(img,contornoVioleta,-1,(0,255,0),2)
        elif color == "rosa": 
            con_forma = cv2.findContours(img,contornoRosa,-1,(0,255,0),2)
        elif color == "azul": 
            con_forma = cv2.findContours(img,contornoAzul,-1,(0,255,0),2)
    elif forma == 'circulo' and len(approx) == 8:
        if color == "": cv2.drawContours(img,[approx],-1,(0,255,0),2)
    elif forma == 'cuadrado' and len(approx) == 4:
        if color == "": cv2.drawContours(img,[approx],-1,(0,255,0),2)
    elif forma == 'hexagono' and len(approx) == 6:
        if color == "": cv2.drawContours(img,[approx],-1,(0,255,0),2)
    elif forma == 'pentagono' and len(approx) == 5:
        if color == "": cv2.drawContours(img,[approx],-1,(0,255,0),2)
        
cv2.imshow("FIguras", img)
cv2.waitKey(0)
cv2.destroyAllWindows()