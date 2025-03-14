# Diccionario numero 3

estudiantes = {
    "Cris": {"edad": 20, "carrera": "Mecatronica", "promedio": 8.5},
    "Kike": {"edad": 22, "carrera": "Mecatronica", "promedio": 9.0},
    "Alexa": {"edad": 21, "carrera": "Mecatronica", "promedio": 7.0},
    "Lupita": {"edad": 23, "carrera": "Mecatronica", "promedio": 8.9}
    "Aaron": {"edad": 20, "carrera": "Mecatronica", "promedio": 9.7},
    "Victor": {"edad": 22, "carrera": "Mecatronica", "promedio": 9.9},
    "Manuel": {"edad": 21, "carrera": "Mecatronica", "promedio": 7.8},
    "Adal": {"edad": 23, "carrera": "Mecatronica", "promedio": 8.0}
    "Oswaldo": {"edad": 21, "carrera": "Mecatronica", "promedio": 7.5},
    "Roberto": {"edad": 23, "carrera": "Mecatronica", "promedio": 8.9}

print("Diccionario de estudiantes:")
for nombre, detalles in estudiantes.items():
    print(f"{nombre}: {detalles}")

nombre_estudiante = "Cirs"
if nombre_estudiante in estudiantes:
    detalles = estudiantes[nombre_estudiante]
    print(f"\nDetalles de {nombre_estudiante}:")
    print(f"Edad: {detalles['edad']}")
    print(f"Carrera: {detalles['carrera']}")
    print(f"Promedio: {detalles['promedio']}")
else:
    print(f"\nEstudiante {nombre_estudiante} no encontrado en el diccionario.")