from fastapi import HTTPException
from sqlalchemy import func
from models.sso_usuario import Sso_usuario  as Sso_usuarioModule
from sqlalchemy.orm import Session
from utils.hash import hash_sha256_then_md5_then_sha1_and_sha512
from schemas.sso_usuario import Sso_usuario
from utils.email_usuario import send_registration_email
from models.user_session import UserSession as UserSessionModule
from datetime import datetime, timedelta
import pytz

local_timezone = pytz.timezone('America/Bogota')

class Sso_usuarioService():

    def __init__(self, db: Session) -> None:
        self.db = db
        
    def get_sso_usuario(self):      
        result = self.db.query(Sso_usuarioModule).all()
        sso_usuario_list = [
            {
                "usu_id": sso_usuario.usu_id,
                "usu_estado": sso_usuario.usu_estado,
                "usu_rol": sso_usuario.usu_rol,                
                "usu_correo": sso_usuario.usu_correo ,
                "usu_documento": sso_usuario.usu_documento ,
                "usu_nombres": sso_usuario.usu_nombres ,
                "usu_apellidos": sso_usuario.usu_apellidos ,
                "usu_nickname": sso_usuario.usu_nickname ,
                "usu_clave": sso_usuario.usu_clave ,
                "usu_latitud": sso_usuario.usu_latitud,
                "usu_longitud": sso_usuario.usu_longitud,
                "usu_fechahora": sso_usuario.usu_fechahora,
                "nombre_estado": sso_usuario.estado.est_nombre,   
                "nombre_rol": sso_usuario.sso_rol.rol_nombre,             
            }
            for sso_usuario in result
        ]
        return sso_usuario_list
    
    def create_sso_usuario(self, sso_usuario: Sso_usuario):
        existing_user = self.db.query(Sso_usuarioModule).filter_by(usu_nickname=sso_usuario.usu_nickname).first()
        if existing_user:
            raise ValueError("El nickname ya está en uso. Por favor, elige otro.")
        else:
            new_sso_usuario = Sso_usuarioModule(
                usu_estado = sso_usuario.usu_estado,
                usu_rol= sso_usuario.usu_rol,
                usu_correo = sso_usuario.usu_correo,
                usu_documento = sso_usuario.usu_documento,
                usu_nombres = sso_usuario.usu_nombres,
                usu_apellidos = sso_usuario.usu_apellidos,
                usu_nickname = sso_usuario.usu_nickname,
                usu_clave = hash_sha256_then_md5_then_sha1_and_sha512(sso_usuario.usu_clave),
                usu_latitud = sso_usuario.usu_latitud,
                usu_longitud = sso_usuario.usu_longitud,
                usu_fechahora = sso_usuario.usu_fechahora,
            )
            self.db.add(new_sso_usuario)
            self.db.commit()
            send_registration_email(email = sso_usuario.usu_correo,nickname = sso_usuario.usu_nickname, clave = sso_usuario.usu_clave)
            return
    
    def update_sso_usuario(self, id: int, sso_usuario: Sso_usuario):
        result = self.db.query(Sso_usuarioModule).filter(Sso_usuarioModule.usu_id == id).first()
        result.usu_estado = sso_usuario.usu_estado
        result.usu_rol = sso_usuario.usu_rol
        result.usu_correo = sso_usuario.usu_correo
        result.usu_documento = sso_usuario.usu_documento
        result.usu_nombres = sso_usuario.usu_nombres
        result.usu_apellidos = sso_usuario.usu_apellidos
        result.usu_nickname = sso_usuario.usu_nickname
        result.usu_clave = sso_usuario.usu_clave
        result.usu_latitud = sso_usuario.usu_latitud
        result.usu_longitud = sso_usuario.usu_longitud
        result.usu_fechahora = sso_usuario.usu_fechahora
        self.db.commit()
        return

    def authenticate_user(self, nickname: str, clave: str):   
        password = hash_sha256_then_md5_then_sha1_and_sha512(clave)
        user = self.db.query(Sso_usuarioModule).filter(Sso_usuarioModule.usu_nickname == nickname, Sso_usuarioModule.usu_clave == password, Sso_usuarioModule.usu_estado == 1).first()                   
        return user
    
    def create_user_session(self, user_id: int, token: str) -> UserSessionModule:                 
        try:
            existing_session = self.db.query(UserSessionModule).filter_by(uses_iduser=user_id).first()
            current_time = datetime.now(local_timezone)

            if existing_session and existing_session.uses_active:
                raise HTTPException(status_code=400, detail="Ya hay una sesión activa para este usuario.")

            if existing_session:                
                existing_session.uses_token = token
                existing_session.uses_expiration_timestamp = current_time + timedelta(minutes=480)
                existing_session.uses_created_at = current_time
                existing_session.uses_active = True
                self.db.commit()
                self.db.refresh(existing_session)
                return existing_session
            else:                
                new_session = UserSessionModule(
                    uses_iduser=user_id,
                    uses_token=token,
                    uses_expiration_timestamp=current_time + timedelta(minutes=480),
                    uses_created_at=current_time,
                    uses_active=True
                )
                self.db.add(new_session)
                self.db.commit()
                self.db.refresh(new_session)
                return new_session
        except HTTPException as http_error:
            raise http_error
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al crear o actualizar la sesión de usuario")

    def deactivate_user_session(self, user_id: int) -> UserSessionModule:
        try:            
            existing_session = self.db.query(UserSessionModule).filter_by(uses_iduser=user_id).first()            
            if existing_session:   
                existing_session.uses_token = "null_session"         
                existing_session.uses_active = False
                self.db.commit()
                self.db.refresh(existing_session)
                return existing_session
            else:
                raise HTTPException(status_code=404, detail="Sesión no encontrada")
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar la sesión del usuario")