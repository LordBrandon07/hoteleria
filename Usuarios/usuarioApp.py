from Tipo_usuario import *
from usuarios import *
from datetime import *

with sqlite3.connect("kratosbase.db") as conect:
    cursor=conect.cursor()
    

def Crearusuario():
    usu_id=int(input("ingrese id del usuario: "))
    usu_nombre=input("ingrese nombre del usuario: ")
    usu_apellido=input("ingrese el apellido del usuario: ")
    usu_direccion=(input("ingrese su direccion: "))
    usu_contraseña=(input("ingrese su contraseña: "))
    usu_fe_rest=input("fecha de registro usuario\ndd-mm-yyyy: ")
    usu_fe_registro=input("fecha de registro\ndd-mm-yyyy: ")
    tipo_usu_id=input("ingrese el tipo de usuario: ")

 
    
    ob=Usuario(usu_id,usu_nombre,usu_apellido,usu_direccion,usu_contraseña,usu_fe_rest,usu_fe_registro,tipo_usu_id)
    ob.insertarusuario(ob.getusuario())



def Eliminarusuario():
    usu_id=int(input("ingrese un numero id del usuario: "))
    sentencia = f"DELETE FROM USUARIO WHERE usu_id={usu_id}"
    cursor.execute(sentencia)
    conect.commit()

    print("exitoso")



def Consultarusuario():
    usu_id=int(input("ingrese un numero id del usuario: "))
    #lo que va en la linea 32 no va 
    sentencia = f"SELECT * FROM USUARIO WHERE usu_id={usu_id}"
    print(cursor.execute(sentencia).fetchall())
    
    print("busqueda exitosa")


    
def Modificarusuario():
    usu_id= int(input('ingrese un numero de usuario: ')) 
    campo = input('ingrese el nombre del campo: ')
    dato = input('ingresar dato: ') 
    sentencia = f"UPDATE USUARIO SET {campo} = '{dato}' WHERE usu_id={usu_id} "
    cursor.execute(sentencia)
    conect.commit()
    print('Modificado con exito')


