from pydantic import BaseModel,Field
from typing import Optional


class Comuna(BaseModel):
        com_id: Optional[int]=None
        com_nombre:str        
