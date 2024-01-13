from pydantic import BaseModel,Field
from typing import Optional
from schemas.estado import Estado
from schemas.sso_cliente import Sso_cliente
from schemas.recogida import Recogida
from schemas.sso_usuario import Sso_usuario

class SsoRecogida(BaseModel):
    sreg_idcliente: int
    sreg_idestado: int
    sreg_idrecogida: int
    sreg_idtrabajador: int
    sreg_puntos: int
    sreg_peso: float
    sreg_fecha: str
    sreg_hora1: str
    sreg_hora2: str
    sreg_asignacion: bool
    cliente:Sso_cliente
    estado:Estado
    recogida:Recogida
    trabajador: Sso_usuario