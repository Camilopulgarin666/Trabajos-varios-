# Variables y operadores: snake_case, Pascalcase (clase P00)

# Entradas
# Desarrollador, Usuario, Sensor, Base de datos
pago_por_dia = int(input("cuanto gana por dia: "))      
apellidos = input("Digite su apellido: ")       
dias_trabajados = float(input("Cuantos dias trabajo: "))       
despedido = input("Estas despedido? S/N: ")

# Proceso 
sueldo = pago_por_dia * dias_trabajados

# concatenar
print("Tu sueldo es " + str(sueldo))
print("Tu sueldo es ", (sueldo), "dolares por mes", (despedido))
print(f"Tu sueldo es {sueldo} dolares por mes {despedido}")
# Salida
print(sueldo)
