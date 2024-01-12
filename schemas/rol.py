from pydantic import BaseModel,Field
from typing import Optional


class Sso_rol(BaseModel):
        rol_id: Optional[int]=None
        rol_nombre:str        
