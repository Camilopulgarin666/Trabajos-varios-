"""
Hacer un programa que pueda dibujar una recta, triangulo o un rectangulo
"""
print(50*"-")

print("     /\\")
print("    /  \\")
print("   /    \\")
print("  /      \\")
print(" /        \\")
print("/          \\")
print("------------")

print(50*"-")
print("************")
print("*          *")
print("*          *")
print("************")

print(50*"-")
print(30*"-","\n",30*"-",sep="")
print(50*"-")
print("*")
print("*")
print("*")
print("*")
print("*")
print("*")
print(50*"-")
print(50*"-")
print("Selecciona una de las siguientes figuras:\ntriangulo\nrectangulo\nrecta")
figura = input("Cual quieres escoger?: ")


if figura == "triangulo":
    
    print("""
         *    
        * *  
       *   * 
      *     *    
     ********* 
""")
elif figura == "rectangulo":

    print("""
    ***********
    *         *
    ***********
""")
elif figura == "recta":

    print("""
    ----------------||
    ----------------||
                    ||
                    ||
                    ||
                    ||
                    ||
                    ||   
""")