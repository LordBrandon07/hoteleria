class tipo_usuario:
    def __init__(self,tipo_usu_id,tipo_usu_nombre,tipo_usu):
        self.__tipo_usu_id=tipo_usu_id
        self.tipo_usu_nombre=tipo_usu_nombre
        self.tipo_usu=tipo_usu
        
    def getusuario (self):
        return self.__tipo_usu_id,self.tipo_usu_nombre,self.tipo_usu
    
    
    def set__tipo_usu_id(self,tipo_usu_id):
        self.__tipo_usu_id=tipo_usu_id
        
    def settipo_usu_nombre(self,tipo_usu_nombre):
        self.tipo_usu_nombre=tipo_usu_nombre
        
    def settipo_usu(self,tipo_usu):
        self.tipo_usu=tipo_usu
    
