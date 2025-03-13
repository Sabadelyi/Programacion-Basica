# Programacion Basica

## Sabayd de Jesus Mascorro Lopez

### Unidad 1

¿Qué tipos de clasificación de software hay?
¿Qué es un algoritmo?
¿Qué es un lenguaje de programación?
¿Qué es un paradigma de programación?
¿Cuál es la diferencia entre un lenguaje interpretado y copilado?
¿Qué es un lenguaje de alto nivel y bajo nivel?

### Unidad 2

# Operadors
a = 10
b = 3
suma = a + b      # 10 + 3 = 13
resta = a - b     # 10 - 3 = 7
multiplicacion = a * b  # 10 * 3 = 30
division = a / b  # 10 / 3 = 3.333...
division_entera = a // b  # 10 // 3 = 3
potencia = a ** b  # 10^3 = 1000
#Operadors

# if
if opcion == "1":
        tarea = input("📝 Escribe la nueva tarea: ")
        tareas.append(tarea)
        print(f"✅ Tarea '{tarea}' agregada.")

# Else
else:
            num = int(input("🔹 Número de la tarea completada: ")) - 1
            if 0 <= num < len(tareas):
                print(f"✔️🤓 Tarea '{tareas[num]}' completada y eliminada.")
                tareas.pop(num)
            else:
                print("❌  Número inválido.")

# Elsaif

if condition1:
    # Código si condition1 es verdadera
elif condition2:
    # Código si condition2 es verdadera
else:
    # Código si ninguna condición anterior es verdadera

# While

while True:
    print("\n📋 MENÚ DE TAREAS 📋")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

# For

for item in my_list:
    print(item)
for i in range(5, 15, 2):  # De 5 a 15, saltando de 2 en 2
    print(i)
for i in range(3):
    for j in range(3):
        print(f"Elemento en posición {i}, {j}")

# Librerias

import math

print(math.sqrt(25))

# Tipo de Datos

entero = 5
flotante = 1.2
cadena = "Ed Flores"
booleano = True

print("Imprime los tipos de datos")
print("Entero = ", entero)
print("Cadena = ", cadena)
print("flotante =", flotante)
print("Booleano =", booleano)

# Switch (Programacion)

def switch_example(option):
    switcher = {
        1: "Option 1 selected",
        2: "Option 2 selected",
        3: "Option 3 selected",
    }
    return switcher.get(option, "Invalid option")

Example usage
option = int(input("Enter an option (1-3): "))
print(switch_example(option))

### Unidad 3

# Lista de números
numeros = [1, 2, 3, 4, 5]

# Lista de cadenas
nombres = ["saba", "kike", "cris"]

# Lista con diferentes tipos de datos
mixta = [10, "Python", True, 3.14]

# Lista vacía
vacia = []

print(numeros)
print(nombres)
print(mixta)
print(vacia)


input("Presiona Enter para continuar...")

# Lista vacía para almacenar los productos
lista_compras = []

print("🛒 Lista de Compras 🛒")

# Agregar productos
producto1 = input("Agrega el primer producto: ")
lista_compras.append(producto1)

producto2 = input("Agrega el segundo producto: ")
lista_compras.append(producto2)

producto3 = input("Agrega el tercer producto: ")
lista_compras.append(producto3)

# Mostrar la lista completa
print("\n📌 Tu lista de compras es:")
for producto in lista_compras:
    print(f"- {producto}")

print("\n✅ ¡Lista creada con éxito!")

# Lista vacía para almacenar las tareas
tareas = []

while True:
    print("\n📋 MENÚ DE TAREAS 📋")
    print("1. Agregar tarea")
    print("2. Ver tareas")
    print("3. Marcar tarea como completada")
    print("4. Eliminar tarea")
    print("5. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        tarea = input("📝 Escribe la nueva tarea: ")
        tareas.append(tarea)
        print(f"✅ Tarea '{tarea}' agregada.")

    elif opcion == "2":
        if not tareas:
            print("📭 No hay tareas pendientes.")
        else:
            print("\n📌 Lista de Tareas:")
            for i, tarea in enumerate(tareas, 1):
                print(f"{i}. {tarea}")

    elif opcion == "3":
        if not tareas:
            print("📭 No hay tareas para completar.")
        else:
            num = int(input("🔹 Número de la tarea completada: ")) - 1
            if 0 <= num < len(tareas):
                print(f"✔️🤓 Tarea '{tareas[num]}' completada y eliminada.")
                tareas.pop(num)
            else:
                print("❌  Número inválido.")

    elif opcion == "4":
        if not tareas:
            print("📭 No hay tareas para eliminar.")
        else:
            num = int(input("🗑️ Número de la tarea a eliminar: ")) - 1
            if 0 <= num < len(tareas):
                print(f"🗑️ Tarea '{tareas[num]}' eliminada.")
                tareas.pop(num)
            else:
                print("❌ Número inválido.")

    elif opcion == "5":
        print("👋 Saliendo del programa. ¡Hasta luego!")
        break

    else:
        print("❌ Opción inválida. Intenta de nuevo.")

# Lista nombres
nombres = ["Cristian", "Enrique", "Oswaldo", "Roberto", "Adal", "Alejandro", "Manuel", "Aaron", "Lupita", "Alexa"]

# Lista edades
edades = [18, 18, 18, 18, 18, 18, 18, 18, 18, 18]

# Lista materias
materias = ["Programacion Basica", "Calculo Diferencial", "Algebra lineal", "Contabilidad", 
            "Estadistica y control de Calidad", "Materiales", "Ingles"]

# Lista maestros
maestros = ["Enrique", "Eduardo", "Marlen", "Cecilia", "Jorge", "Martha"]

print(len(nombres)) 
print(max(edades))  
print(min(edades))  
nombres.sort()  
print(nombres)


materias.remove("Programacion Basica")  
print(materias)
materias.append("Programacion Avanzada")  
materias.append([1, "Programacion Basica"])  
print(materias)

for Materias in materias:
	print(Materias)

# Diccionarios
