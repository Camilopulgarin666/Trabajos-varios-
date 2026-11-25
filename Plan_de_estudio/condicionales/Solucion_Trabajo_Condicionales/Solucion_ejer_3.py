"""

Una cafetería vende dos tipos de bebidas calientes:
• Café Americano: $3.500
• Chocolate con leche: $5.000
Tu reto: Es escribe un programa en Python que haga lo siguiente:
1. Pregunte al usuario si desea ordenar alguna bebida.
2. Si responde que sí, el programa debe preguntar qué tipo de bebida quiere (Americano o Chocolate) y qué cantidad va a llevar. Al final, debe mostrar el total de la cuenta.
3. Si responde que no, debe mostrar un mensaje de despedida que diga que no se realizó ninguna compra.
4. (Opcional para puntos extra): Si escribe un tipo de bebida que no existe, dile que ese producto no está en el menú.

"""
print("-"*50)
print("Bienvenidos a la cafeteria. \nhoy solo tenemos disponible"+
       " a la venta los siguientes productos. \nCafe americano $3.500"+
       "\nChocolate con leche $5.000")  

cliente = input("¿Desea ordenar algo?: ").upper()

if cliente == "SI":
    bebida = input("Cuenteme que bebida desea ordenar?: ").upper()
    cantidad = int(input("¿Cuantos desea?: "))
    if bebida == "CAFE AMERICANO":
        total = cantidad*3500
        print(f"El total de su pedido es: {total}")
    elif bebida == "CAFE CON LECHE":
        total = cantidad*5000
        print(f"El total de su pedido es: {total}")
else:
    print("No se preocupe sera en otra ocasion.")


 