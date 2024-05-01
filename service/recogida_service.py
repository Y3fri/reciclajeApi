from sqlalchemy import func
from models.recogida import Recogida  as RecogidaModel
from models.sso_recogida import Sso_recogida as Sso_recogidaModule
from schemas.recogida import Recogida
from schemas.sso_recogida import Sso_Recogida
from models.sso_usuario import Sso_usuario  as Sso_usuarioModule

class RecogidaService():

    def __init__(self,db) -> None:
        self.db = db

    def get_recogida(self):      
        result = self.db.query(RecogidaModel).all()
        recogida_list = [
            {
                "reg_idcomuna": recogida.reg_idcomuna,
                "reg_plastico": recogida.reg_plastico,
                "reg_carton": recogida.reg_carton,
                "reg_vidrio": recogida.reg_vidrio,
                "reg_ubicacion_log": recogida.reg_ubicacion_log,
                "reg_papel": recogida.reg_papel,
                "reg_id": recogida.reg_id,
                "reg_metal": recogida.reg_metal,
                "reg_ubicacion_lag": recogida.reg_ubicacion_lag,
                "reg_numero": recogida.reg_numero,
                "nombre_comuna": recogida.comuna.com_nombre,                
            }
            for recogida in result
        ]
        return recogida_list


    def create_recogida(self, recogida: Recogida, sso_recogida: Sso_Recogida):
        result = (self.db.query(Sso_usuarioModule)
        .filter(Sso_usuarioModule.usu_rol == 2)
        .order_by(func.random())
        .first()
        )    
        try:            
            new_recogida = RecogidaModel(
                reg_idcomuna=recogida.reg_idcomuna,
                reg_plastico=recogida.reg_plastico,
                reg_papel=recogida.reg_papel,
                reg_carton=recogida.reg_carton,
                reg_metal=recogida.reg_metal,
                reg_vidrio=recogida.reg_vidrio,
                reg_ubicacion_lag=recogida.reg_ubicacion_lag,
                reg_ubicacion_log=recogida.reg_ubicacion_log,
                reg_numero=recogida.reg_numero
            )
            self.db.add(new_recogida)
            self.db.commit()

            new_sso_recogida = Sso_recogidaModule(
                sreg_idcliente=sso_recogida.sreg_idcliente,
                sreg_idestado= 1,
                sreg_idrecogida=new_recogida.reg_id,
                sreg_idtrabajador= result.usu_id,
                sreg_puntos=sso_recogida.sreg_puntos,
                sreg_peso=sso_recogida.sreg_peso,
                sreg_fecha=sso_recogida.sreg_fecha,
                sreg_hora1=sso_recogida.sreg_hora1,
                sreg_hora2=sso_recogida.sreg_hora2,
                sreg_asignacion=False
            )
            self.db.add(new_sso_recogida)
            self.db.commit()
        except Exception as e:         
            print(f"Error en la inserción: {str(e)}")
            self.db.rollback()
            raise
    
    def update_recogida(self, id: int, recogida: Recogida):
        result = self.db.query(RecogidaModel).filter(RecogidaModel.reg_id == id).first()
        result.reg_idcomuna = recogida.reg_idcomuna
        result.reg_plastico = recogida.reg_plastico
        result.reg_papel = recogida.reg_papel
        result.reg_carton = recogida.reg_carton
        result.reg_metal = recogida.reg_metal
        result.reg_vidrio = recogida.reg_vidrio
        result.reg_ubicacion_lag = recogida.reg_ubicacion_lag
        result.reg_ubicacion_log = recogida.reg_ubicacion_log
        result.reg_numero = recogida.reg_numero
        self.db.commit()
        return
    