from pydantic import BaseModel
from typing import Optional


class Sso_rol(BaseModel):
        rol_id: Optional[int]=None
        rol_nombre:str        
