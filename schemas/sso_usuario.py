from pydantic import BaseModel
from typing import Optional
from schemas.estado import Estado
from schemas.rol import Sso_rol

class Sso_usuario(BaseModel):
        usu_id: Optional[int]=None
        usu_estado: int
        usu_rol:int
        usu_correo:str
        usu_documento:str
        usu_nombres:str   
        usu_apellidos:str
        usu_nickname:str
        usu_clave:str        
        usu_latitud:float
        usu_longitud:float
        usu_fechahora:str
        estado:Estado
        rol:Sso_rol