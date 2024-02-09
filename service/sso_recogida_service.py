from models.sso_recogida import Sso_recogida as Sso_recogidaModule
from schemas.sso_recogida import Sso_Recogida

class Sso_recogidaService():

    def __init__(self,db) -> None:
        self.db = db

    def get_sso_recogida(self):      
        result = self.db.query(Sso_recogidaModule).all()
        sso_recogida_list = [
            {
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
                "nombre_trabajador": sso_recogida.sso_usuario.usu_nombres,
                "apellido_trabajador": sso_recogida.sso_usuario.usu_apellidos,
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
        result.reg_idcomuna = sso_recogida.reg_idcomuna
        result.reg_plastico = sso_recogida.reg_plastico
        result.reg_papel = sso_recogida.reg_papel
        result.reg_carton = sso_recogida.reg_carton
        result.reg_metal = sso_recogida.reg_metal
        result.reg_vidrio = sso_recogida.reg_vidrio
        result.reg_ubicacion_lag = sso_recogida.reg_ubicacion_lag
        result.reg_ubicacion_log = sso_recogida.reg_ubicacion_log
        result.reg_numero = sso_recogida.reg_numero
        self.db.commit()
        return