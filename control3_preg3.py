
def potencia(num, exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return num
    else:
        return num * potencia(num, exp - 1)

num = int(input("ingresa un número: "))
exp = int(input("ingresa un exponente: "))
resultado = potencia(num, exp)
print("El resultado es: ", resultado)
