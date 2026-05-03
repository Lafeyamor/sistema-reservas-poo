from excepciones import ReservaError

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        if duracion <= 0:
            raise ReservaError("Duración inválida")

        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "pendiente"

    def confirmar(self):
        self.estado = "confirmada"

    def cancelar(self):
        self.estado = "cancelada"

    def mostrar(self):
        return f"{self.cliente.get_nombre()} - {self.servicio.descripcion()} - Estado: {self.estado}"
