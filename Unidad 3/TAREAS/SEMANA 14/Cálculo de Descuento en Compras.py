#Creación de la Función:
# una función llamada calcular_descuento que tome dos parámetros: el monto total de la compra y un valor predeterminado para el porcentaje de descuento (por ejemplo, 10% por defecto).
#La función debe calcular el descuento aplicando el porcentaje al monto total de la compra.
#La función debe devolver el monto del descuento calculado.
#Llamada a la Función:
#Llama a la función calcular_descuento al menos dos veces desde el programa principal.
#En una llamada, proporciona el monto total de la compra y, en la otra, proporciona tanto el monto total de la compra como el porcentaje de descuento.
#Salida de Resultados:
#Muestra los resultados de las llamadas a la función, incluyendo el monto del descuento y el monto final a pagar después del descuento.

def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento/100)
    return descuento

if __name__ == "__main__":
    monto1=1700
    monto2=2500

# Llamada 1: Proporciona el monto total de la compra y el porcentaje de descuento

    descuento1 = calcular_descuento(monto1)
    print(f"Monto total de la compra: ${monto1}, el descuento es: {descuento1}")

# Llamada 2: Proporciona solo el monto total de la compra (porcentaje de descuento es el valor predeterminado)
    porcentaje_descuento = 45
    descuento2 = calcular_descuento(monto2, porcentaje_descuento)
    print(f"Monto total de la compra: ${monto2}, el descuento es: {descuento2}")
