from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.recogida import Recogida
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.recogida_service import RecogidaService
from schemas.recogida import Recogida


recogida_router = APIRouter()


@recogida_router.get('/recogida',tags=['Recogida'], response_model=list[Recogida])
def get_recogida()-> List [Recogida]:
        db = Session()
        result = RecogidaService(db).get_recogida()
        return JSONResponse(content= jsonable_encoder(result))

