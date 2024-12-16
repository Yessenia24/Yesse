# Programación Orientada a Objetos (POO)

class ClimaSemanal:
    def __init__(self):
        self.temperaturas = []

    def ingresar_temperaturas(self):
        print("Ingrese las temperaturas diarias de la semana:")
        for i in range(7):
            temp = float(input(f"Día {i + 1}: "))
            self.temperaturas.append(temp)

    def calcular_promedio(self):
        if not self.temperaturas:
            raise ValueError("No se han ingresado temperaturas.")
        return sum(self.temperaturas) / len(self.temperaturas)

def main_poo():
    clima = ClimaSemanal()
    clima.ingresar_temperaturas()
    promedio = clima.calcular_promedio()
    print(f"El promedio semanal de temperaturas es: {promedio:.2f} grados.")