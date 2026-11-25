print(50*"-")
print("¿Que temperatura estamos?")

temperatura = int(input("Grados de temperatura: "))

if temperatura <= 15:
    print("El Clima frio")
elif temperatura >= 25:
    print("El Clima es templado") 
else: 
    print("El clima es bochornoso")