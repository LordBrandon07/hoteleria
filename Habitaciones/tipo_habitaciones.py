class Tipo_habitaciones:
    def __init__(self, tipo_hab_id, tipo_hab, tipo_hab_cant):
        self.__tipo_hab_id = tipo_hab_id
        self.tipo_hab = tipo_hab
        self.tipo_hab_cant = tipo_hab_cant

    def getTipo_habitaciones(self):
        return self.__tipo_hab_id, self.tipo_hab, self.tipo_hab_cant
    
    def setTipo_hab_id(self, tipo_hab_id):
        self.__tipo_hab_id = tipo_hab_id

    def setTipo_hab(self, tipo_hab):
        self.Tipo_hab = tipo_hab

    def setTipo_hab_cant(self, tipo_hab_cant):
        self.tipo_hab_cant = tipo_hab_cant
        