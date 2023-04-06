import sqlite3

with sqlite3.connect('D:\\DonBrandon\\Tarea\\Adso\\visual\\hoteleria\\kratosbase.db')as pepe:
    micursor=pepe.cursor()

class Habitaciones:
    def __init__(self, hab_numero, hab_disponible, tipo_hab_id, hab_capacidad, hab_tarifa):
        self.hab_numero = hab_numero
        self.hab_disponible = hab_disponible
        self.tipo_hab_id = tipo_hab_id
        self.hab_capacidad = hab_capacidad
        self.hab_tarifa = hab_tarifa

    def getHabitaciones(self):
        return self.hab_numero, self.hab_disponible, self.tipo_hab_id, self.hab_capacidad, self.hab_tarifa
    
    def setHab_numero(self, hab_numero):
        self.hab_numero = hab_numero

    def setHab_disponible(self, hab_disponible):
        self.hab_disponible = hab_disponible

    def setTipo_hab_id(self, tipo_hab_id):
        self.tipo_hab_id = tipo_hab_id

    def setHab_capacidad(self, hab_capacidad):
        self.hab_capacidad = hab_capacidad

    def sethab_tarifa(self, hab_tarifa):
        self.hab_tarifa = hab_tarifa

    def crearHabitacion(self, hab):
        micursor=pepe.cursor()
        sentencia = f"INSERT INTO HABITACION VALUES ({hab[0]}, '{hab[1]}', '{hab[2]}', {hab[3]}, {hab[4]})"
        micursor.execute(sentencia)
        pepe.commit()
        print('Accion satisfactoria')
