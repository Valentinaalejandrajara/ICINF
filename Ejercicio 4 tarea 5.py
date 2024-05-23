
#Aqui como en la anterior se ocupa el bucle mientras
#Se crea una lista 
sueldos = []
while True:
    sueldo = float(input("Ingrese el sueldo del empleado (ingrese -1 para terminar): "))
    if sueldo == -1:
        break
    if 500000 <= sueldo <= 1500000:
        #Igual que antes, Append se utiliza para agregfar un nuevo elemento al final de la lista, esta modifica la lista original y no crea una nueva
        sueldos.append(sueldo)
    else:
        print("Sueldo fuera del rango permitido ($500,000 a $1,500,000).")

entre_500k_y_900k = sum(1 for s in sueldos if 500000 <= s <= 900000)
mas_de_900k = sum(1 for s in sueldos if s > 900000)
total_gasto = sum(sueldos)

print(f"Empleados que cobran entre $500,000 y $900,000: {entre_500k_y_900k}")
print(f"Empleados que cobran más de $900,000: {mas_de_900k}")
print(f"Total gastado en sueldos: ${total_gasto:.2f}")