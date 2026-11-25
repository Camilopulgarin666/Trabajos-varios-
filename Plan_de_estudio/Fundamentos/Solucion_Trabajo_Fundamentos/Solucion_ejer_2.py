"""
Ejercicio 2
Una empresa de tecnología quiere calcular el pago quincenal para sus colaboradores. Crea un programa que solicite:
El apellido del empleado, asegurándote de transformarlo y guardarlo completamente en mayúsculas usando el método de cadena correspondiente.
Los días trabajados en el periodo (número entero).
El pago recibido por día (número decimal).
Si el empleado laboró horas extra durante la quincena (el usuario debe ingresar 'S', 'SI' o 'sí', y debes validarlo como booleano usando un conjunto y el operador in).
El programa debe calcular el sueldo total multiplicando los días trabajados por el pago diario, y mostrar un reporte formateado con el apellido en mayúsculas, el sueldo total y el valor booleano que confirma si realizó horas extra.
"""

apellido_de_empleado = input("Digite su apellido: ").upper()
print(f"Apellido Del Empleado: {apellido_de_empleado}")
dias_trabajados_periodo = int(input("Dias Efectivos Laborados: "))
pago_por_dias = float(input("Valor dia: "))

total = dias_trabajados_periodo * pago_por_dias

horas_extras = input("¿Horas extras S/N?: ")in{"SI","si","Si","sI","s"}
print(f"Horas Extras Laboradas: {horas_extras} Pago Nomina: {total}")
