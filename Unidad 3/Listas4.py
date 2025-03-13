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