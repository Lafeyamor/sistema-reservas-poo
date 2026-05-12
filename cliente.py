# cliente.py

from excepciones import ErrorCliente

class Cliente:
    def __init__(self, nombre, edad, documento, correo):
        try:
            self.set_nombre(nombre)
            self.set_edad(edad)
            self.set_documento(documento)
            self.set_correo(correo)

        except Exception as e:
            raise ErrorCliente(f"Error al crear cliente: {e}")

    # -------------------------
    # VALIDACIONES
    # -------------------------

    def set_nombre(self, nombre):
        if not nombre:
            raise ErrorCliente("El nombre es obligatorio")

        self.__nombre = nombre

    def set_edad(self, edad):
        if not isinstance(edad, int) or edad <= 0:
            raise ErrorCliente("Edad inválida")

        self.__edad = edad

    def set_documento(self, documento):
        if not documento:
            raise ErrorCliente("Documento obligatorio")

        self.__documento = documento

    def set_correo(self, correo):
        if "@" not in correo:
            raise ErrorCliente("Correo inválido")

        self.__correo = correo

    # -------------------------
    # GETTERS
    # -------------------------

    def get_nombre(self):
        return self.__nombre

    def get_edad(self):
        return self.__edad

    def get_documento(self):
        return self.__documento

    def get_correo(self):
        return self.__correo

    # -------------------------
    # MOSTRAR INFORMACIÓN
    # -------------------------

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Edad: {self.__edad}, Correo: {self.__correo}"
