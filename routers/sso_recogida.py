from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.sso_recogida import Sso_recogida
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.sso_recogida_service import Sso_recogidaService
from schemas.sso_recogida import Sso_Recogida  

sso_recogida_router = APIRouter()

@sso_recogida_router.get('/sso_recogida', tags=['Sso_recogidas'], response_model=List[Sso_Recogida])
def get_sso_recogida() -> List[Sso_Recogida]:
    db = Session()
    result = Sso_recogidaService(db).get_sso_recogida()
    return JSONResponse(content=jsonable_encoder(result))



