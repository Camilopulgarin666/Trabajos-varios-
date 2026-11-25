#Condicionales..completos: if ... elif ... else
#                          si    sino-si   sino
print("-"*50)
dinero = 50000
desayunar = input("Opciones de desayuno:\nHamburgesa\nBuñuelos\nPescado\nEscriba lo que desea: ").upper ()

if desayunar == "HAMBURGUESA":
    #anidamineto, condicional dentro de otro...
    if dinero > 20000:
            print("Costo: $25.000")
    else:
            print("Costo: $15.000")
elif desayunar == "HUEVOS":
    print("Costo: $9.000")
elif desayunar == "BUEÑUELOS":
    print("Costo: $20.000")
elif desayunar == "PESCADOS":
    print("Costo: $27.000")
else:
    print("No tengo de eso...")

