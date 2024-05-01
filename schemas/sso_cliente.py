from pydantic import BaseModel
from typing import Optional
from schemas.estado import Estado


class Sso_cliente(BaseModel):
        cli_id: Optional[int]=None
        cli_estado: int
        cli_correo:str
        cli_documento:str
        cli_nombres:str   
        cli_apellidos:str
        cli_nickname:str
        cli_clave:str
        cli_telefono:str
        cli_totalpuntos:int
        estado:Estado
