def cargar():
    lista=[]
    for x in range(10):
        valor=int(input("Ingrese el valor: "))
        lista.append(valor)
    return lista

def inverso(lista):
    lista_invertida=[]
    for y in range(len(lista)-1, -1, -1):
        lista_invertida.append(lista[y])
    return lista_invertida

lista=cargar()
lista_invertida=inverso(lista)
print("La lista invertida es: ", lista_invertida)
