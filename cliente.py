class Cliente:
    def __init__(self, nombre, correo):
        if not nombre:
            raise ValueError("El nombre es obligatorio")
        if "@" not in correo:
            raise ValueError("Correo inválido")

        self.__nombre = nombre
        self.__correo = correo

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo

    def mostrar_info(self):
        return f"Cliente: {self.__nombre}, Correo: {self.__correo}"
