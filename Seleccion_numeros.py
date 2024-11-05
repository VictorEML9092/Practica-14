"""
Created on Tuesday 05/10/24

@author: Victor Mendoza
"""
import random # Modulo random

# Método de selección para ordenar números
def metodo_seleccion(ListaNum):
    for i in range(len(ListaNum) - 1):
        indicemenor = i # Guardamos el indice del primer elemento como el menor

        for j in range(i + 1,len(ListaNum)): # Ciclo desde el elemento que sigue al seleccionado como menor hasta el último elemento

            print(f"El elemento menor es:",ListaNum[indicemenor]) # Se imprime el elemento menor seleccionado
            print(ListaNum[indicemenor],"<",ListaNum[j]) # Se imprime la comparación

            if ListaNum[indicemenor] > ListaNum[j]: # Comparamos los números
                indicemenor = j
                print("Si hay cambio")
            else:
                print("No hay cambio")
    
        if indicemenor != i: # Actuatilizamos las posiciones
            ListaNum[i], ListaNum[indicemenor] = ListaNum[indicemenor], ListaNum[i]

        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(ListaNum,"\n")

ListaNum = random.sample(range(1, 51), 6) # Se genera una lista de "n" números únicos del 1 al 50

print("La lista de números a ordenar por el método de Selección es:\n")
print(ListaNum,"\n")
metodo_seleccion(ListaNum)               