#Escriba un programa en python que permita ingresar 7 nombres de personas en unna lista
#una vez terminado el ingreso debera eliminar de la lista todos los nombres que no terminen con "a" y mostrar la lista resultante
#despues de dicha eliminacion

lista = []
for x in range(7):
    nombre = input("Ingrese el nombre de una persona: ")
    lista.append(nombre)

nombresA= [nombre for nombre in lista if nombre[-1] == "a"]

print("Lista de nombres después de eliminar los que no terminan con 'a' son :", nombresA)




