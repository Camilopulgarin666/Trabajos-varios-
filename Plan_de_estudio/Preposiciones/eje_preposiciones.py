# AND, OR, NOT

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))
num3 = int(input("Num3: "))

#                R1             and     C
#        A      and         B   and     C
if ((num1 + 20) == num2) and num1 > num3 and num3 == 5:
    print("Si todo correcto")
elif num3 < num2 and num3 < num1:
    print("cumple....")
else:
    print("ninguno...")

# rangos
# notas: 0-2.5, deficiente, 2.6 y 3.9, bueno, 4 - 5, excelente.

nota = float(input("Digite su nota de algoritmos 0-5: "))

if nota >= 4 and nota <= 5:
    print("Excelente!")
elif nota >= 2.6 and nota < 4:
    print("Buena...")
elif nota >= 0 and nota < 2.6:
    print("Deficiente....")
else:
    print("Fuera de rango...")


# semáforo:  rojo, amarillo, verde

estado = input("Estado del semáforo[rojo, amarillo, verde]: ").lower()
energia = input("Hay energía eléctrica? S/N: ").upper() in {'S'}

if estado == "rojo" and energia == True:
    print("Pare!")
elif estado == "amarillo" and energia == True:
    print("Precaución")
elif estado == "verde" and energia == True:
    print("Siga")
else:
    print("Semáforo malo.")
