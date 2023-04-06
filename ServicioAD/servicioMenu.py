from servicio_app import*

while True:

    print('''
    1- Crear un servicio adicional
    2- Eliminar un servicio adicional
    3- Modificar un servicio adicional
    4- seleccionar un servicio adicional
    0- Inicio
''')

    seleccion =int(input("seleccionar: "))
    if seleccion == 1:

        crearadicional()

    if seleccion == 2:

        eliminaradicional()
        
    if seleccion == 3:

        modadicional()

    if seleccion == 4:

        selcadicional()

    if seleccion == 0:
        exit()
    
print(seleccion)
    