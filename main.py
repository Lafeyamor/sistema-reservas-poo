from cliente import Cliente

try:
    cliente1 = Cliente("Miguel", 20, "123", "miguel@gmail.com")
    print(cliente1.mostrar_info())

except Exception as e:
    print(e)

try:
    cliente2 = Cliente("", -5, "", "correo_malo")

except Exception as e:
    print("Error controlado:", e)
    
    
from servicio import ReservaSala, AlquilerEquipo, Asesoria
from reserva import Reserva
from excepciones import ReservaError


def main():

    print("=== SISTEMA DE RESERVAS ===")

    try:

        # ---------------------------------------------------
        # PRUEBA 1: CLIENTE VÁLIDO
        # ---------------------------------------------------
        cliente1 = Cliente("Erney", "erney@email.com")
        print(cliente1.mostrar_info())

        # ---------------------------------------------------
        # PRUEBA 2: OTRO CLIENTE VÁLIDO
        # ---------------------------------------------------
        cliente2 = Cliente("Miguel", "miguel@email.com")
        print(cliente2.mostrar_info())

        # ---------------------------------------------------
        # PRUEBA 3: CLIENTE INVÁLIDO
        # ---------------------------------------------------
        try:
            cliente_error = Cliente("", "correo")
        except Exception as e:
            print("Error creando cliente:", e)

        # ---------------------------------------------------
        # PRUEBA 4: SERVICIOS VÁLIDOS
        # ---------------------------------------------------
        servicio1 = ReservaSala(2)
        servicio2 = AlquilerEquipo(3)
        servicio3 = Asesoria(1)

        print(servicio1.descripcion())
        print(servicio2.descripcion())
        print(servicio3.descripcion())

        # ---------------------------------------------------
        # PRUEBA 5: RESERVA VÁLIDA
        # ---------------------------------------------------
        reserva1 = Reserva(cliente1, servicio1, 2)
        reserva1.confirmar()
        print(reserva1.mostrar())

        # ---------------------------------------------------
        # PRUEBA 6: OTRA RESERVA VÁLIDA
        # ---------------------------------------------------
        reserva2 = Reserva(cliente2, servicio2, 3)
        reserva2.confirmar()
        print(reserva2.mostrar())

        # ---------------------------------------------------
        # PRUEBA 7: CANCELAR RESERVA
        # ---------------------------------------------------
        reserva2.cancelar()
        print(reserva2.mostrar())

        # ---------------------------------------------------
        # PRUEBA 8: RESERVA CON ASESORÍA
        # ---------------------------------------------------
        reserva3 = Reserva(cliente1, servicio3, 1)
        reserva3.confirmar()
        print(reserva3.mostrar())

        # ---------------------------------------------------
        # PRUEBA 9: RESERVA INVÁLIDA
        # ---------------------------------------------------
        try:
            reserva_error = Reserva(cliente1, servicio1, -1)
        except ReservaError as e:
            print("Error en reserva:", e)

        # ---------------------------------------------------
        # PRUEBA 10: SERVICIO INVÁLIDO
        # ---------------------------------------------------
        try:
            servicio_error = ReservaSala(0)
        except Exception as e:
            print("Error en servicio:", e)

    except Exception as e:
        print("Error general del sistema:", e)


if __name__ == "__main__":
    main()
