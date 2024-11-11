# ALGORITMO 1: Escritura de los primeros 100 números naturales usando MIENTRAS

def numeros_mientras():
    i = 1
    while i <= 100:
        print(i)
        i += 1

# Llamar a la función
while True:
    numeros_mientras()
    repetir = input("¿Deseas repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break


# ALGORITMO 2: Escritura de los primeros 100 números naturales usando PARA

def numeros_para():
    for i in range(1, 101):
        print(i)

# Llamar a la función
while True:
    numeros_para()
    repetir = input("¿Deseas repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break


# ALGORITMO 3: Mostrar solo los números impares entre 1 y 100

def numeros_impares():
    for i in range(1, 101):
        if i % 2 != 0:
            print(i)

# Llamar a la función
while True:
    numeros_impares()
    repetir = input("¿Deseas repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break


# ALGORITMO 4: Sumatoria de los números enteros entre 1 y 10

def sumatoria():
    suma = 0
    for i in range(1, 11):
        suma += i
    print(f"La sumatoria de los números del 1 al 10 es: {suma}")

# Llamar a la función
while True:
    sumatoria()
    repetir = input("¿Deseas repetir el proceso? (s/n): ")
    if repetir.lower() != 's':
        break
