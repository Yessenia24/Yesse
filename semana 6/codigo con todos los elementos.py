# Clase base: Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca  # Atributo privado (encapsulación)
        self.modelo = modelo

    # Métodos para acceder al atributo privado
    def get_marca(self):
        return self.__marca

    def set_marca(self, marca):
        self.__marca = marca

    # Método común
    def mostrar_informacion(self):
        return f"Marca: {self.__marca}, Modelo: {self.modelo}"


# Clase derivada: Coche
class Coche(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)  # Herencia
        self.puertas = puertas

    # Sobrescritura del método (polimorfismo)
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Puertas: {self.puertas}"


# Clase derivada: Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    # Sobrescritura del método (polimorfismo)
    def mostrar_informacion(self):
        return f"{super().mostrar_informacion()}, Tipo: {self.tipo}"


# Instancias de las clases
coche = Coche("Toyota", "Corolla", 4)
moto = Moto("Yamaha", "MT-07", "Deportiva")

# Mostrar información
print(coche.mostrar_informacion())
print(moto.mostrar_informacion())

# Uso de encapsulación
print("\nEncapsulación:")
print(f"Marca del coche: {coche.get_marca()}")
coche.set_marca("Honda")
print(f"Nueva marca del coche: {coche.get_marca()}")