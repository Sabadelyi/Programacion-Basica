

import cv2
import numpy as np

imagen = cv2.imread("zona_quemada.jpg")

gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

_, umbral = cv2.threshold(gris, 200, 255, cv2.THRESH_BINARY)

contornos, _ = cv2.findContours(umbral, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(imagen, contornos, -1, (0, 0, 255), 2)

cv2.imshow("Zonas Quemadas Detectadas", imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()