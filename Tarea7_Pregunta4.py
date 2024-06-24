def crear_diccionario_deudores():
    deudores = {}
    print("Ingrese el RUT y la deuda de 5 personas:")
    for _ in range(5):
        rut = input("RUT: ")
        deuda = float(input("Deuda en pesos: "))
        deudores[rut] = deuda
    return deudores

def gestionar_abonos(deudores):
    while True:
        rut = input("Ingrese el RUT del deudor (o presione Enter para finalizar): ")
        if rut == "":
            break
        if rut not in deudores:
            print("RUT no encontrado en la lista de deudores.")
            continue
        abono = float(input("Ingrese el monto del abono para " + rut + ": "))
        if abono >= deudores[rut]:
            del deudores[rut]
        else:
            deudores[rut] -= abono

def mostrar_deudores(deudores):
    print("")
    print("Deudores restantes:")
    for rut in deudores:
        print("RUT:", rut, "- Deuda restante:", deudores[rut], "pesos")


deudores = crear_diccionario_deudores()
gestionar_abonos(deudores)
mostrar_deudores(deudores)

