import math
import random

print("TRABAJO PRACTICO 2 - PERCEPTON SIMPLE")
print("\n")
print("Compuertas disponibles: \n")
print("1) OR \n")
print("2) AND \n")
usuario=int(input("Seleccione una opcion: \n"))

#salida=0
#i=0

#PLANTEO DE FORMULAS
#logica
e0=1
e1=[0, 0, 1, 1]
e2=[0, 0, 0, 1]

if usuario == 1:
    sd=[0, 1, 1, 1]
elif usuario == 2:
    sd=[0, 0, 0, 1]
#sinopticos
w0=random.uniform(-1, 1)
w1=random.uniform(-1, 1)
w2=random.uniform(-1, 1)
#x e y
#cont = 0
#x=e0*w0+e1[cont]*w1+e2[cont]*w2
#y=1/(1+math.exp(-x))

#tenemos 2 tipos de pesos sinopticos, iniciaciales
#y finales, ahora vamos por los iniciales
print("Iniciales: \n")
print(f"w0={w0}   w1={w1}   w2={w2}\n")

salida=0
i=0
aprendizaje = True
lr=0.1

while aprendizaje==True:
    i+=1
    aprendizaje=False
    for cont in range(0,4):
        x=e0*w0+e1[cont]*w1+e2[cont]*w2
        y=1/(1+math.exp(-x))
        if y>0.5:
            salida=1
        else:
            salida=0
        if salida!=sd[cont]:
            aprendizaje=True
            e=sd[cont]-y
            d=y*(1-y)*e
            dw0=lr*e0*d
            dw1=lr*e1[cont]*d
            dw2=lr*e2[cont]*d

            #ahora vamos por los sinopticos obtenidos
            w0=w0+dw0
            w1=w1+dw1
            w2=w2+dw2
    if aprendizaje==False:
        break

#muestra de resultados por pantalla
#iteraciones, sinopticos finales y tabla logica

print(f"Iteraciones= {i} \n")
print("Sinopticos finales: \n")
print(f"w0={w0}   w1={w1}   w2={w2} \n")
print("Tabla logica: \n")
for cont in range(0,4):
    x=e0*w0+e1[cont]*w1+e2[cont]*w2
    y=1/(1+math.exp(-x))
    if y > 0.5:
        salida=1
    else:
        salida=0
print(f"e1= {e1[cont]}")
print(f"e2= {e2[cont]}")
print(f"s= {salida}")