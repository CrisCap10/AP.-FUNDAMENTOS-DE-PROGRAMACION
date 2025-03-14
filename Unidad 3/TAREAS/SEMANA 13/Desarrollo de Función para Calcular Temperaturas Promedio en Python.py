#Desarrolla una función en Python que calcule la temperatura promedio de una ciudad durante un período de tiempo. La función debe ser capaz de manejar datos de temperaturas de múltiples ciudades y semanas.
#Utiliza como base el ejemplo anterior, donde tenías datos de 3 ciudades durante 4 semanas.
#Tu función debe recibir estos datos como parámetros y calcular la temperatura promedio de cada ciudad.


def calcular_temperatura_promedio(ciudades_temperaturas):

    # Inicializo un diccionario vacío para almacenar los resultados
    temperatura_promedio = {}

    # Recorre cada ciudad en el diccionario
    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Inicializa una lista vacía para almacenar las temperaturas de la ciudad
        temperaturas_ciudad = []

        # Recorre cada semana de la ciudad
        for semana, temperatura_semana in temperaturas.items():
            # Agrega las temperaturas de la semana a la lista de temperaturas de la ciudad
            temperaturas_ciudad.extend(temperatura_semana)

        # Calcula la temperatura promedio de la ciudad
        temperatura_promedio_ciudad = sum(temperaturas_ciudad) / len(temperaturas_ciudad)

        # Almacena la temperatura promedio de la ciudad en el diccionario de resultados
        temperatura_promedio[ciudad] = temperatura_promedio_ciudad

    # Regresa el diccionario de resultados
    return temperatura_promedio


# Ejemplo de uso
ciudades_temperaturas = {
    'Ciudad Guaranda': {
        'Semana 1': [20, 22, 21, 23, 24],
        'Semana 2': [25, 26, 27, 28, 29],
        'Semana 3': [30, 31, 32, 33, 34],
        'Semana 4': [35, 36, 37, 38, 39]
    },
    'Ciudad Ambato': {
        'Semana 1': [15, 17, 16, 18, 19],
        'Semana 2': [20, 22, 21, 23, 24],
        'Semana 3': [25, 26, 27, 28, 29],
        'Semana 4': [30, 31, 32, 33, 34]
    },
    'Ciudad Quito': {
        'Semana 1': [10, 12, 11, 13, 14],
        'Semana 2': [15, 17, 16, 18, 19],
        'Semana 3': [20, 22, 21, 23, 24],
        'Semana 4': [25, 26, 27, 28, 29]
    }
}

temperatura_promedio = calcular_temperatura_promedio(ciudades_temperaturas)

# Imprime la temperatura promedio de cada ciudad
for ciudad, temperatura in temperatura_promedio.items():
    print(f"La temperatura promedio de {ciudad} es {temperatura}°C")