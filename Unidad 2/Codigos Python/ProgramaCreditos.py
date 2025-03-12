
creditos = int(input("Ingresa el número de créditos que tienes: "))

if creditos >= 120:
    print("Puedes realizar la residencia.")
elif creditos >= 80:
    print("Puedes realizar el servicio social.")
else:
    print("No tienes suficientes créditos para realizar el servicio social o la residencia.")
