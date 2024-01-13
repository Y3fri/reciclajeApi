from models.recogida import Recogida  as RecogidaModel
from schemas.recogida import Recogida

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

    def create_recogida(self, recogida: Recogida):
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
        return
    
    def update_recogida(self, id: int, recogida: Recogida):
        result = self.db.query(RecogidaModel).filter(RecogidaModel.reg_id == id).first()
        result.reg_idcomuna = recogida.reg_idcomuna
        result.reg_plastico = recogida.reg_plastico
        result.reg_papel = recogida.reg_papel
        result.reg_carton = recogida.reg_carton
        result.reg_metal = recogida.reg_metal
        result.reg_vidrio = recogida.reg_vidrio
        result.reg_ubicacion_lag=recogida.reg_ubicacion_lag
        result.reg_ubicacion_log=recogida.reg_ubicacion_log
        result.reg_numero=recogida.reg_numero
        self.db.commit()
        return
    