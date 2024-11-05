"""
Created on Tuesday 05/10/24

@author: Victor Mendoza
"""
import random # Modulo random

# Método de selección para ordenar letras
def metodo_seleccion(Listaletras):
    for i in range(len(Listaletras) - 1):
        indicemenor = i # Guardamos el indice del primer elemento como el menor

        for j in range(i + 1,len(Listaletras)): # Ciclo desde el elemento que sigue al seleccionado como menor hasta el último elemento

            print(f"El elemento menor es:",Listaletras[indicemenor]) # Se imprime el elemento menor seleccionado
            print(Listaletras[indicemenor],"<",Listaletras[j]) # Se imprime la comparación

            if Listaletras[indicemenor] > Listaletras[j]: # Comparamos las letras
                indicemenor = j
                print("Si hay cambio")
            else:
                print("No hay cambio")
    
        if indicemenor != i: # Actuatilizamos las posiciones
            Listaletras[i], Listaletras[indicemenor] = Listaletras[indicemenor], Listaletras[i]

        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(Listaletras,"\n")

Listaletras = random.sample('abcdefghijklmnopqrstuvwxyz', 6)  # Se genera una lista con "n" letras únicas del alfabeto

print("La lista de letras a ordenar por el método de Selección es:\n")
print(Listaletras,"\n")
metodo_seleccion(Listaletras) 