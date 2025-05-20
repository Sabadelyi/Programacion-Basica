import re

texto = input("Introduce un texto para analizar: ")

texto = texto.strip()

contador_vocales = 0
contador_consonantes = 0
contador_numeros = 0
contador_otros = 0

vocales = "aeiouáéíóú"
consonantes = "bcdfghjklmnpqrstvwxyz"
numeros = "0123456789"

for caracter in texto:
    caracter = caracter.lower()  
    if caracter in vocales:
        contador_vocales += 1
    elif caracter in consonantes:
        contador_consonantes += 1
    elif caracter in numeros:
        contador_numeros += 1
    else:
        contador_otros += 1  

print("Vocales:", contador_vocales)
print("Consonantes:", contador_consonantes)
print("Números:", contador_numeros)
print("Otros caracteres:", contador_otros)