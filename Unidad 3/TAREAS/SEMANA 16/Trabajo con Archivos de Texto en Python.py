##Tarea: Trabajo con Archivos de Texto en Python

#En esta tarea, realizarás operaciones de lectura y escritura en archivos de texto en Python. Sigue las instrucciones detalladas a continuación:

#Escritura de Archivo de Texto:

#Crea un nuevo archivo llamado my_notes.txt.
#Escribe al menos tres líneas de notas personales en el archivo.
#Lectura de Archivo de Texto:

#Abre el archivo my_notes.txt.
#Lee el contenido del archivo línea por línea utilizando el metodo adecuado.
#Muestra en la consola cada línea leída.
#Cierre de Archivos:

#Asegúrate de cerrar el archivo my_notes.txt después de realizar las operaciones necesarias.
#Instrucciones Adicionales:

#Utiliza métodos como write() y readline() para manipular el archivo de texto.
#Agrega comentarios explicativos en tu código.

                                            #DESARROLLO DE LA TAREA
# Importar la biblioteca para manipular archivos
import os

# Crear un nuevo archivo llamado my_notes.txt
def crear_archivo():
    try:
        # Abrir el archivo en modo escritura
        archivo = open('my_notes.txt', 'w')
        # Escribe algunas líneas de notas en el archivo
        archivo.write('Esta es la primera nota.\n')
        archivo.write('Esta es la segunda nota.\n')
        archivo.write('Esta es la tercera nota.\n')
        # Cerrar el archivo
        archivo.close()
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Abrir el archivo my_notes.txt y leer su contenido
def leer_archivo():
    try:
        # Abrir el archivo en modo lectura
        archivo = open('my_notes.txt', 'r')
        # Leer el contenido del archivo línea por línea
        linea = archivo.readline()
        while linea:
            # Muestra en la consola cada línea leída
            print(linea.strip())
            # Leer la siguiente línea
            linea = archivo.readline()
        # Cerrar el archivo
        archivo.close()
    except Exception as e:
        print(f'Ocurrió un error: {e}')

# Crear el archivo de notas
crear_archivo()

# Leer el contenido del archivo de notas
leer_archivo()

# Verificar si el archivo existe
if os.path.exists('my_notes.txt'):
    print('El archivo my_notes.txt existe.')
else:
    print('El archivo my_notes.txt no existe.')



