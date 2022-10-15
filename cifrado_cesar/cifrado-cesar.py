#!/usr/bin/env python3
# Defina dos funciones que permitan cifrar y descifrar un texto utilizando el algoritmo de cifrado césar
# Desarollado por: Santiago Macías Corzo (sanmacorz)

# Define un diccionario con los valores correspondientes para cada letra del alfabeto
alfabeto = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7,
    "I": 8,
    "J": 9,
    "K": 10,
    "L": 11,
    "M": 12,
    "N": 13,
    "Ñ": 14,
    "O": 15,
    "P": 16,
    "Q": 17,
    "R": 18,
    "S": 19,
    "T": 20,
    "U": 21,
    "V": 22,
    "W": 23,
    "X": 24,
    "Y": 25,
    "Z": 26,
}


# Función de cifrado de texto utilizando aritmética módular
def cifrado_texto(texto, n):
    resultado = []
    resultado_texto = []
    # Verifica para cada letra su valor respectivo en el diccionario
    for letra in texto:
        for key, value in alfabeto.items():
            # Cuando se encuentra el valor correspondiente se realiza la operación módular
            if letra.upper() == key:
                resultado.append((value + n) % 27)
    # Una vez con los valores númericos cifrados se pasan a letras
    for numero in resultado:
        for key, value in alfabeto.items():
            if numero == value:
                resultado_texto.append(key)
    # Y se regresa el resultado cifrado como texto alfabetico
    return resultado_texto


# Función de descifrado de texto utilizando aritmética módular
def descifrado_texto(texto, n):
    resultado = []
    resultado_texto = []
    # Verifica para cada letra su valor respectivo en el diccionario
    for letra in texto:
        for key, value in alfabeto.items():
            # Cuando se encuentra el valor correspondiente se realiza la operación módular
            if letra.upper() == key:
                resultado.append((value - n) % 27)
    # Una vez con los valores númericos descifrados se pasan a letras
    for numero in resultado:
        for key, value in alfabeto.items():
            if numero == value:
                resultado_texto.append(key)
    # Y se regresa el resultado descifrado como texto alfabetico
    return resultado_texto


# Pide un valor de entrada
entrada = str(input("Ingrese texto: "))
clave = int(input("Ingrese un número para la clave: "))

# Define a las variables como cadenas de texto
texto_cifrado = ""
texto_descifrado = ""

# Genera una cadena de texto con cada letra cifrada
for letra in cifrado_texto(entrada, clave):
    texto_cifrado += letra

# Genera una cadena de texto con cada letra descifrada
for letra in descifrado_texto(texto_cifrado, clave):
    texto_descifrado += letra

# Devuelve un valor de salida
print(
    "El texto "
    + entrada
    + " se cifra como "
    + texto_cifrado
    + " y se descifra como "
    + texto_descifrado
    + "!"
)
