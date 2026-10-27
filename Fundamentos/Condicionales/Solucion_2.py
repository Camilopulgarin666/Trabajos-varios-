print = ("tienda de camisas")
tienda_2 = input("Tengo disponible en el catalogo:\nCamiseta Manga Sisa\nCamiseta Manga Larga")

tipo_camisas = input("¿Que tipo de camisa busca?: ").upper()
cantidad = int(input("¿cuantas camisa busca?: "))

if tipo_camisas == "Camisa Manga larga":
    print("Costo: $45.000")
    total = 45000 * cantidad
    print(f"Total a pagar: {total}")
elif tipo_camisas == "Camisa Manga Sisa":
    print("Costo: $80.000")
    total = 80000 * cantidad
    print(f"Total a pagar: {total}")
else:
    ("Lo siento no tenemos camisas")