from Tipo_usuario import *
from usuarios import *
from datetime import *

def crearusuario():
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

crearusuario()

