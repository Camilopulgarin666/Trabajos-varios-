"""
E2:
Las notas de algoritmos tienen los siguientes porcentajes.
Nota1 vale el 30%		<< nota1 * 30 / 100 >>	ó	 << nota1 * 0.3 >>
Nota2 vale el 32%		<< nota2 * 30 / 100 >>	ó	 << nota2 * 0.3 >>
Nota3 vale el 38%		<< nota3 * 30 / 100 >>	ó	 << nota3 * 0.3 >>

Calcula la nota final.
"""

nota_1 = float(input ("Naruto: "))
nota_2 = float(input ("Popeye: "))
nota_3 = float(input ("ichigo: "))

total = (nota_1 * 30, nota_2 * 30, nota_3 * 30) 

total_2=(total/10)

print (f"calculo notas por persona: {total}")
print (f"calculo total: {total_2}")