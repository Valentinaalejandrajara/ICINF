lista = []

for x in range(10):
    precios = float(input("Ingresa el precio del producto en dólares: "))
    lista.append(precios)

dolar = 950
lista1 = []

for precios in lista:
    precios1 = precios * dolar
    lista1.append(precios1)


print("Precios en pesos chilenos:", lista1)
