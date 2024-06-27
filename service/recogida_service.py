from fastapi import HTTPException
from sqlalchemy import func
from models.recogida import Recogida  as RecogidaModel
from models.sso_recogida import Sso_recogida as Sso_recogidaModule
from schemas.recogida import Recogida
from schemas.sso_recogida import Sso_Recogida
from models.sso_usuario import Sso_usuario  as Sso_usuarioModule
from utils.email_recogida import send_email_recogida

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
                "reg_direccion": recogida.reg_direccion,
                "reg_barrio_conjunto": recogida.reg_barrio_conjunto,
                "nombre_comuna": recogida.comuna.com_nombre,                
            }
            for recogida in result
        ]
        return recogida_list

#arreglarrrrrrrrrrrrrrrrrrrrrr erro en front
    def create_recogida(self, recogida: Recogida, sso_recogida: Sso_Recogida):
        try:
            result = (self.db.query(Sso_usuarioModule)
                    .filter(Sso_usuarioModule.usu_rol == 2)
                    .order_by(func.random())
                    .first())

            if result is None:
                raise HTTPException(status_code=400, detail="No se encontró un usuario trabajador disponible.")

            existing_recogida = self.db.query(Sso_recogidaModule).filter(
                Sso_recogidaModule.sreg_idcliente == sso_recogida.sreg_idcliente,
                Sso_recogidaModule.sreg_idestado == 2
            ).first()

            if existing_recogida:
                raise HTTPException(status_code=400, detail="Ya existe una recogida, debes esperar a que vayan por tus materiales.")

            new_recogida = RecogidaModel(
                reg_idcomuna=recogida.reg_idcomuna,
                reg_plastico=recogida.reg_plastico,
                reg_papel=recogida.reg_papel,
                reg_carton=recogida.reg_carton,
                reg_metal=recogida.reg_metal,
                reg_vidrio=recogida.reg_vidrio,
                reg_ubicacion_lag=recogida.reg_ubicacion_lag,
                reg_ubicacion_log=recogida.reg_ubicacion_log,
                reg_numero=recogida.reg_numero,
                reg_direccion=recogida.reg_direccion,
                reg_barrio_conjunto=recogida.reg_barrio_conjunto
            )
            self.db.add(new_recogida)
            self.db.commit()

            new_sso_recogida = Sso_recogidaModule(
                sreg_idcliente=sso_recogida.sreg_idcliente,
                sreg_idestado=2,
                sreg_idrecogida=new_recogida.reg_id,
                sreg_idtrabajador=result.usu_id,
                sreg_puntos=sso_recogida.sreg_puntos,
                sreg_peso=sso_recogida.sreg_peso,
                sreg_fecha=sso_recogida.sreg_fecha,
                sreg_hora1=sso_recogida.sreg_hora1,
                sreg_hora2=sso_recogida.sreg_hora2,
                sreg_asignacion=False
            )
            self.db.add(new_sso_recogida)
            self.db.commit()

            result_users = self.db.query(Sso_usuarioModule).filter(Sso_usuarioModule.usu_rol == 1).all()
            for user in result_users:
                send_email_recogida(email=user.usu_correo, idRecogida=new_recogida.reg_id)

        except ValueError as ve:
            print(f"Error de validación: {str(ve)}")
            self.db.rollback()
            raise HTTPException(status_code=400, detail=str(ve))

        except Exception as e:            
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))


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
        result.reg_direccion = recogida.reg_direccion
        result.reg_barrio_conjunto = recogida.reg_barrio_conjunto
        self.db.commit()
        return
    