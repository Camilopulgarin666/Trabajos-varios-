### OPERADORES ARITMETICOS ###

# Operaciones con enteros
print(3 + 4) # suma
print(3 - 4) # resta
print(3 * 4) # multiplicacion
print(3 / 4) # division
print(10 % 3) # modulo (es el que arroja el residuo de la division)
print(10 // 3) # division pero sin decimales, el resultado sera un entero
print(2 ** 3) # numero elevados
print(2 ** 3 + 3 - 7 / 1 // 4) #ecuciones lineales 

# Operaciones con cadenas de texto
print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))

# Operaciones mixtas
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### OPERADORES COMPARATIVOS ###

# Operaciones con enteros
print(3 > 4) 
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

# Operaciones con cadenas de texto
print("Hola" > "Python") 
print("Hola" < "Python")
print("aaaa" >= "abaa") # Ordenación alfabética por ASCII
print(len("aaaa") >= len("abaa")) # Cuenta caracteres
print("Hola" <= "Python")
print("Hola" == "Hola")
print("Hola" != "Python")

### OPERADORES LOGICOS ###

# Teoria mas afondo https://es.wikipedia.org/wiki/%C3%81lgebra_de_Boole
# Basada en el Álgebra de Boole 
print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or ("Hola" > "Python" and 4 == 4))