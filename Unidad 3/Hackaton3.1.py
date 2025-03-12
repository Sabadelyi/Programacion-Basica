# Preguntar si deseas realizar el mandado
respuesta = input("¿Deseas realizar el mandado? (sí/no): ")

if respuesta.lower() == "sí":
    # Preguntar cuántos artículos desea comprar
    cantidad = int(input("¿Cuántos artículos deseas comprar?: "))

    # Crear una lista para guardar los artículos
    lista_articulos = []

    # Pedir los nombres de los artículos
    for i in range(cantidad):
        articulo = input(f"Ingrese el nombre del artículo {i + 1}: ")
        lista_articulos.append(articulo)

    # Imprimir los artículos
    print("\nLos artículos que deseas comprar son:")
    for articulo in lista_articulos:
        print(f"- {articulo}")
else:
    print("¡Tal vez en otro momento!")
