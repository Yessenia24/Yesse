# Este programa calcula el área de un círculo dado su radio

import math

# Pedimos al usuario que ingrese el radio del círculo
radio = float(input("Ingrese el radio del círculo: "))

# Calculamos el área utilizando la fórmula A = πr²
area = math.pi * radio**2

# Mostramos el resultado por pantalla
print("El área del círculo es:", area)