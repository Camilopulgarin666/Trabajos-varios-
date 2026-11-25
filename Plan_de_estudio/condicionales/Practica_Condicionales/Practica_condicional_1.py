"""
1) Preguntar la edad a un usuario y decir si puede votar
votar o no. mayor a 18 años
2) ademas si tiene mas de 16 años, decir que se puede lanzar como personero

"""
print(50*"-")
print("Antes de votar deben de decir la edad")
edad = int(input("Ingrese su edad: "))


if edad >= 18:
    print ("Estas habilitado para votar")
elif edad >= 16:
        print ("Puedes votar como personero")
else:
    print ("No esta habilidato para votar")

""" 
Averiguar si un numero es negativo, cero o positivo
"""
print (50*"-")
x = int(input("Averigua si este numero es negativo, cero o negativo: "))

if x < 0:
     print("Este numero negativo")
elif x == 0:
     print("Este este es 0")
elif x > 0:
     print("Este numero es positivo")

"""
Desarrolle un algoritmo que permita leer dos numero
y ordenalos de menor a mayor, si es el caso
"""
print(50*"-")
print("Digite los siguientes numeros")

val1 = int(input("Digite valor: "))
val2 = int(input("Digite valor: "))

if val1 > val2:
     print (f"Orden: {val1} Orden: {val2}") 
else:
     print("No digistaste un valor")








