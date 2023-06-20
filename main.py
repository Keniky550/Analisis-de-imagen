import cv2
import numpy as np

# Carga la imagen desde un archivo
image = cv2.imread('img/circulos.jpg')

# Convierte la imagen a escala de grises
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplica un desenfoque gaussiano para reducir el ruido
gray = cv2.GaussianBlur(gray, (5, 5), 0)

# Detecta círculos en la imagen
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 20,
                           param1=50, param2=30, minRadius=0, maxRadius=0)

# Dibuja un círculo alrededor de cada círculo detectado
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0,:]:
        # Dibuja el contorno del círculo
        cv2.circle(image, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Dibuja el centro del círculo
        #cv2.circle(image, (i[0], i[1]), 2, (0, 0, 255), 3)

# Muestra la imagen resultante en una ventana
cv2.imshow('image', image)

# Espera a que se presione una tecla para cerrar la ventana
cv2.waitKey(0)
cv2.destroyAllWindows()