
lista= []
while True:
    palabra = input("Ingrese una palabra (presione Enter para finalizar): ")
    if palabra == "":
        break
    lista.append(palabra)

longitud = 0
for palabra in lista:
    if len(palabra) > longitud:
        longitud = len(palabra)
print("La longitud de la palabra más larga es:", longitud)

