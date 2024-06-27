#Crear un programa en pyhton que permita al usuario ingresar N notas
#e una lista.Para finalizar debera igresar un 0. una vez finalizado,
#debera mostrar lo siguiente: 1) cantidad de notas 2) promedio de notas
#3)La nota minima 4)la nota maxima


notas = []
nota = float(input("Ingresa una nota 0 para terminar: "))

while nota != 0:
    notas.append(nota)
    nota = float(input("Ingresa una nota 0 para terminar: "))

if len(notas) > 0:
    cantidad = len(notas)
    suma = 0
    nota_minima = notas[0]
    nota_maxima = notas[0]

    for nota in notas:
        suma=suma+ nota
        if nota < nota_minima:
            nota_minima = nota
        if nota > nota_maxima:
            nota_maxima = nota

    promedio = suma / cantidad

    print("Cantidad de notas:", cantidad)
    print("Promedio de notas:", promedio)
    print("La nota mínima:", nota_minima)
    print("La nota máxima:", nota_maxima)
else:
    print("No se ingresaron notas.")
