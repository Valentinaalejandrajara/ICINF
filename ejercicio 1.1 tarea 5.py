n = (int(input("Ingrese la cantidad de preguntas que se realizaron: ")))
n1 = (int(input("Ingrese la cantidad de respuestas correctas: ")))
porcentaje = (n1 / n) * 100
if porcentaje >= 95: 
    nivel = "Nivel maximo"
else:
    if porcentaje>= 70:
       nivel = "Nivel medio"
    else:
        if porcentaje >= 40:
         nivel = "Nivel regular"
        else:
             nivel= "Fuera de nivel"
print("El procentaje de las respuestas correctas es:", porcentaje)
print("el nivel es:" , nivel)