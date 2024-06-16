from fastapi import HTTPException
from models.sso_cliente import Sso_cliente  as Sso_clienteModule
from datetime import datetime, timedelta
from utils.hash import hash_sha256_then_md5_then_sha1_and_sha512
from schemas.sso_cliente import Sso_cliente
from utils.email_cliente import send_registration_email
from utils.email_password_cli import send_reset_password_email
from models.sso_recogida import Sso_recogida as Sso_recogidaModule
from models.UserCliSession import UserCliSession as UserCliSessionModule
from models.resetpasswordcli import Resetpasswordcli as ResetpasswordcliModule
from utils.jwt_manager_cliente import create_token_cli,validate_token_cli
import secrets

import pytz

local_timezone = pytz.timezone('America/Bogota')

class Sso_clienteService():

    

    def __init__(self,db) -> None:
        self.db = db

    def get_sso_cliente(self):      
        result = self.db.query(Sso_clienteModule).all()
        sso_cliente_list = [
            {
                "cli_estado": sso_cliente.cli_estado,
                "cli_correo": sso_cliente.cli_correo ,
                "cli_documento": sso_cliente.cli_documento ,
                "cli_nombres": sso_cliente.cli_nombres ,
                "cli_apellidos": sso_cliente.cli_apellidos ,
                "cli_nickname": sso_cliente.cli_nickname ,
                "cli_clave": sso_cliente.cli_clave ,
                "cli_telefono": sso_cliente.cli_telefono ,
                "cli_totalpuntos": sso_cliente.cli_totalpuntos,
                "cli_id": sso_cliente.cli_id,
                "nombre_estado": sso_cliente.estado.est_nombre,                
            }
            for sso_cliente in result
        ]
        return sso_cliente_list
    
    def get_sso_clienteId(self, cli_id):      
        result = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_id == cli_id).first()    
        if result:
            sso_cliente_data = {
                "cli_estado": result.cli_estado,
                "cli_correo": result.cli_correo,
                "cli_documento": result.cli_documento,
                "cli_nombres": result.cli_nombres,
                "cli_apellidos": result.cli_apellidos,
                "cli_nickname": result.cli_nickname,
                "cli_clave": result.cli_clave,
                "cli_telefono": result.cli_telefono,
                "cli_totalpuntos": result.cli_totalpuntos,
                "cli_id": result.cli_id,
                "nombre_estado": result.estado.est_nombre,
            }
            return sso_cliente_data
        
        return None

    
        
    def create_sso_cliente(self, sso_cliente: Sso_cliente):
        existing_user_by_nickname = self.db.query(Sso_clienteModule).filter_by(cli_nickname=sso_cliente.cli_nickname).first()
        existing_user_by_correo = self.db.query(Sso_clienteModule).filter_by(cli_correo=sso_cliente.cli_correo).first()
        
        if existing_user_by_nickname:
            raise ValueError("El nickname ya está en uso. Por favor, elige otro.")
        
        if existing_user_by_correo:
            raise ValueError("El correo electrónico ya está registrado. Por favor, usa otro correo.")
        
        new_sso_cliente = Sso_clienteModule(
            cli_estado=sso_cliente.cli_estado,
            cli_correo=sso_cliente.cli_correo,
            cli_documento=sso_cliente.cli_documento,
            cli_nombres=sso_cliente.cli_nombres,
            cli_apellidos=sso_cliente.cli_apellidos,
            cli_nickname=sso_cliente.cli_nickname,
            cli_clave=hash_sha256_then_md5_then_sha1_and_sha512(sso_cliente.cli_clave),
            cli_telefono=sso_cliente.cli_telefono,
            cli_totalpuntos=0
        )
        
        self.db.add(new_sso_cliente)
        self.db.commit()
        
        send_registration_email(email=sso_cliente.cli_correo, nickname=sso_cliente.cli_nickname)
        
        return "Usuario creado exitosamente"

    
    def update_sso_cliente(self, id: int, sso_cliente: Sso_cliente):
        result = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_id == id).first()
        result.cli_estado = sso_cliente.cli_estado
        result.cli_correo = sso_cliente.cli_correo
        result.cli_documento = sso_cliente.cli_documento
        result.cli_nombres = sso_cliente.cli_nombres
        result.cli_apellidos = sso_cliente.cli_apellidos
        result.cli_nickname = sso_cliente.cli_nickname
        result.cli_clave = sso_cliente.cli_clave
        result.cli_telefono = sso_cliente.cli_telefono  
        result.cli_totalpuntos = sso_cliente.cli_totalpuntos      
        self.db.commit()
        return
    
    def calcular_total_puntos(self, id):        
        result = self.db.query(Sso_recogidaModule).filter(Sso_recogidaModule.sreg_idcliente == id).all()
        total_puntos = sum(punto.sreg_puntos for punto in result)
        print(f"Total de puntos: {total_puntos}")
        return total_puntos

    def update_sso_cliente_puntos(self, id: int, sso_cliente: Sso_cliente):
        result = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_id == id).first()
        result.cli_estado = sso_cliente.cli_estado
        result.cli_correo = sso_cliente.cli_correo
        result.cli_documento = sso_cliente.cli_documento
        result.cli_nombres = sso_cliente.cli_nombres
        result.cli_apellidos = sso_cliente.cli_apellidos
        result.cli_nickname = sso_cliente.cli_nickname
        result.cli_clave = sso_cliente.cli_clave
        result.cli_telefono = sso_cliente.cli_telefono  
        result.cli_totalpuntos = self.calcular_total_puntos(id)
        self.db.commit()
        return


    def authenticate_user(self, nickname: str, clave: str):
        password = hash_sha256_then_md5_then_sha1_and_sha512(clave)
        user = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_nickname == nickname, Sso_clienteModule.cli_clave == password, Sso_clienteModule.cli_estado == 1).first()
        return user

    

    def create_user_session(self, user_id: int, token: str) -> UserCliSessionModule:                 
        try:
            existing_session = self.db.query(UserCliSessionModule).filter_by(ses_idcliente=user_id).first()
            current_time = datetime.now(local_timezone)

            if existing_session and existing_session.ses_active:
                raise HTTPException(status_code=400, detail="Ya hay una sesión activa para este usuario.")

            if existing_session:                
                existing_session.ses_token = token
                existing_session.ses_expiration_timestamp = current_time + timedelta(minutes=480)
                existing_session.ses_created_at = current_time
                existing_session.ses_active = True
                self.db.commit()
                self.db.refresh(existing_session)
                return existing_session
            else:                
                new_session = UserCliSessionModule(
                    ses_idcliente=user_id,
                    ses_token=token,
                    ses_expiration_timestamp=current_time + timedelta(minutes=480),
                    ses_created_at=current_time,
                    ses_active=True
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

        
    def deactivate_user_session(self, user_id: int) -> UserCliSessionModule:
        try:            
            existing_session = self.db.query(UserCliSessionModule).filter_by(ses_idcliente=user_id).first()            
            if existing_session:   
                existing_session.ses_token = "null_session"         
                existing_session.ses_active = False
                self.db.commit()
                self.db.refresh(existing_session)
                return existing_session
            else:
                raise HTTPException(status_code=404, detail="Sesión no encontrada")
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al actualizar la sesión del usuario")
    
    
    def generate_verification_code(self, length=6):
        return ''.join(secrets.choice('0123456789') for i in range(length))

    def code_password(self, correo: str):
        try:
            user = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_correo == correo).first()
            if not user:
                raise ValueError("No se encontró ningún usuario con ese correo electrónico")

            verification_code = self.generate_verification_code()
            current_time = datetime.now(local_timezone)
            expiration_time = current_time + timedelta(minutes=1)
            reset_password_entry = self.db.query(ResetpasswordcliModule).filter(ResetpasswordcliModule.resp_correo == correo).first()
            
            if reset_password_entry:
                reset_password_entry.resp_code = verification_code
                reset_password_entry.resp_expiration = expiration_time
            else:
                new_reset_password = ResetpasswordcliModule(
                    resp_correo=correo,
                    resp_code=verification_code,
                    resp_expiration=expiration_time
                )
                self.db.add(new_reset_password)
            
            self.db.commit()
                    
            
            send_reset_password_email(email=correo, verification_code=verification_code)
            return expiration_time,correo
        finally:
            self.db.close()



    def valid_code(self, code: str):
        try:
            reset_entry = self.db.query(ResetpasswordcliModule).filter(ResetpasswordcliModule.resp_code == code).first()
            if not reset_entry:
                raise ValueError("Código de verificación no encontrado")
            
            current_time = datetime.utcnow()
            if reset_entry.resp_expiration > current_time:
                raise ValueError("El código de verificación ha expirado")

            token_data = {"sub": reset_entry.resp_correo}
            token = create_token_cli(token_data)
            return token
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            self.db.close()

    def reset_password_with_token(self, token: str, new_password: str):
        try:
            payload = validate_token_cli(token)
            if not payload:
                raise ValueError("Token inválido o expirado")

            correo = payload.get("sub")
            if not correo:
                raise ValueError("No se pudo obtener el correo del token")

            user = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_correo == correo).first()
            if not user:
                raise ValueError("No se encontró ningún usuario con ese correo electrónico")

            user.cli_clave = hash_sha256_then_md5_then_sha1_and_sha512(new_password)

            reset_entry = self.db.query(ResetpasswordcliModule).filter(ResetpasswordcliModule.resp_correo == correo).first()
            if reset_entry:
                self.db.delete(reset_entry)
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            self.db.close()

    def delete_code(self, correo:str):
        try:
            reset_entry = self.db.query(ResetpasswordcliModule).filter(ResetpasswordcliModule.resp_correo == correo).first()
            if reset_entry:
                self.db.delete(reset_entry)
                self.db.commit()
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail=str(e))
        finally:
            self.db.close()     