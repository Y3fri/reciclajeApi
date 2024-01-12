from models.recogida import Recogida  as RecogidaModel

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
