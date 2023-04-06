from usuarioApp import *


def MenuUsuarios():
   while True:

    print('''
         __________________________________________________
        |1- cree un usuario________________________________|
        |2- eliminar usuario_______________________________|                               
        |3- consultar usuario______________________________|                              
        |4- modificar usuario______________________________|
        |0- regresar_______________________________________|                                       
        |__________________________________________________|
    
''')


    sele = int(input('seleccionar: '))
    if sele == 1:
        Crearusuario()
    if sele == 2:
        Eliminarusuario()
    if sele == 3:
        Consultarusuario()
    if sele == 4:
        Modificarusuario()
    if sele == 0:
        exit()
    
MenuUsuarios()