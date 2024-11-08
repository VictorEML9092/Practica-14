"""
Created on Tuesday 04/10/24

@author: Victor Mendoza
"""
import random # Modulo random

# Método por inserción para ordenar los números
def metodo_baraja(ListaNum):
    # Empezamos desde el segundo elemento
    for i in range(1, len(ListaNum)):
        valor_actual = ListaNum[i] # Guardamos el valor actual que queremos insertar en su posición correcta
        j = i - 1

        # Desplazamos los elementos mayores hacia la derecha para hacer espacio
        while j >= 0 and ListaNum[j] > valor_actual:
            print(valor_actual,"<",ListaNum[j]) # Se imprime la comparación actual
            ListaNum[j + 1] = ListaNum[j]
            j -= 1  
            print("Si hay cambio")
        
        if ListaNum[j] < valor_actual:
            print(valor_actual,"<",ListaNum[j]) # Se imprime la comparación actual
            print("No hay cambio")
        
        ListaNum[j + 1] = valor_actual # Insertamos el valor actual en su lugar
        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(ListaNum,"\n")

ListaNum = random.sample(range(1, 51), 6) # Se genera una lista de "n" números únicos del 1 al 50

print("La lista de números a ordenar por el método Baraja es:\n")
print(ListaNum,"\n")
metodo_baraja(ListaNum)