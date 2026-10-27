"""
E3:
Solicitar al usuario el porcentaje de peso de cada nota.
Luego pedir las notas		<< nota1 * porcentaje1 / 100 >>	 ó	 << nota1 * p0.3 >>
Calcular la nota final.
"""

porcentaje_de_peso_naruto = float(input("costo materia naruto: "))
porcentaje_de_peso_ichigo = float(input("costo materia naruto: "))
porcentaje_de_peso_bleach = float(input("costo materia naruto: "))

notas_1 = float(input("notas naruto: "))
notas_2 = float(input("notas naruto: "))
notas_3 = float(input("notas naruto: "))

total_naruto = (notas_1*porcentaje_de_peso_naruto/100) 
total_ichigo = (notas_2*porcentaje_de_peso_ichigo/100) 
total_bleach = (notas_3*porcentaje_de_peso_bleach/100)

total_de_todos = (total_naruto+total_ichigo+total_bleach)

print (f"Nota final naruto: {total_naruto} Nota final ichigo: {total_ichigo} Nota final bleach: {total_bleach}")
print (f"Notas totales de todos: {total_de_todos}")