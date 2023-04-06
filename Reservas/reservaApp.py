from reservas import *
from datetime import *
import sqlite3
#from habitaciones import *

with sqlite3.connect('C://Users//gveje//Desktop//DIEGO//ADSO//SQLite//kratosbase.db')as con:
    cursor=con.cursor()

def captura_reserva():
    id=input("Digite codigo de reserva:\n")
    fecha=date.today()
    cant_hab=int(input("Cuantas habitaciones desea reservar:\n"))
    cant_adultos=int(input("Cantidad de adultos:\n"))
    cant_ninos=int(input("Cantidad de niños:\n"))
    fe_inicio=input("Fecha inicio:\ndd-mm-yyyy\n")
    ini=datetime.strptime(fe_inicio,'%d-%m-%Y')
    fe_fin=input("Fecha final:\ndd-mm-yyyy\n")
    fin=datetime.strptime(fe_fin,'%d-%m-%Y')
    cant_dias=(fin-ini).days
    valor=cant_dias*10000
    usu_id=int(input("Digite numero de identificacion\n"))

    nw=Reservas(id, fecha, cant_hab, cant_adultos, cant_ninos, fe_inicio, fe_fin, cant_dias, valor, usu_id)
    nw.guardarReserva(nw.getReserva())
    
def borrar_reserva():
    id=input("Digite ID de la reserva a eliminar")
    sql=f"DELETE FROM reserva WHERE res_id == '{id}'"
    cursor.execute(sql)
    con.commit()
    print("Reserva Eliminada Correctamente")
    
def consultar_reserva():
    cont=1
    sql=f"SELECT * FROM reserva"
    consulta=cursor.execute(sql).fetchall()
    for i in consulta:
        print(f"{cont} - {i[0]}  {i[1]}  {i[2]}  {i[3]}  {i[4]}  {i[5]}  {i[6]}  {i[7]}  {i[8]}  {i[9]}  {i[10]}")
        cont+=1
        
