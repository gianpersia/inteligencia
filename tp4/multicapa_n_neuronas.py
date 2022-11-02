import random
import math
import matplotlib.pyplot as plt


def graficar(limite_iteraciones, errores):
    lista_iteraciones = []
    for i in range(limite_iteraciones):
        lista_iteraciones.append(i)
    plt.xlabel("Iteraciones")
    plt.ylabel("Errores")
    plt.title("GRÁFICO DE ERRORES")
    plt.axhline(y=0, color='black', linestyle='-')
    for cont in range(4):
        plt.plot(lista_iteraciones, errores[cont], label=f"error{cont}")
    plt.legend()
    plt.show()


def main():

    e1 = [0, 0, 1, 1]
    e2 = [0, 1, 0, 1]
    sd = [0, 1, 1, 0]

    bias = 1

    neuronas_ocultas = int(input("Ingrese la cantidad de neuronas en capa oculta: "))
    cantidad_pesos = math.trunc((neuronas_ocultas * 13)/3)

    errores = [[], [], [], []]
    
    pesos = [random.uniform(1,-1) for _ in range(cantidad_pesos)]

    lista_pesos = [[] for _ in range(cantidad_pesos)]

    learning_rate = float(input("Ingrese el learning rate: "))

    limite_iteraciones = int(input("Ingrese la cantidad de iteraciones a realizar: "))

    iteraciones = 0

    salidas_reales = sd.copy()

    while True:

        copia_pesos = pesos.copy()

        iteraciones += 1

        for i, peso in enumerate(pesos):
            lista_pesos[i].append(peso)

        for cont in range(4):

            copia_pesos = pesos.copy()

            entradas = [bias, e1[cont], e2[cont]]
            salidas = [] 
            deltas = []

            for _ in range(neuronas_ocultas):
                x = 0
                for entrada in entradas:
                    x += entrada*copia_pesos[0]
                    copia_pesos.remove(copia_pesos[0])
                y = 1/(1 + math.exp(-x))
                salidas.append(y)

            entradas = [bias]
            for element in salidas:
                entradas.append(element)

            x = 0
            for entrada in entradas:
                x += entrada*copia_pesos[0]
                copia_pesos.remove(copia_pesos[0])
            y = 1/(1 + math.exp(-x))

            error = sd[cont] - y
            errores[cont].append(error)
            salidas_reales[cont] = y

            d_f = y * (1 - y) * error

            dwf = [learning_rate * entrada * d_f for entrada in entradas]

            d_o = [salida * (1 - salida) * d_f for salida in salidas]

            entradas = [bias, e1[cont], e2[cont]]
            for d in d_o:
                for entrada in entradas:
                    deltas.append(learning_rate * entrada * d)

            deltas.extend(dwf)

            for i, delta in enumerate(deltas):
                pesos[i] = pesos[i] + delta
            
        if iteraciones == limite_iteraciones:
            break
    
    for cont in range(4):
        print(f"Para e1={e1[cont]} y e2={e2[cont]}: salida real={salidas_reales[cont]} / error={errores[cont][-1]} despues de {limite_iteraciones} iteraciones.")
    

    graficar(limite_iteraciones, errores)    


if __name__ == '__main__':
    main()