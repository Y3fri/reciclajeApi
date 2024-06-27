from models.sso_recogida import Sso_recogida as Sso_recogidaModule
from schemas.sso_recogida import Sso_Recogida
from utils.email_recogida_cliente import send_email_recogida_cliente
from models.sso_cliente import Sso_cliente  as Sso_clienteModule

class Sso_recogidaService():

    def __init__(self,db) -> None:
        self.db = db

    
    def get_sso_recogida_id_cliente(self,id:int):      
        result = self.db.query(Sso_recogidaModule).filter(Sso_recogidaModule.sreg_idcliente == id).all()
        sso_recogida_list = [
            {
                "sreg_id":sso_recogida.sreg_id,
                "sreg_idcliente": sso_recogida.sreg_idcliente,
                "sreg_idestado": sso_recogida.sreg_idestado,                
                "sreg_idrecogida": sso_recogida.sreg_idrecogida ,
                "sreg_idtrabajador": sso_recogida.sreg_idtrabajador ,
                "sreg_puntos": sso_recogida.sreg_puntos,
                "sreg_peso": sso_recogida.sreg_peso,
                "sreg_fecha": sso_recogida.sreg_fecha ,
                "sreg_hora1": sso_recogida.sreg_hora1,
                "sreg_hora2": sso_recogida.sreg_hora2,
                "sreg_asignacion": sso_recogida.sreg_asignacion,                
                "nombre_estado": sso_recogida.estado.est_nombre,   
                "nombre_cliente": sso_recogida.sso_cliente.cli_nombres,
                "apellido_cliente": sso_recogida.sso_cliente.cli_apellidos,
                "comuna":  sso_recogida.recogida.comuna.com_nombre,
                "nombre_trabajador": sso_recogida.sso_usuario.usu_nombres,
                "apellido_trabajador": sso_recogida.sso_usuario.usu_apellidos,
                "direccion": sso_recogida.recogida.reg_direccion,
                "barrio_conjunto":  sso_recogida.recogida.reg_barrio_conjunto,
                "plastico": sso_recogida.recogida.reg_plastico,
                "papel": sso_recogida.recogida.reg_papel,
                "carton": sso_recogida.recogida.reg_carton,
                "metal": sso_recogida.recogida.reg_metal,
                "vidrio": sso_recogida.recogida.reg_vidrio,
                "latitud": sso_recogida.recogida.reg_ubicacion_lag,
                "longitud": sso_recogida.recogida.reg_ubicacion_log,
                "numero": sso_recogida.recogida.reg_numero,
            }
            for sso_recogida in result
        ]
        return sso_recogida_list

    def get_sso_recogida_id(self,id:int):      
        result = self.db.query(Sso_recogidaModule).filter(Sso_recogidaModule.sreg_id == id).all()
        sso_recogida_list = [
            {
                "sreg_id":sso_recogida.sreg_id,
                "sreg_idcliente": sso_recogida.sreg_idcliente,
                "sreg_idestado": sso_recogida.sreg_idestado,                
                "sreg_idrecogida": sso_recogida.sreg_idrecogida ,
                "sreg_idtrabajador": sso_recogida.sreg_idtrabajador ,
                "sreg_puntos": sso_recogida.sreg_puntos,
                "sreg_peso": sso_recogida.sreg_peso,
                "sreg_fecha": sso_recogida.sreg_fecha ,
                "sreg_hora1": sso_recogida.sreg_hora1,
                "sreg_hora2": sso_recogida.sreg_hora2,
                "sreg_asignacion": sso_recogida.sreg_asignacion,                
                "nombre_estado": sso_recogida.estado.est_nombre,   
                "nombre_cliente": sso_recogida.sso_cliente.cli_nombres,
                "apellido_cliente": sso_recogida.sso_cliente.cli_apellidos,
                "comuna":  sso_recogida.recogida.comuna.com_nombre,
                "nombre_trabajador": sso_recogida.sso_usuario.usu_nombres,
                "apellido_trabajador": sso_recogida.sso_usuario.usu_apellidos,
                "direccion": sso_recogida.recogida.reg_direccion,
                "barrio_conjunto":  sso_recogida.recogida.reg_barrio_conjunto,
                "plastico": sso_recogida.recogida.reg_plastico,
                "papel": sso_recogida.recogida.reg_papel,
                "carton": sso_recogida.recogida.reg_carton,
                "metal": sso_recogida.recogida.reg_metal,
                "vidrio": sso_recogida.recogida.reg_vidrio,
                "latitud": sso_recogida.recogida.reg_ubicacion_lag,
                "longitud": sso_recogida.recogida.reg_ubicacion_log,
                "numero": sso_recogida.recogida.reg_numero,
            }
            for sso_recogida in result
        ]
        return sso_recogida_list

    def get_sso_recogida(self):      
        result = self.db.query(Sso_recogidaModule).all()
        sso_recogida_list = [
            {
                "sreg_id":sso_recogida.sreg_id,
                "sreg_idcliente": sso_recogida.sreg_idcliente,
                "sreg_idestado": sso_recogida.sreg_idestado,                
                "sreg_idrecogida": sso_recogida.sreg_idrecogida ,
                "sreg_idtrabajador": sso_recogida.sreg_idtrabajador ,
                "sreg_puntos": sso_recogida.sreg_puntos,
                "sreg_peso": sso_recogida.sreg_peso,
                "sreg_fecha": sso_recogida.sreg_fecha ,
                "sreg_hora1": sso_recogida.sreg_hora1,
                "sreg_hora2": sso_recogida.sreg_hora2,
                "sreg_asignacion": sso_recogida.sreg_asignacion,                
                "nombre_estado": sso_recogida.estado.est_nombre,   
                "nombre_cliente": sso_recogida.sso_cliente.cli_nombres,
                "apellido_cliente": sso_recogida.sso_cliente.cli_apellidos,
                "comuna": sso_recogida.recogida.comuna.com_nombre,
                "nombre_trabajador": sso_recogida.sso_usuario.usu_nombres,
                "apellido_trabajador": sso_recogida.sso_usuario.usu_apellidos,
                "direccion": sso_recogida.recogida.reg_direccion,
                "barrio_conjunto":  sso_recogida.recogida.reg_barrio_conjunto,
                "plastico": sso_recogida.recogida.reg_plastico,
                "papel": sso_recogida.recogida.reg_papel,
                "carton": sso_recogida.recogida.reg_carton,
                "metal": sso_recogida.recogida.reg_metal,
                "vidrio": sso_recogida.recogida.reg_vidrio,
                "latitud": sso_recogida.recogida.reg_ubicacion_lag,
                "longitud": sso_recogida.recogida.reg_ubicacion_log,
                "numero": sso_recogida.recogida.reg_numero,
            }
            for sso_recogida in result
        ]
        return sso_recogida_list
    
    def get_sso_recogida_asignacion(self):      
        result = self.db.query(Sso_recogidaModule).filter(Sso_recogidaModule.sreg_asignacion == False).all()
        sso_recogida_list = [
            {
                "sreg_id":sso_recogida.sreg_id,
                "sreg_idcliente": sso_recogida.sreg_idcliente,
                "sreg_idestado": sso_recogida.sreg_idestado,                
                "sreg_idrecogida": sso_recogida.sreg_idrecogida ,
                "sreg_idtrabajador": sso_recogida.sreg_idtrabajador ,
                "sreg_puntos": sso_recogida.sreg_puntos,
                "sreg_peso": sso_recogida.sreg_peso,
                "sreg_fecha": sso_recogida.sreg_fecha ,
                "sreg_hora1": sso_recogida.sreg_hora1,
                "sreg_hora2": sso_recogida.sreg_hora2,
                "sreg_asignacion": sso_recogida.sreg_asignacion,                
                "nombre_estado": sso_recogida.estado.est_nombre,   
                "nombre_cliente": sso_recogida.sso_cliente.cli_nombres,
                "apellido_cliente": sso_recogida.sso_cliente.cli_apellidos,
                "comuna": sso_recogida.recogida.comuna.com_nombre,
                "nombre_trabajador": sso_recogida.sso_usuario.usu_nombres,
                "apellido_trabajador": sso_recogida.sso_usuario.usu_apellidos,
                "direccion": sso_recogida.recogida.reg_direccion,
                "barrio_conjunto":  sso_recogida.recogida.reg_barrio_conjunto,
                "plastico": sso_recogida.recogida.reg_plastico,
                "papel": sso_recogida.recogida.reg_papel,
                "carton": sso_recogida.recogida.reg_carton,
                "metal": sso_recogida.recogida.reg_metal,
                "vidrio": sso_recogida.recogida.reg_vidrio,
                "latitud": sso_recogida.recogida.reg_ubicacion_lag,
                "longitud": sso_recogida.recogida.reg_ubicacion_log,
                "numero": sso_recogida.recogida.reg_numero,
            }
            for sso_recogida in result
        ]
        return sso_recogida_list


    def update_sso_recogida(self, id: int, sso_recogida: Sso_Recogida):
        result = self.db.query(Sso_recogidaModule).filter(Sso_recogidaModule.sreg_id == id).first()
        try:
            result.sreg_idcliente = sso_recogida.sreg_idcliente
            result.sreg_idestado = sso_recogida.sreg_idestado
            result.sreg_idrecogida = sso_recogida.sreg_idrecogida
            result.sreg_idtrabajador = sso_recogida.sreg_idtrabajador
            result.sreg_puntos = sso_recogida.sreg_puntos
            result.sreg_peso = sso_recogida.sreg_peso
            result.sreg_fecha = sso_recogida.sreg_fecha
            result.sreg_hora1 = sso_recogida.sreg_hora1
            result.sreg_hora2 = sso_recogida.sreg_hora2
            result.sreg_asignacion = sso_recogida.sreg_asignacion
            self.db.commit()
            result_cli = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_id == result.sreg_idcliente).first()
            if not result_cli:
                raise ValueError("No se encontró el cliente con el ID proporcionado")
            send_email_recogida_cliente(email=result_cli.cli_correo, fecha= result.sreg_fecha,hora1= result.sreg_hora1,hora2=result.sreg_hora2)            
        except Exception as e:         
            print(f"Error en la inserción: {str(e)}")
            self.db.rollback()
            raise
    
    def update_sso_recogida_trabajo(self, id: int, idtrabajador:int, sso_recogida: Sso_Recogida):
        result = self.db.query(Sso_recogidaModule).filter(Sso_recogidaModule.sreg_id == id,Sso_recogidaModule.sreg_idtrabajador == idtrabajador ).first()
        try:
            result.sreg_idcliente = sso_recogida.sreg_idcliente
            result.sreg_idestado = sso_recogida.sreg_idestado
            result.sreg_idrecogida = sso_recogida.sreg_idrecogida
            result.sreg_idtrabajador = sso_recogida.sreg_idtrabajador
            result.sreg_puntos = sso_recogida.sreg_puntos
            result.sreg_peso = sso_recogida.sreg_peso
            result.sreg_fecha = sso_recogida.sreg_fecha
            result.sreg_hora1 = sso_recogida.sreg_hora1
            result.sreg_hora2 = sso_recogida.sreg_hora2
            result.sreg_asignacion = sso_recogida.sreg_asignacion
            self.db.commit()
        except Exception as e:         
            print(f"Error en la inserción: {str(e)}")
            self.db.rollback()
            raise