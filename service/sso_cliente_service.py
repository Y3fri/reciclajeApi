from models.sso_cliente import Sso_cliente  as Sso_clienteModule
from schemas.sso_cliente import Sso_cliente

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