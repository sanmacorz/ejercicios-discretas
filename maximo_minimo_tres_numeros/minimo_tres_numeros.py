#!/usr/bin/env python3
# Determinar el mínimo de tres números

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = int(input("Ingrese otro número: "))

if a < b and a < c:
    menor = a
elif b < a and b < c:
    menor = b
else:
    menor = c

print("El número menor es: " + menor)
