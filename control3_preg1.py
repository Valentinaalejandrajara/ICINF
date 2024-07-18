

def solo_numeros(var):
    if var == "":
        return False
    for x in var:
        if x < '0' or x > '9':
            return False
    return True

var = input("ingresa un valor: ")
n= solo_numeros(var)
print(n)
