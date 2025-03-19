import os
import time

# Eqjemplo
productos = {"001": "Manzanas", "002": "Plátanos"}
precios = {"001": 10.5, "002": 8.0}

def imprimir_menu():
    print("\n--- Menú de opciones ---")
    print("1. Agregar producto")
    print("2. Eliminar producto")
    print("3. Ver productos")
    print("4. Salir")

def agregar_producto():
    codigo = input("Ingrese el código del producto: ")
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    productos[codigo] = nombre
    precios[codigo] = precio
    print(f"Producto '{nombre}' agregado correctamente.")

def eliminar_producto():
    codigo = input("Ingrese el código del producto a eliminar: ")
    if codigo in productos:
        eliminado = productos.pop(codigo)
        precios.pop(codigo)
        print(f"Producto '{eliminado}' eliminado correctamente.")
    else:
        print("El código ingresado no existe.")

def ver_productos():
    print("\n--- Lista de productos ---")
    for codigo, nombre in productos.items():
        print(f"Código: {codigo}, Producto: {nombre}, Precio: ${precios[codigo]}")

# Ciclo principal
while True:
    imprimir_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()
    elif opcion == "2":
        eliminar_producto()
    elif opcion == "3":
        ver_productos()
    elif opcion == "4":
        print("Saliendo del programa...")
        time.sleep(1)  # Usando la librería time
        break
    else:
        print("Opción no válida. Inténtelo de nuevo.")

    time.sleep(10)  
    os.system("cls" if os.name == "nt" else "clear")  
