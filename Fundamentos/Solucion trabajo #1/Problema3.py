"""
jercicio 2
Crea un programa para una empresa de envíos que le pida al empleado su nombre, 
la cantidad de entregas realizadas (número entero), 
el pago recibido por cada entrega (valor con decimales), 
y si el turno fue nocturno (ingresando 'S' o 'N'). 
El programa debe calcular el sueldo total multiplicando 
las entregas por el pago por entrega, y mostrar un mensaje 
final con el valor total recibido y el estado del turno nocturno.
"""
nombre_empleado = input("Nombre colaborador: "). upper()
pedidos_entregados = int(input("numeros de pedidos: "))
ganacias_entregas = float(input("ganacias por pedido: "))
turno = input("turno_laborado S/N: ").upper()

sueldo_total = pedidos_entregados * ganacias_entregas

print = (f"valor total recibido: {sueldo_total} turno actual colaborador: {turno}")