"""
Ejercicio 1
Un gimnasio necesita automatizar el cálculo de la tarifa para sus clientes. Desarrolla un programa que solicite:
El nombre del cliente, asegurándote de transformarlo y guardarlo completamente en minúsculas usando el método de cadena correspondiente.
La cantidad de horas de entrenamiento personalizadas contratadas (número decimal).
El costo por hora (número entero).
Si el cliente cuenta con la membresía "Gold" (el usuario debe ingresar 'S', 'SI' o 'sí', y debes capturarlo como un booleano usando un conjunto y el operador in).
El programa debe calcular el costo total de las horas de entrenamiento y mostrar un mensaje formateado con el nombre en minúsculas, el valor total a pagar y el booleano que indica si tiene la membresía Gold.
"""

nombre = input("Ingrese el nombre del cliente: ").lower()
print(f"Cliente registrado: {nombre}")
horas_entrenamiento = float(input("Horas entrenadas: "))
costo_por_hora = int(input("Costo por hora: "))

Total = horas_entrenamiento * costo_por_hora


mensualiadad = input("membresia S/N: ") in {"S", "s", "SI", "si"}
print(f"Factura por horas: {Total} ¿Membresia Gold?: {mensualiadad}")