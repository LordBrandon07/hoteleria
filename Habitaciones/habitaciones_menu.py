from habitaciones_app import *

def mhabitaciones():
    while True:

        print('''
        1- crear una habitacion
        2- modificar una habitacion
        3- eliminar una habitacion
        4- seleccionar una habitacion
        0- regresar
    ''')


        sele = int(input('seleccionar: '))
        if sele == 1:
            capturarHabitaciones()
        if sele == 2:
            modificarHabitacion()
        if sele == 3:
            eliminarHabitaciones()
        if sele == 4:
            selectHabitacion()
        if sele == 0:
            break