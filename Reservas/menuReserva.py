from reservaApp import *

def menuReservas():
    while True:
        print('''\n====MODULO RESERVAS====
    1- Crear Reserva
    2- Modificar Reserva
    3- Eliminar Reserva
    4- Buscar Reserva
    5- Crear Informe de Reservas en txt
    0- Regresar
    ''')
        opcion=int(input('Seleccione una opcion: '))
        if opcion == 1:
            capturar_reserva()
        if opcion == 2:
            modificar_reserva()
        if opcion == 3:
            borrar_reserva()
        if opcion == 4:
            buscar_reserva()
        if opcion == 5:
            consultar_reservas()
        if opcion == 0:
            exit()

menuReservas()