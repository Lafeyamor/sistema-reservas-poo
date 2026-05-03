from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva

def main():
    try:
        # Crear cliente
        cliente1 = Cliente("Erney", "erney@email.com")

        # Crear servicios
        servicio1 = ReservaSala(2)
        servicio2 = AlquilerEquipo(3)
        servicio3 = Asesoria(1)

        # Crear reservas
        reserva1 = Reserva(cliente1, servicio1, 2)
        reserva1.confirmar()

        reserva2 = Reserva(cliente1, servicio2, 3)
        reserva2.cancelar()

        reserva3 = Reserva(cliente1, servicio3, 1)
        reserva3.confirmar()

        # Mostrar resultados
        print(reserva1.mostrar())
        print(reserva2.mostrar())
        print(reserva3.mostrar())

    except Exception as e:
        print("Error en el sistema:", e)


if __name__ == "__main__":
    main()
