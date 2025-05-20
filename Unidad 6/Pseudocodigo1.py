import re

nombre_programa = input("Introduce el nombre del programa: ")
print("Has iniciado el programa:", nombre_programa)

texto_usuario = input("Escribe una frase o texto: ")

palabras = re.findall(r'\b\w+\b', texto_usuario)  
cantidad_palabras = len(palabras)

print("El texto contiene", cantidad_palabras, "palabras.")