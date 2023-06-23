import cv2 
import numpy as np
#Código para crear un input en ventana
import tkinter as tk
from tkinter import ttk

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
combobox2 = ttk.Combobox(ventana,values=["rojo", "naranja", "amarillo", "verde","rosa","violeta"])
boton_guardar = tk.Button(ventana, text="Guardar", command=guardar_datos)

etiqueta1.pack()
combobox1.pack()
etiqueta2.pack()
combobox2.pack()
boton_guardar.pack()

ventana.mainloop()
#Fin del input


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

img = cv2.imread("figurasColores2.png")
imagenHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
output = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.medianBlur(gray, 5)
circulo = cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,20,param1=50,param2=30,minRadius=0,maxRadius=0)
detectar_circulo = np.uint16(np.around(circulo))

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

#Encontrar contornos
contornoAmarillo = cv2.findContours(maskAmarillo, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoRojo = cv2.findContours(maskRojo, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoVerde = cv2.findContours(maskVerde, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoVioleta = cv2.findContours(maskVioleta, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoNaranja = cv2.findContours(maskNaranja, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]
contornoRosa= cv2.findContours(maskRosa,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)[0]

if color == "rojo": cv2.drawContours(img,contornoRojo,-1,(0,255,0),2)
if color == "naranja": cv2.drawContours(img,contornoNaranja,-1,(0,255,0),2)
if color == "amarillo": cv2.drawContours(img,contornoAmarillo,-1,(0,255,0),2)
if color == "verde": cv2.drawContours(img,contornoVerde,-1,(0,255,0),2)
if color == "violeta": cv2.drawContours(img,contornoVioleta,-1,(0,255,0),2)
if color == "rosa": cv2.drawContours(img,contornoRosa,-1,(0,255,0),2)


#if forma == "circulo":
#	for(x,y,r) in detectar_circulo[0, :]:
#		cv2.circle(output,(x,y),r,(0,255,0),2)

cv2.imshow("Figuras", img)
cv2.waitKey(0)
cv2.destroyAllWindows()