from pydantic import BaseModel
from schemas.empresa import Empresa
from schemas.estado import Estado

class Producto(BaseModel):
    pro_id: int
    pro_empresa: int
    pro_estado: int
    pro_foto: str
    pro_nombre: str
    pro_puntos : int
    pro_cantidad: int
    empresa: Empresa
    estado: Estado

    class Config:
        orm_mode = True
