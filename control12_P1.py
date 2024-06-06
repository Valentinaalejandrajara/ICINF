listapuntajes = []
for dia in range(1, 16):
    puntaje = -1
    while puntaje < 0 or puntaje > 100:
        puntaje = int(input("Ingrese el puntaje del día " + str(dia) + " (de 0 a 100): "))
        if puntaje < 0 or puntaje > 100:
            print("El puntaje debe estar entre 0 y 100")
    listapuntajes.append(puntaje)

print("Días con puntaje mayor o igual a 60 puntos:")
for dia in range(1, 16):
    puntaje = listapuntajes[dia - 1]
    if puntaje >= 60:
        print("Día " + str(dia))

print("Días con puntaje menor a 60 puntos:")
for dia in range(1, 16):
    puntaje = listapuntajes[dia - 1]
    if puntaje < 60:
        print("Día " + str(dia))
