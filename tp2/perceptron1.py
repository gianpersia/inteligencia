import math
import random
import matplotlib.pyplot as plt

plt.style.use('ggplot')

#lista_iteracion=[]
#lista_pesos=[]
#lista_error=[]


def menu():
    print("TRABAJO PRACTICO 2 - PERCEPTON SIMPLE")
    print("\n")
    print("Compuertas: \n")
    print("1) OR \n")
    print("2) AND \n")
    usuario=int(input("Seleccione una opcion: "))
    return usuario

def pesos_sinopticos():
    #w0=random.uniform(-1, 1)
    #w1=random.uniform(-1, 1)
    #w2=random.uniform(-1, 1)
    w0=0.9
    w1=0.66
    w2=-0.2
    return w0, w1, w2


def aprender(aprendizaje, e0, e1, e2, sd, w0, w1, w2, iteracion, lr):
    while aprendizaje==True:
        print(f"ITERACION: {iteracion} \n")

        iteracion += 1
        if iteracion==100:
            break
        aprendizaje=False
        for aux in range(0,4):
            print(f"R= {aux} \n")
            print("Sinopticos finales: \n")
            print(f"w0={w0}   w1={w1}   w2={w2} \n")
            
            #lista_iteracion.append(iteracion)
            #lista_pesos.append(w0)
            #lista_pesos.append(w1)
            #lista_pesos.append(w2)
            #lista_error.append(e)
            x=e0*w0+e1[aux]*w1+e2[aux]*w2
            y=1/(1+math.exp(-x))
            e=sd[aux]-y
            print(f"error= {e} \n")

            if abs(e)>0.1:   
            #if y>0.5:
            #    salida=1
            #else:
            #    salida=0
                aprendizaje=True
                d=y*(1-y)*e
                dw0=lr*e0*d
                dw1=lr*e1[aux]*d
                dw2=lr*e2[aux]*d
                #print(f"dw0={dw0}   dw1={dw1}   dw2={dw2} \n")
                #ahora vamos por los sinopticos obtenidos
                w0=w0+dw0
                w1=w1+dw1
                w2=w2+dw2
            plt.scatter(iteracion, e)
        if aprendizaje==False:
            break
    #print(f"Iteraciones= {iteracion} \n")
    #print("Sinopticos finales: \n")
    #print(f"w0={w0}   w1={w1}   w2={w2} \n")
    print("Tabla logica: \n")
    for aux in range(0,4):
        x=e0*w0+e1[aux]*w1+e2[aux]*w2
        y=1/(1+math.exp(-x))
        if y > 0.5:
            salida=1
        else:
            salida=0
        print(f"e1= {e1[aux]}")
        print(f"e2= {e2[aux]}")
        print(f"s= {salida}")
    plt.show()
    #return e



if __name__ == '__main__':

    usuario = menu()

    e0=1
    e1=[0, 0, 1, 1]
    e2=[0, 1, 0, 1]

    salida=0
    iteracion=0
    aprendizaje = True
    lr=0.1

    if usuario == 1:
        sd=[0, 1, 1, 1]
    elif usuario == 2:
        sd=[0, 0, 0, 1]
    
    w0, w1, w2 = pesos_sinopticos()
    print("Pesos iniciales: \n")
    print(f"w0={w0}\tw1={w1}\tw2={w2}\n")
    
    aprender(aprendizaje, e0, e1, e2, sd, w0, w1, w2, iteracion, lr)

    figure = plt.figure()
    #plt.scatter(lista_iteracion, lista_pesos)
    plt.xlabel('iteraciones')
    plt.ylabel('error')
    plt.title('PERCEPTRON SIMPLE')