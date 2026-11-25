#operador in: buscar aguja en pajar,  para capturar boleanos
#                                   Conjunto: set
estudio = input("Estudío S/N: ") in {"S", "S", "SI", "si"}
print(f"¿Estudío?: {estudio}")

es_casado = input("Estado civil: Soltero/Casado: ") in {"Soltero", "Casado"}
print(f"¿Es casado?: {es_casado}")
