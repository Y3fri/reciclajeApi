from pydantic import BaseModel
from schemas.comuna import Comuna

class Recogida(BaseModel):
    reg_id: int
    reg_idcomuna: int
    reg_plastico: bool
    reg_papel: bool
    reg_carton: bool
    reg_metal: bool
    reg_vidrio: bool
    reg_ubicacion_lag: float
    reg_ubicacion_log: float
    reg_numero: str
    reg_direccion:str
    reg_barrio_conjunto:str
    comuna: Comuna

    class Config:
        orm_mode = True
