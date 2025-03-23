#Crea un nuevo proyecto en PyCharm y un archivo Python para este programa.

#Escribe un programa que incluya una matriz bidimensional (puede ser una matriz pequeña de 3x3) con valores numéricos.

#Implementa una función que realice una búsqueda en la matriz para encontrar un valor específico que definas.

#Muestra un mensaje que indique si el valor se encontró o no, y muestra su posición en la matriz si se encontró.



#defino una matriz 3*3
matriz=[
    [91,82,73],
    [64,55,46],
    [37,28,19]

]

def buscar_valor(matriz,valor):
    #recorrer y buscar el valor
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz[i][j] == valor:
                return i,j #retorna la posición
    return None
#solicito el valor a buscar
numero_buscar=46
#llamo a la función
resultado=buscar_valor(matriz,numero_buscar)

if resultado:
    print(f"el resultado del numero{numero_buscar} se encuentra en la posición {resultado[0]} y {resultado[1]}")
else:
    print(f" el número no se encontró en la matriz")