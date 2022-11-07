import random
from numpy import exp
import numpy as np
import matplotlib.pyplot as plt
import time
import cv2



def obtener_array_imagen(gesto, imagen):
    path = f'tp6/fotostp5/persona{imagen}/{gesto}.jpg'
    print(f"Direccion en uso: {path}")

    img = cv2.imread(path)
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    filas, columnas = grey.shape

    imgl = [1]

    for i in range(filas):
        for j in range(columnas):
            imgl.append(img[i, j][0])
    
    return imgl

def calcular_cantidad_pesos(entradasl, neuronas):
    return ((len(entradasl)) * neuronas) + (neuronas + 1)

def calcular_x(entradasl, primeros_pesos):
    return sum(np.multiply(entradasl, primeros_pesos))

def calcular_y(x):
    return 1/(1 + exp(-x))

def calcular_error(sd, y):
    return sd - y

def calcular_delta_f(y, error):
    return y * (1 - y) * error

def graficar_errores(errores):
    iteracionesl = []
    iteracionesl.extend(range(0, 100))
    plt.xlabel("Iteraciones")
    plt.ylabel("Errores")
    plt.title("Grafico de errores")
    plt.axhline(y=0, color='black', linestyle='-')
    for cont in range(10):
        plt.plot(iteracionesl, errores[cont])
    plt.show()


def main():

    gestos = ['gesto1', 'gesto2', 'gesto3', 'gesto4', 'gesto5']
    errores = []
    for _ in range(len(gestos)):
        errores += [],[]

    aux_imagenes = 0
    
    lr = 0.5

    neuronas = 100

    for gesto in gestos:

        for imagen in range(2):

            entradasl = obtener_array_imagen(gesto, imagen)

            bias = 1
            if imagen == 0:
                sd = 0
            elif imagen == 1:
                sd = 1

            cantidad_pesos = calcular_cantidad_pesos(entradasl, neuronas)

            pesos = []
            for p in range(cantidad_pesos):
                pesos.append(random.uniform(0.01,-0.01))

            iter = 0
            printcounter = 0

            inicio = time.time()
            times_printed = 0

            while 1:

                iter += 1
                if iter == 101:
                    final = time.time()
                    print(f"Llegamos a las {iter - 1} iteraciones en {final - inicio} segundos.")
                    break

                salidas = [bias]
                deltas = []

                aux = 0
 
                for _ in range(neuronas):

                    primeros_pesos = []
                    for i in range(aux, aux + len(entradasl)):
                        primeros_pesos.append(pesos[i])
                    aux += len(entradasl)

                    x = calcular_x(entradasl, primeros_pesos)
                    y = calcular_y(x)
                    salidas.append(y)

                cantidad_ultimos_pesos = neuronas + 1
                ultimos_pesos = pesos[-cantidad_ultimos_pesos:]

                x = calcular_x(salidas, ultimos_pesos)
                y = calcular_y(x)

                error = calcular_error(sd, y)
                errores[aux_imagenes] += [error]

                if printcounter == 99:
                    print(f"Salida real = {y}")
                    print(f"Error = {error}")

                delta_f = calcular_delta_f(y, error)

                deltas_pesos_finales = []
                for s in salidas:
                    deltas_pesos_finales.append(lr * s * delta_f)

                salidas.remove(salidas[0])

                deltas_ocultas = []
                for s in salidas:
                    deltas_ocultas.append(s * (1 - s) * delta_f)

                for delta_oculta in deltas_ocultas:
                    deltas += list(np.multiply(entradasl, delta_oculta * lr))

                deltas.extend(deltas_pesos_finales)

                pesos = np.sum([pesos, deltas], axis=0)

                final = time.time()
            
            aux_imagenes += 1

    graficar_errores(errores)



if __name__ == '__main__':
    main()