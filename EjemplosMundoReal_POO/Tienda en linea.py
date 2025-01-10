# Clase que representa un cliente
class Cliente:
    def __init__(self, nombre, dni):
        """
        Inicializa un cliente con nombre y DNI.
        :param nombre: Nombre del cliente.
        :param dni: Documento de identidad del cliente.
        """
        self.nombre = nombre
        self.dni = dni

    def __str__(self):
        return f"Cliente: {self.nombre} (DNI: {self.dni})"