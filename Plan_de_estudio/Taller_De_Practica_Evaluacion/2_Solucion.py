print(50*"-")
print("ingresa tus datos para poder acceder")

edad = int(input("ingrese su edad: "))
mebresia = input("¿Maneja la edad sufienciente? S/N: "). upper() in{"S","SI"}

if edad >= 18 and mebresia == True:
    print("El usuario puede pasar")
else:
    print("No tienes la edad o no tienes membresia")



    