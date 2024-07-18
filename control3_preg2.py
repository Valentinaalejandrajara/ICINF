
def convierte_negativo(lista):
    listaN= []
    for numero in lista:
        listaN.append(-numero)
    return listaN

n= []
for x in range(10):
    valor = int(input("ingresa el numero: "))
    n.append(valor)

n= convierte_negativo(n)
print(n)
