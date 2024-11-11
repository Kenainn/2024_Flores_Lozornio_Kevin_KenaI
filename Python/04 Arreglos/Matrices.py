# Definicion de matrices
def ingresar_matriz():
    matriz = []
    print("Introduce los valores de la matriz 3x3")
    for i in range(3):
        fila = []
        for j in range(3):
            valor = float(input(f"elemento : [{1 + i}][{1 + j}]: "))
            fila.append(valor)
        matriz.append(fila)
    return matriz

def sumar_matriz(matriz1, matriz2):
    '''
    Función que suma dos matrices cuadradas 
    Parámetros:
        matriz1: float 
        matriz2: float 
    '''
    matriz_suma = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz1[i][j] + matriz2[i][j])
        matriz_suma.append(fila)
    return matriz_suma

def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Transposición de las matrices
def trans(matriz):
    matriz_transpuesta = []
    for i in range(3):
        fila = []
        for j in range(3):
            fila.append(matriz[j][i])
        matriz_transpuesta.append(fila)
    return matriz_transpuesta

# Resultado de las matrices
print("Matriz 1")
matriz1 = ingresar_matriz()
print("Matriz 2")
matriz2 = ingresar_matriz()

# Suma de las matrices
matriz_resultado = sumar_matriz(matriz1, matriz2)
print("El resultado de la suma es:")
imprimir_matriz(matriz_resultado)

# Transposición de la matriz resultante
matriz_transpuesta = trans(matriz_resultado)
print("La matriz transpuesta es:")
imprimir_matriz(matriz_transpuesta)
