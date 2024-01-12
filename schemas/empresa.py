from pydantic import BaseModel,Field
from typing import Optional


class Empresa(BaseModel):
        inf_id: Optional[int]=None
        inf_municipio:str
        inf_nit:str
        inf_razon_social:str
        inf_email:str
        inf_direccion:str
        inf_telefono:str
        inf_logo:str
        inf_facebook:str
        inf_instagram:str
        inf_tiktok:str


