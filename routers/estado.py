from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.estado import Estado
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.estado_service import EstadoService
from schemas.estado import Estado


estado_router = APIRouter()


@estado_router.get('/estado',tags=['Estado'], response_model=list[Estado])
def get_estado()-> List [Estado]:
        db = Session()
        result = EstadoService(db).get_estado()
        return JSONResponse(content= jsonable_encoder(result))

