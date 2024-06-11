from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.sso_cliente import Sso_cliente


class UserCliSession(BaseModel):
    ses_id: Optional[int]
    ses_idcliente: int
    ses_token: str
    ses_expiration_timestamp: datetime
    ses_created_at: datetime
    cliente: Sso_cliente

    class Config:
        orm_mode = True