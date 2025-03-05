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
Solo genera un numero random del 1 al 10

2. ¿Qué tipo es la variable intentos?
Es de tipo entero(int) ya que esto ase que cuente los intentos que llevas adivinando el numero

3. ¿Qué estamos haciendo en la línea 1?
Esta importando el modulo random

4. ¿Mencione los operadores que se utilizan en el código?
puse el de asignacion, igual, suma y mayor que

5. ¿Qué hace la palabra intentos que está entre corchetes?
Te da las vese que repitio el el siclo
"""