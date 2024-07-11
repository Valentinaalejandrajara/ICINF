def separar(lista):
    pares = []
    impares = []
    
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    pares.sort()
    impares.sort()
    
    return pares, impares
lista = [4, 7, 2, 9, 3, 8, 5, 6]
pares, impares = separar(lista)
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
