"""
Created on Monday 04/10/24

@author: Victor Mendoza
"""
import random # Modulo random

# Método por intercambio para ordenar números
def metodo_burbuja(ListaNum):
    for i in range(len(ListaNum) - 1):
    
        for j in range(len(ListaNum) - 1):
        
            print(ListaNum[j],">",ListaNum[j + 1]) # Se imprime la comparación
        
            if ListaNum[j] > (ListaNum[j + 1]): # Comparamos los números
                ListaNum[j], ListaNum[j + 1] = ListaNum[j + 1], ListaNum[j] # Si el primer número es mayor al segundo, intercambiamos
                print("Si hay cambio")
            else:
                print("No hay cambio")
    
        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(ListaNum,"\n")

ListaNum = random.sample(range(1, 51), 6) # Se genera una lista de "n" números únicos del 1 al 50

print("La lista de números a ordenar por el método Burbuja es:\n")
print(ListaNum,"\n")
metodo_burbuja(ListaNum)