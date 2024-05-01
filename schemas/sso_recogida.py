from pydantic import BaseModel
from schemas.estado import Estado
from schemas.sso_cliente import Sso_cliente
from schemas.recogida import Recogida
from schemas.sso_usuario import Sso_usuario

class Sso_Recogida(BaseModel):
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
    sso_cliente:Sso_cliente
    estado:Estado    
    sso_usuario: Sso_usuario
    recogida:Recogida
    