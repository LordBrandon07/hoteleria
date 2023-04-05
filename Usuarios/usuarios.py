import sqlite3

with sqlite3.connect("C:\Villamil\kratosbase.db") as conect:
    cursor=conect.cursor()




class Usuario:
    def __init__(self,usu_id,usu_nombre,usu_apellido,usu_direccion,usu_contraseña,usu_fe_rest,usu_fe_registro,tipo_usu_id):
        self.__usu_id=usu_id
        self.usu_nombre=usu_nombre
        self.usu_apellido=usu_apellido
        self.usu_direccion=usu_direccion
        self.usu_contraseña=usu_contraseña
        self.usu_fe_rest=usu_fe_rest
        self.usu_fe_registro=usu_fe_registro
        self.tipo_usu_id=tipo_usu_id
        self.hot_id=1
    
        
    def getusuario (self):
        return self.__usu_id,self.usu_nombre,self.usu_apellido,self.usu_direccion,self.usu_contraseña,self.usu_fe_rest,self.usu_fe_registro,self.tipo_usu_id,self.hot_id
    
    
    
    def set__usu_id(self,usu_id):
        self.__usu_id=usu_id
    
    def setusu_nombre(self,usu_nombre):
        self.usu_nombre=usu_nombre
    
    def setusu_apellidos(self,usu_apellidos):
        self.usu_apellidos=usu_apellidos
        
    def setusu_direccion(self,usu_direccion):
        self.usu_direccion=usu_direccion
        
    def setusu_contraseña(self,usu_contraseña):
        self.usu_contraseña=usu_contraseña
        
    def setusu_fe_rest(self,usu_fe_rest):
        self.usu_fe_rest=usu_fe_rest
        
    def setusu_telefono(self,usu_telefono):
        self.usu_telefono=usu_telefono
    
    def setusu_email(self,usu_email):
        self.usu_email=usu_email
        
    def insertarusuario(self,usu):
        cursor=conect.cursor()
        sentencia=f"insert into Usuario values({usu[0]},'{usu[1]}','{usu[2]}','{usu[3]}','{usu[4]}','{usu[5]}','{usu[6]}','{usu[7]}',{usu[8]})"

        cursor.execute(sentencia)
        conect.commit()
        print("el usuario se creo correctamente")