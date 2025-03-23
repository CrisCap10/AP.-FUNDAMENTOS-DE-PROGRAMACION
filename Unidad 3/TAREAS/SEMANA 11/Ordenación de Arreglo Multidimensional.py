#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

#Escribe un programa que incluya una matriz bidimensional con valores numéricos (puede ser una matriz pequeña de 3x3).

#Implementa una función que ordene una fila específica de la matriz en orden ascendente utilizando un algoritmo de ordenación de tu elección (por ejemplo, Bubble Sort o QuickSort).

#Muestra la matriz original y la matriz con la fila ordenada.

# Definimos una matriz 3x3 con valores numéricos
matriz = [
    [5, 2, 8],
    [3, 1, 6],
    [9, 4, 7]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Definimos una función para ordenar una fila específica de la matriz
def ordenar_fila(matriz, fila):
    # Utilizamos el algoritmo de ordenación QuickSort
    def quicksort(arr):
        if len(arr) <= 1:
            return arr
        pivote = arr[len(arr) // 2]
        left = [x for x in arr if x < pivote]
        middle = [x for x in arr if x == pivote]
        right = [x for x in arr if x > pivote]
        return quicksort(left) + middle + quicksort(right)

    # Ordenamos la fila específica
    matriz[fila] = quicksort(matriz[fila])

# Ordenamos la fila 1 de la matriz
ordenar_fila(matriz, 1)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila 1 ordenada:")
for fila in matriz:
    print(fila)
