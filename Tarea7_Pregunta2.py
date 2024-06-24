

def cargar():
    lista=[]
    while True:
       valor=input("Ingrese las palabras: ")
       if valor=="":
           break
       lista.append(valor)
    return lista


def cantidad(palabras):
    cant=0
    for x in range(len(palabras)):
        if palabras[x]=="a" or palabras[x]=="A":
            cant=cant+1
    return cant

lista_palabras=cargar()
for palabra in lista_palabras:
    cant_a= cantidad(palabra)
    print("La palabras", palabra,"tiene", cant_a, "Letras A o a")