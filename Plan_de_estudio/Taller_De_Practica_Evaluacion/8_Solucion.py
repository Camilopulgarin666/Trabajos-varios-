print(50*"-")
print("resultados de notas de año final")

estudiate_1 = input("Camilo para asistencia: ").upper() in {"PRESENTE"}
nota1 = float(input("Matematicas: "))
nota2 = float(input("Sociales: "))
nota3 = float(input("Programacion: "))

total = nota1 * 0.30 + nota2 * 0.30 + nota3 * 0.40 
print (50*"-")
if total > 3 and estudiate_1 == True:
    print ("ASISTENCIA: PERFECTO\nFINAL AÑO: APROVADO\n",sep="")
elif total < 3 and estudiate_1 == True:
    print ("ASISTENCIA: PERFECTO\nFINAL AÑO: REPROVADO\n",sep="")
else:
    print ("ASISTENCIA: Falto a clases por ende no se dice su nota")








