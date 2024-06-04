lista =[]
while True:
    print("1. Ingresa un elemento a la lista ")
    print("2. Modifica un elemento de la lista segun el indice")
    print("3. Eliminar un elemento de la lista segun indice")
    print("4. Eliminar el ultimo elemento de la lista")
    print("5. Buscar un elemento de la lista segun el dato(devuelve el indice)")
    print("6. Mostrar todos los elementos de la lista")
    print("7. Salir")
    
    opcion=int(input("Ingrese una opcion: "))
    
    if opcion == 1:
        elemento= input("Ingrese el elemento a la lista:")
        lista.append(elemento)
        print(elemento, "Se añadio a la lista")
    else:
        if opcion == 2:
            indice= int(input("Ingrese el indice del elemento a modificar: "))
            nuevo= int(input("Ingrese el nuevo valor:"))
            lista [indice]= nuevo
            print("El nuevo valor es:", nuevo)
        else:
            if opcion == 3:
                indice= int(input("Ingrese el indice del elemento a eliminar:"))
                elementoE = lista.pop(indice)
                print("Elemento", elementoE, "Elininado de la lista" )
            else:
                if opcion == 4:
                    elementoE= lista.pop()
                    print("el ultimo elemento", elementoE, "fue eliminado de la lista")
                else:
                    if opcion == 5:
                        if elemento in lista:
                            indice= lista. index (elemento)
                            print("El elemento", elemento, "Se encuentra en el indice", indice)
                    else:
                        if opcion == 6:
                            if lista:
                                print("Los elementos de la lista: ")
                                for i, elemento in enumerate(lista):
                                    print(i, elemento)
                        else:
                            if opcion == 7:
                                print("Salir")
                                break
                            else:
                                print("opcion no valida ingrese una opcion del 1 al 7)")
