from reservas import *
from datetime import *
import sqlite3
#from habitaciones import *

with sqlite3.connect('kratosbase.db')as con:
    cursor=con.cursor()

def capturar_reserva():
    fecha=date.today()
    while True:
        usu_id=input("Digite numero de identificacion del cliente\n")
        if usu_id.isdigit() and int(usu_id)>0:
            break
        else:
            print("===ID del cliente es incorrecto===")
    while True:
        cant_hab=int(input("Cuantas habitaciones desea reservar:\n"))
        if str(cant_hab).isdigit() and cant_hab<10:
            break
        else:
            print("===Esta cantidad supera nuestra capacidad de 10 habitaciones por cliente===")
    while True:
        cant_adultos=int(input("Cantidad de adultos:\n"))
        if str(cant_adultos).isdigit() and cant_adultos<=cant_hab*2:
            break
        else:
            print("===Verifique que la cantidad de adultos no supere nuestra capacidad===")
    while True:
        cant_ninos=int(input("Cantidad de niños:\n"))
        if str(cant_ninos).isdigit() and cant_ninos<=cant_hab*3-cant_adultos:
            break
        else:
            print("===Verifique que la cantidad de niños no supere nuestra capacidad===")
    while True:
        try:
            fe_inicio=input("Fecha inicio:\ndd-mm-yyyy\n")
            ini=datetime.strptime(fe_inicio,'%d-%m-%Y')
            break
        except:
            print("===Formato de fecha incorrecto: debe ser dd-mm-yyyy===")
    while True:
        try:
            fe_fin=input("Fecha final:\ndd-mm-yyyy\n")
            fin=datetime.strptime(fe_fin,'%d-%m-%Y')
            if fe_fin>fe_inicio:
                break
            else:
                print("===Fecha fin menor a fecha inicio===")
        except:
            print("===Formato de fecha incorrecto: debe ser dd-mm-yyyy===")
    cant_dias=(fin-ini).days
    valor=cant_dias*10000
    while True:
        id="R"
        try:
            num=input("Digite codigo de reserva:\n")
            if len(num)!=4 or not num.isdigit():
                assert()
            id+=num
            nw=Reservas(id, fecha, cant_hab, cant_adultos, cant_ninos, fe_inicio, fe_fin, cant_dias, valor, usu_id)
            nw.guardarReserva(nw.getReserva())
            break
        except sqlite3.IntegrityError:
            print("===Codigo de reserva ya existe===")
        except:
            print("===Formato de codigo incorrecto: Debe ser de 4 digitos===")

def buscar_reservas():
    print('''\n====Busqueda====
    1- ID reserva
    2- ID usuario
    3- Fecha de inicio
    4- Estado de reserva
    ''')
    opcion=int(input('Seleccione una opcion de busqueda: '))
    if opcion==1:
        campo="res_id"
    elif opcion==2:
        campo="usu_id"
    elif opcion==3:
        campo="res_fe_inicio"
    elif opcion==4:
        campo="est_id"
    else:
        print("===Opcion no valida===")
        buscar_reservas()
    dato=input('Digite el valor buscado: ').upper()
    sql=f"SELECT * FROM reserva WHERE {campo}='{dato}'"
    consulta=cursor.execute(sql).fetchall()
    if len(consulta)==0:
        print("\n===No existe la reserva===")
        buscar_reservas()
    else:
        print("===========================================================================================================================================")
        print("res_id |res_fecha   |res_cant_hab |res_cant_adultos |res_cant_niños |res_fe_inicio |res_fe_final |res_cant_dias |res_valor |usu_id |est_id")
        for i in consulta:
            print(f"{i[0]}  |{i[1]}  |{i[2]}            |{i[3]}                |{i[4]}              |{i[5]}    |{i[6]}   |{i[7]}             |{i[8]}    |{i[9]}     |{i[10]}")
        print("===========================================================================================================================================")
        
def modificar_reserva():
    consultar_reservas()
    while True:
        id=input('***Digite ID de la Reserva a Modificar: ').upper()
        if len(id)==5 and id.startswith("R"):
            break
        else:
            print("===ID incorrecta, favor verificar===")
    campo=input('Digite el campo que desea modificar: ')
    dato=input('Digite el nuevo valor del campo: ')
    sentencia = f"UPDATE reserva SET {campo} = '{dato}' WHERE res_id='{id}'"
    cursor.execute(sentencia)
    con.commit()
    print('===Cambio realizado correctamente===')
    
def borrar_reserva():
    consultar_reservas()
    while True:
        id=input('***Digite ID de la Reserva a Eliminar: ').upper()
        if len(id)==5 and id.startswith("R"):
            break
        else:
            print("===ID incorrecta, favor verificar===")
    sql=f"DELETE FROM reserva WHERE res_id == '{id}'"
    cursor.execute(sql)
    con.commit()
    print("===Reserva Eliminada Correctamente===")
    
def consultar_reservas():
    cont=1
    sep="============================================================================================================================================="
    cab="# |res_id |res_fecha   |res_cant_hab |res_cant_adultos |res_cant_niños |res_fe_inicio |res_fe_final |res_cant_dias |res_valor |usu_id |est_id"
    sql=f"SELECT * FROM reserva"
    consulta=cursor.execute(sql).fetchall()
    print(sep)
    print(cab)
    with open("Reservas\informe.txt","w") as flujo:
        flujo.write(f"{sep}\n")
        flujo.write(f"{cab}\n")
        for i in consulta:
            info=f"{cont} |{i[0]}  |{i[1]}  |{i[2]}            |{i[3]}                |{i[4]}              |{i[5]}    |{i[6]}   |{i[7]}             |{i[8]}    |{i[9]}     |{i[10]}"
            flujo.write(f"{info}\n")
            print(info)
            cont+=1
        flujo.write(f"{sep}\n")
    print(sep)
