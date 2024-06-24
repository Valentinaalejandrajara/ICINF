def cargar():
    supermercado = {}
    while True:
        producto = input("Ingrese el nombre del producto (o presione Enter para finalizar): ")
        if producto == "":
            break
        cantidad = int(input("Ingrese la cantidad de " + producto + ": "))
        supermercado[producto] = cantidad
    return supermercado

def mostrar_productos(supermercado, factor):
    print("Productos y sus cantidades multiplicadas por", factor)
    for producto in supermercado:
        cantidad_multiplicada = supermercado[producto] * factor
        print(producto + ":", cantidad_multiplicada)

supermercado = cargar()
x = int(input("Ingrese un valor numérico X para multiplicar las cantidades: "))
mostrar_productos(supermercado, x)

