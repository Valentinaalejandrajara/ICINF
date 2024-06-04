palabras = []
print("Ingresa una palabra o coloca enter par terminar:")
while True:
    palabra= input("palabra:")
    if palabra=="":
        break
    palabras.append(palabra)
for palabra in palabras:
    vocales= 0
    consonantes= 0
    for letra in palabra:
        if letra.lower() in "aeiou":
            vocales +=1
        else:
            if letra.isalpha():
                consonantes +=1
print("La palabra", palabra, "tiene", vocales,"vocales y",consonantes, "consonantes")
