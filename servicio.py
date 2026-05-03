from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre):
        self.nombre = nombre

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def descripcion(self):
        pass


class ReservaSala(Servicio):
    def __init__(self, horas):
        super().__init__("Reserva de Sala")
        if horas <= 0:
            raise ValueError("Horas inválidas")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 50

    def descripcion(self):
        return f"Reserva de sala por {self.horas} horas"


class AlquilerEquipo(Servicio):
    def __init__(self, dias):
        super().__init__("Alquiler de Equipo")
        if dias <= 0:
            raise ValueError("Días inválidos")
        self.dias = dias

    def calcular_costo(self):
        return self.dias * 30

    def descripcion(self):
        return f"Alquiler de equipo por {self.dias} días"


class Asesoria(Servicio):
    def __init__(self, horas):
        super().__init__("Asesoría")
        if horas <= 0:
            raise ValueError("Horas inválidas")
        self.horas = horas

    def calcular_costo(self):
        return self.horas * 100

    def descripcion(self):
        return f"Asesoría por {self.horas} horas"
