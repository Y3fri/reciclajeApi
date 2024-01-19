from models.sso_cliente import Sso_cliente  as Sso_clienteModule
from sqlalchemy.orm import Session
from utils.hash import hash_sha256_then_md5_then_sha1_and_sha512
from schemas.sso_cliente import Sso_cliente
from utils.email_cliente import send_registration_email


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
                "cli_id": sso_cliente.cli_id,
                "nombre_estado": sso_cliente.estado.est_nombre,                
            }
            for sso_cliente in result
        ]
        return sso_cliente_list
    
    
    def create_sso_cliente(self, sso_cliente: Sso_cliente):
        new_sso_cliente = Sso_clienteModule(
            cli_estado = sso_cliente.cli_estado,
            cli_correo = sso_cliente.cli_correo,
            cli_documento = sso_cliente.cli_documento,
            cli_nombres = sso_cliente.cli_nombres,
            cli_apellidos = sso_cliente.cli_apellidos,
            cli_nickname = sso_cliente.cli_nickname,
            cli_clave = hash_sha256_then_md5_then_sha1_and_sha512(sso_cliente.cli_clave),
            cli_telefono = sso_cliente.cli_telefono,            
        )
        self.db.add(new_sso_cliente)
        self.db.commit()
        send_registration_email(email = sso_cliente.usu_correo,nickname = sso_cliente.usu_nickname)
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
        self.db.commit()
        return


    def authenticate_user(self, nickname: str, clave: str):   
        password = hash_sha256_then_md5_then_sha1_and_sha512(clave)
        user = self.db.query(Sso_clienteModule).filter(Sso_clienteModule.cli_nickname == nickname, Sso_clienteModule.cli_clave == password).first()                      
        return user
        