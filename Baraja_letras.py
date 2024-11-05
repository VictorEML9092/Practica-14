"""
Created on Tuesday 05/10/24

@author: Victor Mendoza
"""
import random # Modulo random

# Método por inserción para ordenar letras
def metodo_baraja(Listaletras):
    # Empezamos desde el segundo elemento
    for i in range(1, len(Listaletras)):
        letra_actual = Listaletras[i] # Guardamos la letra actual que queremos insertar en su posición correcta
        j = i - 1

        # Desplazamos los elementos mayores hacia la derecha para hacer espacio
        while j >= 0 and Listaletras[j] > letra_actual:
            print(letra_actual,"<",Listaletras[j]) # Se imprime la comparación actual
            Listaletras[j + 1] = Listaletras[j]
            j -= 1  
            print("Si hay cambio")
        
        if Listaletras[j] < letra_actual:
            print(letra_actual,"<",Listaletras[j]) # Se imprime la comparación actual
            print("No hay cambio")
        
        Listaletras[j + 1] = letra_actual # Insertamos el valor actual en su lugar
        print(f"\nLa lista queda así después de la pasada {i + 1}:\n")
        print(Listaletras,"\n")

Listaletras = random.sample('abcdefghijklmnopqrstuvwxyz', 6)  # Se genera una lista con "n" letras únicas del alfabeto

print("La lista de letras a ordenar por el método Baraja es:\n")
print(Listaletras,"\n")
metodo_baraja(Listaletras)