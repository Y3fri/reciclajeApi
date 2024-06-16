from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class Resetpasswordcli(BaseModel):
        resp_id: Optional[int]=None
        resp_correo:str        
        resp_code:str
        resp_expiration: datetime
