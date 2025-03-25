from Archivos import leer_diccionarios_de_csv
import os
import time
import csv

def guardar_diccionarios_en_csv(productos):
    """Guarda una lista de diccionarios en un archivo CSV."""
    if not lista_diccionarios:
        print("productos")
        return

productos = {}
precios = {}

def cargar_datos():
    try:
        with open("productos.csv", mode='r', encoding='utf-8') as archivo_csv:
            lector = csv.DictReader(archivo_csv)
            for fila in lector:
                productos[fila["Código"]] = fila["Nombre"]
                precios[fila["Código"]] = float(fila["Precio"])
    except FileNotFoundError:
        print("No se encontró el archivo productos.csv. Se creará uno nuevo al guardar.")

def guardar_datos():
    with open("productos.csv", mode='w', newline='', encoding='utf-8') as archivo_csv:
        escritor = csv.DictWriter(archivo_csv, fieldnames=["Código", "Nombre", "Precio"])
        escritor.writeheader()
        for codigo, nombre in productos.items():
            escritor.writerow({"Código": codigo, "Nombre": nombre, "Precio": precios[codigo]})
    print("Datos guardados en productos.csv exitosamente.")

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
        print(f"Código: {codigo}, Producto: {nombre}, Precio: ${precios[codigo]:.2f}")


if __name__ == "__main__":
    cargar_datos()

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
            guardar_datos()
            print("Saliendo del programa...")
            time.sleep(7)
            break
        else:
            print("Opción no válida. Inténtelo de nuevo.")

        time.sleep(7)  
        os.system("cls" if os.name == "nt" else "clear")

        leer_diccionarios_de_csv(archivos)

datos_leidos = leer_diccionarios_de_csv(productos)
print("Datos leídos del archivo CSV:")
print(datos_leidos)