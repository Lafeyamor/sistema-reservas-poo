from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva

def main():
    try:
        # Cliente válido
        cliente1 = Cliente("Erney", "erney@email.com")

        # Cliente inválido (error)
        try:
            cliente2 = Cliente("", "correo")
        except Exception as e:
            print("Error creando cliente:", e)

        # Servicios
        servicio1 = ReservaSala(2)
        servicio2 = AlquilerEquipo(3)
        servicio3 = Asesoria(1)

        # Reserva válida
        reserva1 = Reserva(cliente1, servicio1, 2)
        reserva1.confirmar()
        print(reserva1.mostrar())

        # Reserva inválida
        try:
            reserva2 = Reserva(cliente1, servicio2, -1)
        except Exception as e:
            print("Error en reserva:", e)

        # Más operaciones
        reserva3 = Reserva(cliente1, servicio2, 3)
        reserva3.cancelar()
        print(reserva3.mostrar())

        reserva4 = Reserva(cliente1, servicio3, 1)
        reserva4.confirmar()
        print(reserva4.mostrar())

    except Exception as e:
        print("Error general:", e)

if __name__ == "__main__":
    main()
