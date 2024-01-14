from models.sso_usuario import Sso_usuario  as Sso_usuarioModule
from schemas.sso_usuario import Sso_usuario

class Sso_usuarioService():

    def __init__(self,db) -> None:
        self.db = db

    def get_sso_usuario(self):      
        result = self.db.query(Sso_usuarioModule).all()
        sso_usuario_list = [
            {
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