import copy
from math import exp
import random


def tablaXOR():
    booleano = [0,1]
    resultado = int
    listaXOR = []

    print('Tabla de la verdad XOR: \n')
    print('a \t b \t salida \n')
    for X in booleano:
        for Y in booleano:
            resultado = int((X and not Y) or (not X and Y))
            #res = int(resultado)
            listaXOR.append(resultado)
    print('\n')
    #listaXOR.reverse()
    return listaXOR


def pesoSinaptico():
    lista_peso = []

    while True:
        for p in range(19):
            valor=float(input('Ingresar valor de peso sináptico: '))
            if valor >= -1 and valor <= 1:
                lista_peso.append(valor)
            else:
                print("Intente nuevamente.\n")
        return lista_peso


def fcBuffer():
    factores = [0,0]
    return factores


def neurona1(peso_sinaptico):
    terna_pesos = []
    factores = fcBuffer()
    a = factores[0]
    b = factores[1]
    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])

    w0 = terna_pesos[0][0]
    w1 = terna_pesos[0][1]
    w2 = terna_pesos[0][2]

    sr = calculo(w0,w1,w2,a,b)
    print('Salida real de neurona 1:',sr)
    print('\n')
    return sr


def neurona2(peso_sinaptico):
    terna_pesos = []
    factores = fcBuffer()
    a = factores[0]
    b = factores[1]

    for i in range(0, len(peso_sinaptico), 3):
        terna_pesos.append(peso_sinaptico[i:i+3])
    #print('\n')

    w3 = terna_pesos[1][0]
    w4 = terna_pesos[1][1]
    w5 = terna_pesos[1][2]

    sr = calculo(w3,w4,w5,a,b)
    print('Salida real de neurona 2:',sr)
    print('\n')
    return sr


def calculo(wa,wb,wc,sra,srb):
    #if sra == 0 and srb == 0:
    sumatoriaX = wa*1 + wb*sra + wc*srb
    funcionY = 1/(1+exp(-sumatoriaX))
    return funcionY


def menuPrincipal():
    salir = False
    continuar = False
    opcion = 0
    op = 0
    listaOR = []
    listaAND = []
    listaXOR = []
    peso_sinaptico = []
    correcto = False


    while not continuar:
        peso_sinaptico = pesoSinaptico()
        print('\n Los pesos sinápticos son: \n')
        for w in peso_sinaptico:
            print('w',w)
        print('\n')


        continuar = True

    while not salir:

        #opcion = seleccion()

        listaXOR = tablaXOR()
        #calculo(peso_sinaptico,listaXOR)
        n1 = neurona1(peso_sinaptico)
        n2 = neurona2(peso_sinaptico)
        salir = True
        print ("\n Fin \n")


if __name__ == '__main__':
    menuPrincipal()