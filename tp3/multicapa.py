import math
import matplotlib.pyplot as plt


def graficar(errores, lista_pesos):
    itera = []
    for i in range(10000):
        itera.append(i)
    plt.figure(figsize=(15,5))
    plt.subplot(1, 2, 1)
    plt.xlabel("Iteraciones")
    plt.ylabel("Errores")
    plt.title("GRÁFICO DE ERRORES")
    plt.axhline(y=0, color='black', linestyle='-')
    plt.plot(itera, errores[0])
    plt.plot(itera, errores[1])
    plt.plot(itera, errores[2])
    plt.plot(itera, errores[3])
    plt.subplot(1, 2, 2)
    plt.xlabel("Iteraciones")
    plt.ylabel("Pesos")
    plt.title("GRÁFICO DE PESOS")
    plt.axhline(y=0, color='black', linestyle='-')
    for element in lista_pesos:
        plt.plot(itera, element)
    plt.show()


def main():
    e1 = [0, 0, 1, 1]
    e2 = [0, 1, 0, 1]
    sd = [0, 1, 1, 0]

    bias = 1

    learning_rate = 0.1

    errores = [[], [], [], []]

    lista_pesos = [[], [], [], [], [], [], [], [], [], [], [], [], []]

    for cont in range(4):

        pesos = [0.9, 0.7, 0.5, 0.3, -0.9, -1, 0.8, 0.35, 0.1, -0.23, -0.79, 0.56, 0.6]

        neuronas_ocultas = 3
        iteraciones = 0

        while True:
            copia_pesos = pesos.copy()
            entradas = [bias, e1[cont], e2[cont]]
            salidas = [] 
            deltas = []

            for _ in range(neuronas_ocultas):
                x = 0
                for i, element in enumerate(entradas):
                    x += element*copia_pesos[i]
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

            d_f = y * (1 - y) * error

            dwf = [learning_rate * entrada * d_f for entrada in entradas]

            d_o = [salida * (1 - salida) * d_f for salida in salidas]

            entradas = [bias, e1[cont], e2[cont]]
            for d in d_o:
                for entrada in entradas:
                    deltas.append(learning_rate * entrada * d)

            deltas.extend(dwf)

            for i, delta in enumerate(deltas):
                if len(lista_pesos[i]) < 10000:
                    lista_pesos[i].append(pesos[i])
                pesos[i] = pesos[i] + delta

            iteraciones += 1
            if iteraciones == 10000:
                break

        print(f"Salida{cont} = {y} despues de {iteraciones} iteraciones")
        print(f"Error{cont} = {error}")

    graficar(errores, lista_pesos)


if __name__ == '__main__':
    main()