from sys import path
path.append('Habitaciones')
path.append('Reservas')
path.append('ServicioAD')
path.append('Usuarios')

import habitaciones_menu
import menuReserva
import servicioMenu
import MenuUsuario

while True:
    print('''
        BIENVENIDO
    
    MENU HOTELERIA

    1- Modulo Habitaciones
    2- Modulo Reservas
    3- Modulo Servicios Adicionales
    4- Modulo Usuarios
    5- Salir
    ''')

    sele = int(input('seleccione una opcion: '))
    if sele == 1:
        habitaciones_menu.mhabitaciones()
    if sele == 2:
        menuReserva.menuReservas()
    if sele == 3:
        servicioMenu.menuadicional()
    if sele == 4:
        MenuUsuario.MenuUsuarios()
    if sele == 0:
        exit()

