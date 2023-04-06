import sqlite3

with sqlite3.connect("/home/sergio/kratos/kratosbase.db")as sal:
    cursor = sal.cursor()

class Adicional:
    def __init__(self,id,valor,tipo):
        self.__id = id
        self.serv_valor = valor
        self.serv_tipo = tipo

    def getservicio_adicional(self):
        return self.__id, self.serv_valor, self.serv_tipo

    def setid(self,id):
        self.__id = id
    
    def setValor(self,valor):
        self.serv_valor = serv_valor

    def setTipo(self,tipo):
        self.serv_tipo = serv_tipo

    def crear(self, serv):
        cursor = sal.cursor()
        sentencia =f"INSERT INTO servicio_adicional VALUES ('{serv[0]}',{serv[1]},'{serv[2]}')"
        cursor.execute(sentencia)
        sal.commit()
        print("Ejecucion con satisfaccion")
    
 