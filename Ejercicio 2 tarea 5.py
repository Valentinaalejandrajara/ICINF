#Ingrese 2 nombres de pila de 2 personas
#Mostrar los dos nombres y ordenardos alfabeticamente
n = (input("Ingrese el primer nombre de pila: "))
n1 = (input("Ingrese el segundo nombre de pila: "))

nombres = [n, n1]
nombres.sort()


print("Los nombres ordenados alfabeticamente: ")
for nombre in nombres:
    print(nombre)
