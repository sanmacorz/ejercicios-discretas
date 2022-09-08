#!/usr/bin/env python3
# Determinar el máximo de tres números

a = int(input("Ingrese un número: "))
b = int(input("Ingrese otro número: "))
c = int(input("Ingrese otro número: "))

if a > b and a > c:
    mayor = a
elif b > a and b > c:
    mayor = b
else:
    mayor = c

print("El número mayor es: " + mayor)
