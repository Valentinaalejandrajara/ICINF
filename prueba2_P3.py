



lista = {}

for x in range(5):
    pais = input("Ingresa el nombre del pais: ")
    capital = input("Ingresa la capital de ese pais: ")
    lista[pais] = capital

nombre = input("Ingresa el nombre del turista: ")
paisp = input("Ingresa el pais de procedencia del turista: ")
if paisp in lista:
    capitalp = lista[paisp]



print("El turista con el nombre", nombre, "viene del pais", paisp, "y su capital es", capitalp)
