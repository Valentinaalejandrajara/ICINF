def sumatoria(num):
    if num > 1:
        num = num + sumatoria(num -1)
    return num
num=int(input("Ingrese un numero: "))
print(sumatoria(num))
print(f"El valor final de sumatoria es: {sumatoria(num)}")