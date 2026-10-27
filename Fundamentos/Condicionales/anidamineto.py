# Anidamientos de Condicionales
# MOD
# Ejercicio de condicionales
"""
Un usuario desea comprar algo de una tienda:
La tienda 1 vende 2 tipos de zapatos: Formales y Deportyivos
Los formales cuestan $50.000 y los deportivos $300.000
si desea comprar zapatos preguntar de que tipo y cantidad a 
comprar, mostrar el total a pagar

La tienda 2 vende, 2 tipos de camisas:
camisetas: %45.000 y Camisa mga larga: $80.000
Preguntar si quiere comprar camisas, de que tipo y cantidad a comprar.

Mostrar el total a pagar. O si no compró nada.
"""
print("-"*50)
print("Tienda de zapatos")
print("-"*50)
tienda_1 = input("Tengo disponible en el catalogo:\nFormales \nDeportivos")
print("-"*50)
tipo_zapato = input("¿Que tipo de zapatos busca?: ").upper()
cantidad = int(input("¿cuantos zapatos busca?: "))

if tipo_zapato == "FORMALES":
    print("Costo: $50.000")
    total = 50000*cantidad
    print(f"Total a pagar: {total}")
elif tipo_zapato == "DEPORTIVOS":
    print("Costo: $300.000")
    total = 30000*cantidad
    print(f"Total a pagar: {total}")
else:
    ("Lo siento no tenemos esos zapatos")









