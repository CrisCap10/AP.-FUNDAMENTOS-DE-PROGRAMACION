#Instrucciones:
#Crear un Diccionario:
#Crea un diccionario llamado información_personal que contenga información ficticia sobre una persona, incluyendo al menos las claves "nombre", "edad", "ciudad" y "profesion".

#Acceder y Modificar Valores:
#Accede al valor asociado con la clave "ciudad" y modifícalo con una ciudad diferente.
#Agrega una nueva clave-valor al diccionario que represente la "profesión" de la persona.

#Verificar Existencia de Claves:
#Verifica si la clave "teléfono" existe en el diccionario. Si no existe, agrégala con un número de teléfono ficticio.

#Eliminar una Clave:
#Elimina la clave "edad" del diccionario, ya que esa información no es necesaria.

#Imprimir el Diccionario Final:
#Imprime el diccionario resultante después de realizar todas las operaciones.

                                    #DESARROLLO DE LA TAREA
# Crear un diccionario llamado información_personal
informacion_personal ={
    "nombre": "Cristhian Chacha",
    "edad": 20,
    "ciudad": "Riobamba",
    "profesión": "Bachiller"
}

# Acceder al valor asociado con la clave "ciudad" y modificarlo
informacion_personal["ciudad"] = "Guaranda"

# Agregar una nueva clave-valor al diccionario que represente la "profesión" de la persona
informacion_personal["especialidad"] = "Ciencias"

# Verificar si la clave "teléfono" existe en el diccionario
if "teléfono" not in informacion_personal:
    # Agregar la clave "teléfono" con un número de teléfono ficticio
    informacion_personal["teléfono"] = 992405341

# Eliminar la clave "edad" del diccionario
del informacion_personal["edad"]

# Imprimir el diccionario resultante
print(informacion_personal)
