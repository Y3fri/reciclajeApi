from fastapi import HTTPException
from models.sso_cliente import Sso_cliente  as Sso_clienteModule
from datetime import datetime, timedelta
from utils.hash import hash_sha256_then_md5_then_sha1_and_sha512
from schemas.sso_cliente import Sso_cliente
from utils.email_cliente import send_registration_email
from models.sso_recogida import Sso_recogida as Sso_recogidaModule
from models.UserCliSession import UserCliSession as UserCliSessionModule
from utils.jwt_manager_cliente import create_token_cli
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
        existing_user = self.db.query(Sso_clienteModule).filter_by(cli_nickname=sso_cliente.cli_nickname).first()
        if existing_user:
            raise ValueError("El nickname ya está en uso. Por favor, elige otro.")
        else:
            new_sso_cliente = Sso_clienteModule(
                cli_estado = sso_cliente.cli_estado,
                cli_correo = sso_cliente.cli_correo,
                cli_documento = sso_cliente.cli_documento,
                cli_nombres = sso_cliente.cli_nombres,
                cli_apellidos = sso_cliente.cli_apellidos,
                cli_nickname = sso_cliente.cli_nickname,
                cli_clave = hash_sha256_then_md5_then_sha1_and_sha512(sso_cliente.cli_clave),
                cli_telefono = sso_cliente.cli_telefono,
                cli_totalpuntos = 0            
            )
            self.db.add(new_sso_cliente)
            self.db.commit()
            send_registration_email(email = sso_cliente.cli_correo,nickname = sso_cliente.cli_nickname)
            return
    
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
            if existing_session:                
                existing_session.ses_token = token
                existing_session.ses_expiration_timestamp = current_time + timedelta(minutes=480)
                existing_session.ses_created_at = current_time
                self.db.commit()
                self.db.refresh(existing_session)
                return existing_session
            else:                
                new_session = UserCliSessionModule(
                    ses_idcliente=user_id,
                    ses_token=token,
                    ses_expiration_timestamp=current_time + timedelta(minutes=480),
                    ses_created_at=current_time
                )
                self.db.add(new_session)
                self.db.commit()
                self.db.refresh(new_session)
                return new_session
        except Exception as e:
            self.db.rollback()
            raise HTTPException(status_code=500, detail="Error al crear o actualizar la sesión de usuario")