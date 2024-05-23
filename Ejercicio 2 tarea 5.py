#Ingrese 2 nombres de pila de 2 personas
#Mostrar los dos nombres y ordenardos alfabeticamente
n = (input("Ingrese el primer nombre de pila: "))
n1 = (input("Ingrese el segundo nombre de pila: "))

#Se crea una lista que contiene los nombres
nombres = [n, n1]
#El comando sort () se utiliza para ordenar los elementos de una lista en orden ascendente
nombres.sort()

#Se ocupa el bucle for para itinerar cada elemento de la lista anterior "nombres"
print("Los nombres ordenados alfabeticamente: ")
for nombre in nombres:
    print(nombre)
    #Cada itineracion, imprime el nombre actual 
