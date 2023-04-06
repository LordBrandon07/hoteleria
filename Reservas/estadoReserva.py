import sqlite3

with sqlite3.connect('C://Users//gveje//Desktop//DIEGO//ADSO//SQLite//kratosbase.db')as con:
    cursor=con.cursor()

class EstadoReserva:
    def __init__(self, id, estado):
        self.__id = id
        self.estado = estado

    def getEstado (self):
        return self.__id, self.estado

    def setEstado (self,id):
        self.__id = id
        
    def listaEstados(self,num):
        lista=[]
        sql="SELECT est_id FROM estado_reserva"
        est=cursor.execute(sql).fetchall()
        for i in est:
            od=i[0]
            lista.append(od)
        return lista.index(num)
