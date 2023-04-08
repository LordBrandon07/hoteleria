from servicio import*

def crearadicional():
    id=input("Ingrese el id del servicio: ")
    valor=int(input("Ingrese el valor del servicio: "))
    tipo=input("Ingrese el tipo de servicio: ")

    nuevo=Adicional(id,valor,tipo)
    nuevo.crear(nuevo.getservicio_adicional())

def eliminaradicional():
    id=input('Ingrese el id que quiere eliminar: ')
    sentencia = f"DELETE FROM SERVICIO_ADICIONAL WHERE serv_id='{id}'"
    cursor.execute(sentencia)
    sal.commit()
    print("Ejecucion con satisfaccion")

def selcadicional():
    id=input('Ingrese el id del que desea saber: ')
    sentencia= f"SELECT * FROM SERVICIO_ADICIONAL WHERE serv_id='{id}'"
    mostrar= cursor.execute(sentencia).fetchall()
    for i in mostrar:
        print(f"{i[0]},{i[1]},{i[2]}")
    print("Ejecucion con satisfaccion")

def modadicional():
    serv_id = input('ingrese el id del servicio: ')  
    campo = input('ingrese el campo que quiqere modificar: ')
    valor = input('ingrese el dato: ')
    sentencia = f"UPDATE SERVICIO_ADICIONAL SET '{campo}' = {valor} WHERE serv_id='{serv_id}' "
    cursor.execute(sentencia)
    sal.commit()
    print('Ejecucion con satisfaccion')

