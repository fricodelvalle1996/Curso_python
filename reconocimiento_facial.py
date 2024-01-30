from cv2 import cv2 #
import face_recognition as fr #para simplificar su uso
import os
import numpy
from datetime import datetime
from cmake import *

# cargar imagenes
foto_control = fr.load_image('FotoA.jpg')
foto_prueba = fr.load_image('FotoB.jpg')

#cambiar la forma en que se procesa el color (las pasamos a RGB)
foto_control = cv2.cvtColor(foto_control, cv2.COLOR_BGR2RGB)
foto_prueba = cv2.cvtColor(foto_prueba, cv2.COLOR_BGR2RGB)

#localizar cara control
lugar_cara_A = fr.face_locations(foto_prueba)[0] #ubica los puntos clave de la cara (arriba, abajo, izquierda y derecha)
cara_codificada_A = fr.face_encodings(foto_prueba)[0]

#localizar cara control
lugar_cara_B = fr.face_locations(foto_control)[0]
cara_codificada_B = fr.face_encodings(foto_control)[0]

#mostrar rectangulo
cv2.rectangle(foto_control,
              lugar_cara_A[3], lugar_cara_A[0],
              lugar_cara_A[4], lugar_cara_A[2],
              (0, 255, 0),
              2)

cv2.rectangle(foto_prueba,
              lugar_cara_B[3], lugar_cara_B[0],
              lugar_cara_B[4], lugar_cara_B[2],
              (0, 255, 0),
              2)

#realizar comparacion
resultado = fr.compare_faces([cara_codificada_A], cara_codificada_B) #usamos una lista aunque sea una sola foto porque así funciona el compare_faces
print(resultado)


#medida de la "distancia facial" (diferencia entre 2 caras)
distancia = fr.face_distance([cara_codificada_A], cara_codificada_B, 0.5) #el tercer valor es la tolerancia (por defecto viene el 0.6)
print(distancia)
cv2.putText(foto_prueba, #le metemos texto a la foto indicando la disntancia y el resultado de análisis
            f'{resultado} {distancia.round(2)}',
            (50, 50), #ubicacion del texto
            cv2.FONT_HERSHEY_COMPLEX, #fuente de texto
            1, #altura
            (0, 255, 0), #color del texto
            2) #grosor

#mostrar imagenes
cv2.imshow('Foto Control', foto_control)
cv2.imshow('Foto Prueba', foto_prueba)

#mantener programa abierto
cv2.waitKey(0)