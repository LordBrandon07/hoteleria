from habitaciones import *

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
    sentencia = f"DELETE FROM HABITACION WHERE hab_numero={hab_numero}"
    micursor.execute(sentencia)
    pepe.commit()
    print('caremonda1')

def selectHabitacion():
    hab_numero = int(input('ingrese un numero de habitacion: '))
    sentencia = f"SELECT * FROM HABITACION WHERE hab_numero={hab_numero}"
    m = micursor.execute(sentencia).fetchall()
    for i in m:
        print(f'{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]},')
    print('caremonda2')

def modificarHabitacion():
    campo = input('ingresar campo: ')
    dato = input('ingresar dato: ')
    hab_numero = int(input('ingrese un numero de habitacion: '))    
    sentencia = f"UPDATE HABITACION SET {campo} = '{dato}' WHERE hab_numero={hab_numero} "
    micursor.execute(sentencia)
    pepe.commit()
    print('caremonda3')
    




