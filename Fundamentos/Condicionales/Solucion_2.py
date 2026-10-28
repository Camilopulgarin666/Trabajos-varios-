"""
La tienda 2 vende, 2 tipos de camisas:
camisetas: %45.000 y Camisa mga larga: $80.000
Preguntar si quiere comprar camisas, de que tipo y cantidad a comprar.

Mostrar el total a pagar. O si no compró nada.
"""
print ("tienda de camisas")
tienda_2 = input("Tengo disponible en el catalogo:\nCamiseta Manga Sisa\nCamiseta Manga Larga")

tipo_camisas = input("¿Que tipo de camisa busca?: ").upper()
cantidad = int(input("¿cuantas camisa busca?: "))

if tipo_camisas == "CAMISA MANGA LARGA":
    print("Costo: $45.000")
    total = 45000 * cantidad
    print(f"Total a pagar: {total}")
elif tipo_camisas == "CAMISA MANGA SISA":
    print("Costo: $80.000")
    total = 80000 * cantidad
    print(f"Total a pagar: {total}")
else:
    ("Lo siento no tenemos camisas")