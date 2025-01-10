class Cliente:
    """
    Representa un cliente del hotel.
    """
    def __init__(self, nombre, identificacion, telefono, correo):
        """
        Inicializa un cliente con sus datos básicos.
        """
        self.nombre = nombre
        self.identificacion = identificacion
        self.telefono = telefono
        self.correo = correo

    def mostrar_informacion(self):
        """
        Muestra la información completa del cliente.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Identificación: {self.identificacion}")
        print(f"Teléfono: {self.telefono}")
        print(f"Correo: {self.correo}")

# Ejemplo de uso:
if __name__ == "__main__":
    cliente1 = Cliente("Juan Pérez", "1723456789", "0998765432", "juan.perez@mail.com")
    cliente1.mostrar_informacion()
