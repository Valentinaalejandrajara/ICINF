
#def se usa para definir una funcion, marca el comienzo de la definificion de una funcion
def calcular_altura_promedio():
#Se crea una lista vacia "Alturas" para almacenar que se ingresaran
    alturas = []
    #Se inicia el blucle para ingresar alturas
    #Bucle mientras, en resumen el bucle termina cuando se ingresa 0
    while True:
        altura = float(input("Ingrese una altura en metros (0 para terminar): "))
        #Si el usuario ingresa 0 se termina el blucle
        if altura == 0:
            break
        #Append se utiliza para agregfar un nuevo elemento al final de la lista, esta modifica la lista original y no crea una nueva
        alturas.append(altura)

    if alturas:
        # Se calcula el promedio sumando las alturas y dividiendo por la cantidad de elementos
        promedio = sum(alturas) / len(alturas)
        #Se devuelve el resultado
        return promedio
    else:
        # Si la lista está vacía, devolvemos None
        return None

promedio = calcular_altura_promedio()
# Verificamos si el promedio no es None y mostramos el resultado
if promedio is not None:
    print(f"Altura promedio: {promedio:.2f} metros")
else:
    print("No se ingresaron alturas.")
