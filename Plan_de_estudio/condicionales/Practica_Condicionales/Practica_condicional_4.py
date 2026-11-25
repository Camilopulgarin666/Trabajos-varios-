num = int(input("Ingrese un numero: "))
decenas = num // 10 
unidades = num % 10

if decenas == 1:
    romanos_decena = "X"
elif decenas == 2:
    romanos_decena = "XX"
elif decenas == 3:
    romanos_decena = "XXX"
elif decenas == 4:
    romanos_decena = "XL"
elif decenas == 5:
    romanos_decena = "L"
elif decenas == 6:
    romanos_decena = "LX"
elif decenas == 7:
    romanos_decena = "LXX"
elif decenas == 8:
    romanos_decena = "LXXX"
elif decenas == 9:
    romanos_decena = "XC"
elif decenas == 10:
    romanos_decena = "C"      

if unidades == 1:
    romanos_unidades = "I"
elif unidades == 2:
    romanos_unidades = "II"
elif unidades == 3:
    romanos_unidades = "III"
elif unidades == 4:
    romanos_unidades = "IV"
elif unidades == 5:
    romanos_unidades = "V"
elif unidades == 6:
    romanos_unidades = "VI"
elif unidades == 7:
    romanos_unidades = "VII"
elif unidades == 8:
    romanos_unidades = "VIII"
elif unidades == 9:
    romanos_unidades = "IX"

print(f"{romanos_decena}{romanos_unidades}")

