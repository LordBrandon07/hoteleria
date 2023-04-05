from reservas import *
from datetime import *
#from habitaciones import *

def capReserva():
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
    

capReserva()
