# PROGRAMA 1: Conversión de pies a pulgadas, yardas, cm y metros

def convertir_pies(pies, opcion):
    if opcion == 1:
        return pies * 12  # pulgadas
    elif opcion == 2:
        return pies / 3  # yardas
    elif opcion == 3:
        return pies * 12 * 2.54  # centímetros
    elif opcion == 4:
        return pies * 12 * 2.54 / 100  # metros
    else:
        return "Opción no válida"

pies = float(input("Ingresa la medida en pies: "))
print("Elige la conversión que deseas realizar:")
print("1. Pulgadas")
print("2. Yardas")
print("3. Centímetros")
print("4. Metros")
opcion = int(input("Opción: "))

resultado = convertir_pies(pies, opcion)
print(f"Resultado de la conversión: {resultado}")


# PROGRAMA 2: Resolución de ecuación de segundo grado (fórmula cuadrática)

import cmath

def resolver_ecuacion(a, b, c):
    discriminante = b**2 - 4*a*c
    raiz1 = (-b + cmath.sqrt(discriminante)) / (2*a)
    raiz2 = (-b - cmath.sqrt(discriminante)) / (2*a)
    return raiz1, raiz2

a = float(input("Ingresa el valor de a: "))
b = float(input("Ingresa el valor de b: "))
c = float(input("Ingresa el valor de c: "))

raiz1, raiz2 = resolver_ecuacion(a, b, c)
print(f"Las soluciones de la ecuación son: {raiz1} y {raiz2}")


# PROGRAMA 3: Conversión de un número decimal a binario

def convertir_a_binario(decimal):
    return bin(decimal)[2:]

decimal = int(input("Ingresa un número decimal: "))
binario = convertir_a_binario(decimal)
print(f"El número {decimal} en binario es: {binario}")


# PROGRAMA 4: Conversión de temperatura a Celsius, Kelvin, y Rankine

def convertir_temperatura(fahrenheit, opcion):
    if opcion == 1:
        return (fahrenheit - 32) * 5/9  # Celsius
    elif opcion == 2:
        return (fahrenheit - 32) * 5/9 + 273.15  # Kelvin
    elif opcion == 3:
        return fahrenheit + 459.67  # Rankine
    else:
        return "Opción no válida"

fahrenheit = float(input("Ingresa la temperatura en Fahrenheit: "))
print("Elige la conversión que deseas realizar:")
print("1. Celsius")
print("2. Kelvin")
print("3. Rankine")
opcion = int(input("Opción: "))

resultado = convertir_temperatura(fahrenheit, opcion)
print(f"Resultado de la conversión: {resultado}")


# PROGRAMA 5: Contar números positivos y negativos en una serie de números

def contar_positivos_negativos(numeros):
    positivos = sum(1 for num in numeros if num > 0)
    negativos = sum(1 for num in numeros if num < 0)
    return positivos, negativos

numeros = []
print("Ingresa los números (escribe 'fin' para terminar):")
while True:
    entrada = input()
    if entrada.lower() == 'fin':
        break
    else:
        numeros.append(float(entrada))

positivos, negativos = contar_positivos_negativos(numeros)
print(f"Números positivos: {positivos}, Números negativos: {negativos}")
