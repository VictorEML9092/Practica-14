"""
Created on Monday 04/10/24

@author: Victor Mendoza
"""
import random # Modulo random

# Método por intercambio para ordenar letras
def metodo_burbuja(Listaletras):
    for i in range(len(Listaletras) - 1):
    
        for j in range(len(Listaletras) - 1):
        
            print(Listaletras[j], ">", Listaletras[j + 1]) # Se imprime la comparación
        
            if Listaletras[j] > Listaletras[j + 1]: # Comparamos las letras
                Listaletras[j], Listaletras[j + 1] = Listaletras[j + 1], Listaletras[j] # Si la primera letra es mayor que la segunda, intercambiamos
                print("Si hay cambio")
            else:
                print("No hay cambio")
    
        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(Listaletras, "\n") # Se imprime la lista actualizada

Listaletras = random.sample('abcdefghijklmnopqrstuvwxyz', 6)  # Se genera una lista con "n" letras únicas del alfabeto

print("La lista de letras a ordenar por el método Burbuja es:\n")
print(Listaletras, "\n") # Imprimimos la lista generada
metodo_burbuja(Listaletras)