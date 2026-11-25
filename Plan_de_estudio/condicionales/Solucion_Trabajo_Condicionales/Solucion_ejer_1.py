"""
La tienda 2 vende, 2 tipos de camisas:
camisetas: %45.000 y Camisa mga larga: $80.000
Preguntar si quiere comprar camisas, de que tipo y cantidad a comprar.

Mostrar el total a pagar. O si no compró nada.
"""

print("tienda de camisas")
tienda_2 = input("Tengo disponible en el catalogo:\nCamiseta Manga Sisa\nCamiseta Manga Larga")

tipo_camisas = input("¿Que tipo de camisa busca?: ").upper()
cantidad = int(input("¿cuantas camisas busca?: "))

if tipo_camisas == "CAMISETA MANGA LARGA":
    print("Costo: $45.000")
    total = 45000 * cantidad
    print(f"Total a pagar: {total}")
elif tipo_camisas == "CAMISETA MANGA SISA":
    print("Costo: $80.000")
    total = 80000 * cantidad
    print(f"Total a pagar: {total}")
else:
    print("Lo siento no tenemos estipo de camisas")