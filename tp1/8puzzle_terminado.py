import os
import random
import time

lista=[]

#a continuacion defino los movimientos que puede hacer

def izquierda(puzzle, indice):
    if indice % 3 > 0:
        auxiliar=puzzle[indice-1]
        puzzle[indice-1]=puzzle[indice]
        puzzle[indice]=auxiliar
        return puzzle

def derecha(puzzle, indice):
    if indice % 3 < 2:
        auxiliar=puzzle[indice+1]
        puzzle[indice+1]=puzzle[indice]
        puzzle[indice]=auxiliar
        return puzzle

def arriba(puzzle, indice):
    if indice - 3 >= 0:
        auxiliar=puzzle[indice-3]
        puzzle[indice-3]=puzzle[indice]
        puzzle[indice]=auxiliar
        return puzzle

def abajo(puzzle, indice):
    if indice + 3 < len(puzzle):
        auxiliar=puzzle[indice+3]
        puzzle[indice+3]=puzzle[indice]
        puzzle[indice]=auxiliar
        return puzzle

#aca se procede a establecer el menu
def menu_usuario(puzzle):
    print("8-PUZZLE\n")
    print("ESTADO INICIAL:\n")
    print(f'{puzzle}\n')
    print("SELECCIONE UN MÉTODO: \n")
    print("1. MEZCLAR para mezclar 50 veces\n")
    print("2. RANDOM para realizar busqueda random\n")
    print("3. ANCHURA para realizar una busqieda por anchura\n")
    print("4. Terminar el programa.\n")
    algoritmo = int(input("SELECCIÓN: "))
    return algoritmo

#esta funcion es para mezclar el puzzle

def mezcla(puzzle):
    lista1=[0, 1, 2, 3]
    indice=puzzle.index(0)
    funcion=random.choice(lista1)
    if funcion == 2:
        if indice%3>0:
            puzzle=izquierda(puzzle, indice)
    elif funcion==3:
        if indice%3<2:
            puzzle=derecha(puzzle, indice)
    elif funcion==0:
        if indice-3>=0:
            puzzle=arriba(puzzle, indice)
    elif funcion==1:
        if indice+3<len(puzzle):
            puzzle=abajo(puzzle, indice)
    return puzzle

#ahora vamos a definir las funciones de33 busqueda

def anchura(puzzle, correcto):
    lista.append(puzzle)
    print(lista)
    mov=0
    i=-1
    while True:
        i+=1
        nodo=lista[i].copy()
        indice=nodo.index(0)
        print("MOVIMIENTOS DE NODO: \n")
        print(f'{nodo}')
        puzzle_izquierda=izquierda(nodo.copy(), indice)
        if puzzle_izquierda is not None and puzzle_izquierda not in lista:
            print(puzzle_izquierda)
            lista.append(puzzle_izquierda)
            mov+=1
            if puzzle_izquierda==correcto:
                break
        puzzle_derecha=derecha(nodo.copy(), indice)
        if puzzle_derecha is not None and puzzle_derecha not in lista:
            print(puzzle_derecha)
            lista.append(puzzle_derecha)
            mov+=1
            if puzzle_derecha==correcto:
                break
        puzzle_arriba=arriba(nodo.copy(), indice)
        if puzzle_arriba is not None and puzzle_arriba not in lista:
            print(puzzle_arriba)
            lista.append(puzzle_arriba)
            mov+=1
            if puzzle_arriba==correcto:
                break
        puzzle_abajo=abajo(nodo.copy(), indice)
        if puzzle_abajo is not None and puzzle_abajo not in lista:
            print(puzzle_abajo)
            lista.append(puzzle_abajo)
            mov+=1
            if puzzle_abajo==correcto:
                break
    print("Movimientos necesarios para llegar a la solucion: \n")
    print(f'{mov}')

def busqueda_random(puzzle, correcto):
    print("Puzzle inicial: \n")
    print(f'{puzzle}')
    mov=0
    while True:
        mix_p=mezcla(puzzle)
        puzzle=mix_p
        mov+=1
        if puzzle==correcto:
            print("Movimientos necesarios para llegar a la solucion: \n")
            print(f'{mov}')
            print("Puzzle final: \n")
            print(f'{puzzle}')
            break

#y para finalizar definimos el main

def main():
    puzzle=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    correcto=[1, 2, 3, 4, 5, 6, 7, 8, 0]

    while True:
        algoritmo = menu_usuario(puzzle)
        if algoritmo==1:
            for i in range(50):
                puzzle=mezcla(puzzle)
        elif algoritmo==2:
            busqueda_random(puzzle, correcto)
        elif algoritmo==3:
            anchura(puzzle, correcto)
        elif algoritmo==4:
            break
        else:
            print("Seleccion erronea")

if __name__ == '__main__':
    
    main()
        



        

    
