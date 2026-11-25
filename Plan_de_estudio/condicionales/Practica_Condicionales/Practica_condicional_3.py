"""
Soliscitar 3 numeros y averiguar cual es el mayor de los tres 
Nota: NO USAR: AND, OR.
Insertar datos de prueba asi:
1   2   3
1   3   2
2   1   3
2   3   1
3   1   2
3   2   1

Getbootstrap.com
gamma.app
"""

print(50*"-")
print(""" averigue cual es el mayor de los 
1   2   3
1   3   2.
2   1   3
2   3   1
3   1   2
3   2   1.
""")

datos1 = int(input("Numero: "))
datos2 = int(input("Numero: "))
datos3 = int(input("Numero: "))

if datos1>datos2:
    if datos1>datos3:
        print(f"{datos1} es mayor")
if datos3>datos2:
    if datos3>datos1:
        print(f"{datos3} es mayor")
if datos2>datos1:
    if datos2>datos3:
        print(f"{datos2} es mayor")


    
        


    



    
    
    

