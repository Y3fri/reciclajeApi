from pydantic import BaseModel
from schemas.sso_cliente import Sso_cliente
from schemas.producto import Producto

class Cliente_producto(BaseModel):
    clip_id: int
    clip_idcliente: int
    clip_idproducto: int
    clip_latitud: float
    clip_longitud: float  
    clip_cantidad: int
    sso_cliente: Sso_cliente
    producto:Producto

    class Config:
        orm_mode = True
