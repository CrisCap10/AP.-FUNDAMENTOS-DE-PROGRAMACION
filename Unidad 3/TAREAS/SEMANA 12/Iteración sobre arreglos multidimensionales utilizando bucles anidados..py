#Crear una matriz 3D que represente los datos de temperaturas diarias en varias ciudades. En una dimensión, puedes tener diferentes ciudades, en otra dimensión, días de la semana (Lunes, Martes, Miércoles, etc.), y en la tercera dimensión, semanas.
#Dentro de cada celda de la matriz, puedes almacenar las temperaturas diarias para una ciudad en un día específico de una semana determinada.
#Utilizar bucles anidados para calcular el promedio de temperaturas para una ciudad por cada una de las semanas.
#Mostrar el promedio de temperaturas para cada ciudad y semana en la pantalla.

# Definir las ciudades y las semanas
ciudades = ['Guaranda', 'Ambato', 'Quito']
semanas = ['Semana 1', 'Semana 2', 'Semana 3']
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

# Definir las temperaturas diarias para cada ciudad y semana
temperaturas = [
    [
        [20, 22, 21, 23, 24, 25, 26],  # Lunes
        [21, 23, 22, 24, 25, 26, 27],  # Martes
        [22, 24, 23, 25, 26, 27, 28],  # Miércoles
        [23, 25, 24, 26, 27, 28, 29],  # Jueves
        [24, 26, 25, 27, 28, 29, 30],  # Viernes
        [25, 27, 26, 28, 29, 30, 31],  # Sábado
        [26, 28, 27, 29, 30, 31, 32]   # Domingo
    ],
    [
        [18, 20, 19, 21, 22, 23, 24],  # Lunes
        [19, 21, 20, 22, 23, 24, 25],  # Martes
        [20, 22, 21, 23, 24, 25, 26],  # Miércoles
        [21, 23, 22, 24, 25, 26, 27],  # Jueves
        [22, 24, 23, 25, 26, 27, 28],  # Viernes
        [23, 25, 24, 26, 27, 28, 29],  # Sábado
        [24, 26, 25, 27, 28, 29, 30]   # Domingo
    ],
    [
        [15, 17, 16, 18, 19, 20, 21],  # Lunes
        [16, 18, 17, 19, 20, 21, 22],  # Martes
        [17, 19, 18, 20, 21, 22, 23],  # Miércoles
        [18, 20, 19, 21, 22, 23, 24],  # Jueves
        [19, 21, 20, 22, 23, 24, 25],  # Viernes
        [20, 22, 21, 23, 24, 25, 26],  # Sábado
        [21, 23, 22, 24, 25, 26, 27]   # Domingo
    ]
]

# Calcular el promedio de temperaturas para cada ciudad y semana
for i, ciudad in enumerate(ciudades):
    for j, semana in enumerate(semanas):
        promedio = sum(temperaturas[i][k][j] for k in range(7)) / 7  # Seleccionar la semana correcta
        print(f'Promedio de temperaturas en {ciudad} durante {semana}: {promedio:.2f}°C')