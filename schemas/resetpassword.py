from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Resetpassword(BaseModel):
        res_id: Optional[int]=None
        res_correo:str        
        res_code:str
        res_expiration: datetime
