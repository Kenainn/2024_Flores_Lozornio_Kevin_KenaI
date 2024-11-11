import math

# Función para calcular el perímetro y área de un cuadrado
def cuadrado(lado):
    perimetro = 4 * lado
    area = lado ** 2
    return perimetro, area

# Función para calcular el perímetro y área de un rectángulo
def rectangulo(base, altura):
    perimetro = 2 * (base + altura)
    area = base * altura
    return perimetro, area

# Función para calcular el perímetro y área de un pentágono regular
def pentagono(lado):
    perimetro = 5 * lado
    apotema = lado / (2 * math.tan(math.pi / 5))
    area = (perimetro * apotema) / 2
    return perimetro, area

# Función para calcular el perímetro y área de un hexágono regular
def hexagono(lado):
    perimetro = 6 * lado
    apotema = lado / (2 * math.tan(math.pi / 6))
    area = (perimetro * apotema) / 2
    return perimetro, area

# Función para calcular el perímetro y área de un octágono regular
def octagono(lado):
    perimetro = 8 * lado
    apotema = lado / (2 * math.tan(math.pi / 8))
    area = (perimetro * apotema) / 2
    return perimetro, area

# Función para calcular el perímetro y área de un dodecágono regular
def dodecagono(lado):
    perimetro = 12 * lado
    apotema = lado / (2 * math.tan(math.pi / 12))
    area = (perimetro * apotema) / 2
    return perimetro, area

# Menú de selección para el usuario
def menu():
    print("Selecciona la figura para calcular su perímetro y área:")
    print("1. Cuadrado")
    print("2. Rectángulo")
    print("3. Pentágono")
    print("4. Hexágono")
    print("5. Octágono")
    print("6. Dodecágono")
    opcion = int(input("Opción: "))
    return opcion

# Programa principal
while True:
    opcion = menu()

    if opcion == 1:
        lado = float(input("Ingresa el lado del cuadrado: "))
        perimetro, area = cuadrado(lado)
    elif opcion == 2:
        base = float(input("Ingresa la base del rectángulo: "))
        altura = float(input("Ingresa la altura del rectángulo: "))
        perimetro, area = rectangulo(base, altura)
    elif opcion == 3:
        lado = float(input("Ingresa el lado del pentágono: "))
        perimetro, area = pentagono(lado)
    elif opcion == 4:
        lado = float(input("Ingresa el lado del hexágono: "))
        perimetro, area = hexagono(lado)
    elif opcion == 5:
        lado = float(input("Ingresa el lado del octágono: "))
        perimetro, area = octagono(lado)
    elif opcion == 6:
        lado = float(input("Ingresa el lado del dodecágono: "))
        perimetro, area = dodecagono(lado)
    else:
        print("Opción no válida. Intenta de nuevo.")
        continue

    print(f"El perímetro es: {perimetro}")
    print(f"El área es: {area}")

    repetir = input("¿Deseas calcular otra figura? (s/n): ")
    if repetir.lower() != 's':
        break
