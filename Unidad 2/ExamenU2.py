import random

''' 
Programa #1: Adivina el número.
El programa debe generar un número aleatorio entre 1 y 10 y el usuario debe adivinarlo. Si el usuario adivina el número, el programa debe mostrar un mensaje de felicitaciones y el número de intentos que le tomó al usuario adivinar el número. 
Si el usuario no adivina el número, el programa debe mostrar un mensaje indicando si el número secreto es mayor o menor al número ingresado por el usuario.
'''

numero_secreto = random.randint(1, 10)
intentos = 0
adivinado = False

print("🎯 ¡Bienvenido al juego de Adivina el Número!")
print("Tienes que adivinar un número entre 1 y 10.")

# Bucle while hasta que el usuario adivine el número
while not adivinado:
    intento = int(input("Ingresa tu intento: "))
    intentos += 1

    if intento == numero_secreto:
        print(f"🎉 ¡Felicidades! Adivinaste el número en {intentos} intentos.")
        adivinado = True  # Salir del bucle
    elif intento > numero_secreto:
        print("🔽 El número es menor. Intenta de nuevo.")
    else:
        print("🔼 El número es mayor. Intenta de nuevo.")


""" Conteste las siguientes preguntas después de hacer funcionar el código anterior:

1. ¿Qué hace la función randint() del módulo random?
Genera un número entero aleatorio dentro del rango especificado.

2. ¿Qué tipo es la variable intentos?
Es de tipo int (entero), ya que empieza en 0 y se incrementa con cada intento.

3. ¿Qué estamos haciendo en la línea 1?
Estamos importando el módulo random, lo que nos permite usar
funciones para generar valores aleatorios, como randint().

4. ¿Mencione los operadores que se utilizan en el código?
1:Operadores de comparación: ==, >, < (para comparar el número secreto con el intento).
2:Operador de asignación: = (para asignar valores a variables).
3:Operador de incremento: += (para aumentar el número de intentos).
4:Operador lógico: not (para la condición en el bucle while).

5. ¿Qué hace la palabra intentos que está entre corchetes?
Nos señala cuantos intentos llevamos tratando de adivinar el codigo

"""