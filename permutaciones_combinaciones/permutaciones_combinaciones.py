#!/usr/bin/env python3
# Escriba un programa para resolver permutaciones y combinaciones
# Desarollado por: Santiago Macías Corzo (sanmacorz)

from math import factorial


def resolver_permutacion(n, r):
    try:
        resultado = int(factorial(n) / factorial(n - r))
        return resultado
    except ValueError:
        print(
            "ERROR! El número de n conjuntos debe ser mayor que el número de r subconjuntos!"
        )


def resolver_combinacion(n, r):
    try:
        resultado = int(factorial(n) / (factorial(n - r) * factorial(r)))
        return resultado
    except ValueError:
        print(
            "El número de n conjuntos debe ser mayor que el número de r subconjuntos!"
        )


menu = str(
    input(
        "--INICIO DEL PROGRAMA--\n1. Permutación\n2. Combinación\nIngrese una opción: "
    )
)

if menu == "1":
    n = int(input("Ingrese un número de n conjuntos: "))
    r = int(input("Ingrese un número de r subconjuntos: "))
    resultado = str(resolver_permutacion(n, r))
    print("El resultado de la permutación es: " + resultado)
elif menu == "2":
    n = int(input("Ingrese un número de n conjuntos: "))
    r = int(input("Ingrese un número de r subconjuntos: "))
    resultado = str(resolver_combinacion(n, r))
    print("El resultado de la combinación es " + resultado)
