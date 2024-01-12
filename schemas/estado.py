from pydantic import BaseModel,Field
from typing import Optional


class Estado(BaseModel):
        est_id: Optional[int]=None
        est_nombre:str        
