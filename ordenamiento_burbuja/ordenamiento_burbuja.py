#!/usr/bin/env python3
# Implementar el algoritmo de ordenamiento de burbuja para una lista de números
import random

# Define la función con el algoritmo a implementar
def ordenamiento_burbuja(lista):
    numero_elementos = len(lista)
    for pasada in range(numero_elementos):
        for elemento in range(0, numero_elementos - pasada - 1):
            if lista[elemento] > lista[elemento + 1]:
                comodin = lista[elemento]
                lista[elemento] = lista[elemento + 1]
                lista[elemento + 1] = comodin
    return lista


# Crea una lista con diez números pseudoaleatorios
numeros = []

for numero in range(0, 10):
    numeros.append(random.randint(0, 100))

# Pasa a la lista por la función y lo imprime en pantalla
print(
    "Lista original: "
    + str(numeros)
    + "\n"
    + "Lista ordenada: "
    + str(ordenamiento_burbuja(numeros))
)
