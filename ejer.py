def areatriangulo(base,altura):
    return base*altura/2

def menu():
    print("        MENU         ")
    print("1. Area del triángulo")
    print("2. Area del cuadrado")
    print("3. Area del círculo")
    print("4. Que edad tengo")
    print("5. Salir")
    opcion = int(input("Escoja la opcion: "))
    return opcion

opcion = menu()
while opcion != 5:
    if opcion == 1 or opcion == 2:
        print("Calculo del area de un Triangulo")
        base = int(input("ingrese la base: " ) )
        altura = int(input("ingrese la altura: "))
        calculo = areatriangulo(base,altura)
        print("Area del triangulo: " + str(calculo) + "\n")
    else:
        print("Opcion no valida\n")

    opcion = menu()