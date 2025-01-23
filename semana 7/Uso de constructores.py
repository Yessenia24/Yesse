class Registro:
    def __init__(self, nombre_archivo):
        # Constructor: Inicializa el objeto
        self.nombre_archivo = nombre_archivo
        self.archivo = open(nombre_archivo, "a")
        print("Se ha creado un nuevo registro en el archivo:", nombre_archivo)

    def escribir(self, mensaje):
        self.archivo.write(mensaje + "\n")
        print("Mensaje escrito en el registro:", mensaje)

    def __del__(self):
        # Destructor: Cierra el archivo al finalizar el objeto
        self.archivo.close()
        print("Se ha cerrado el archivo de registro:", self.nombre_archivo)

# Creación de un objeto Registro
registro1 = Registro("mi_registro.txt")

# Escritura de mensajes en el archivo
registro1.escribir("Este es el primer mensaje")
registro1.escribir("Este es el segundo mensaje")

# El objeto sale de alcance y se llama al destructor
print("El programa ha terminado.")