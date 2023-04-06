from habitaciones import *

with sqlite3.connect('D:\\DonBrandon\\Tarea\\Adso\\visual\\hoteleria\\kratosbase.db')as pepe:
    micursor=pepe.cursor()

def capturarHabitaciones():
    hab_numero = int(input('ingrese un numero de habitacion: '))
    hab_disponible = str(input('ingrese si la habitacion esta disponible: '))
    tipo_hab_id = str(input('ingrese un id: '))
    hab_capacidad = int(input('ingrese la capacidad de la habitacion: '))
    hab_tarifa = int(input('ingrese la la tarifa: '))

    new1 = Habitaciones(hab_numero, hab_disponible, tipo_hab_id, hab_capacidad, hab_tarifa)
    new1.crearHabitacion(new1.getHabitaciones())

def eliminarHabitaciones():
    hab_numero = int(input('ingrese un numero de habitacion: '))
    micursor=pepe.cursor()
    sentencia = f"DELETE FROM HABITACION WHERE hab_numero={hab_numero}"
    micursor.execute(sentencia)
    pepe.commit()
    print('caremonda1')

def selectHabitacion():
    pass

def modificarHabitacion():
    pass
    
eliminarHabitaciones()

