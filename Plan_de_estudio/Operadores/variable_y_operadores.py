# Variables y operadores: snake_case, Pascalcase (clase P00)

# Entradas
# Desarrollador, Usuario, Sensor, Base de datos
pago_por_dia = 20       #numero entero   int    integer
apellido = "Pérez"      #texto           str    string
dias_trabajados = 3.5   #num decimal     float  Floating-point-number
despedido = False       #booleano        bool   boolean

# Proceso 
sueldo = pago_por_dia * dias_trabajados
# concatenar
print("Tu sueldo es " + str(sueldo))
print("Tu sueldo es ", (sueldo), "dolares por mes", (despedido))
print(f"Tu sueldo es {sueldo} dolares por mes {despedido}")
# Salida
print(sueldo)
