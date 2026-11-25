"""
Una tienda de mascotas vende bolsas de alimento para dos tipos de animales:
• Comida para Perro: $25.000
• Comida para Gato: $18.000
Tu reto: Escribe un programa en Python con la siguiente lógica:
1. El programa debe preguntar directamente qué tipo de alimento desea comprar el usuario (Perro, Gato o Ninguno).
2. Si elige Perro o Gato, el programa debe solicitar la cantidad de bolsas que desea comprar y mostrar el total a pagar.
3. Si el usuario escribe Ninguno, el programa debe mostrar un mensaje confirmando que no compró nada.
"""
print("-"*50)
print("Muy buenas tardes. \nLes agradecemos por vistar mi tienda. \nManejamos estos productos. \nComida para Perro a $25.000 \nComida para Gato a $18.000")
print("-"*50)
producto = input("¿Que tipo de producto desea compra?: ").upper()
cantidad = int(input("¿cuantos paquetes desea llevar?: "))

if producto == "COMIDA PARA PERRO":
    total = cantidad * 25000
    print(f"Parce el total a pagar seria: {total}")
    venta = input("¿Desea seguir con su compra?: ").upper()
    if venta == "SI":
        print("Perfecto Muchas Gracias Por Su Compra!!") 
    elif venta == "NO":
        print("En otro momento sera.")
    else:
        print("Pienselo y cuando este listo me cuenta")

    
elif producto == "COMIDA PARA GATOS":
    total = cantidad * 18000
    print(f"Parce el total a pagar seria: {total}")
    venta = input("¿Desea seguir con su compra?: ").upper()
    if venta == "SI":
        print("Perfecto Muchas Gracias Por Su Compra!!") 
    elif venta == "NO":
        print("En otro momento sera.")
    else:
        print("Pienselo y cuando este listo me cuenta")
else:
    print("Parce no has comprado nada")


