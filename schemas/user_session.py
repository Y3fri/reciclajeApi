from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from schemas.sso_usuario import Sso_usuario


class UserSession(BaseModel):
    uses_id: Optional[int]
    uses_iduser: int
    uses_token: str
    uses_expiration_timestamp: datetime
    uses_created_at: datetime
    uses_active: bool
    usuario: Sso_usuario

    class Config:
        orm_mode = True