import sqlite3
from estadoReserva import *

with sqlite3.connect('kratosbase.db')as con:
    cursor=con.cursor()

class Reservas:
    def __init__(self,id,fecha,cant_hab,cant_adultos,cant_ninos,fe_inicio,fe_fin,cant_dias,valor,usu_id):
        self.__id = id
        self.fecha = fecha
        self.cant_hab = cant_hab
        self.cant_adultos = cant_adultos
        self.cant_ninos = cant_ninos
        self.fe_inicio = fe_inicio
        self.fe_fin = fe_fin
        self.cant_dias = cant_dias
        self.valor = valor
        self.__usu_id = usu_id
        self.est_id = "A025"

    def getReserva(self):
        return self.__id, self.fecha,self.cant_hab,self.cant_adultos,self.cant_ninos,self.fe_inicio,self.fe_fin,self.cant_dias,self.valor,self.__usu_id,self.est_id

    def setReserva(self, id):
        self.__id = id

    def guardarReserva(self,res):
        sql=f"INSERT INTO reserva VALUES ('{res[0]}','{res[1]}',{res[2]},{res[3]},{res[4]},'{res[5]}','{res[6]}',{res[7]},{res[8]},{res[9]},'{res[10]}');"
        cursor.execute(sql)
        con.commit()
        print('===Reserva Creada Correctamente===')
        
    
