from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.comuna import Comuna
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.comuna_service import ComunaService
from schemas.comuna import Comuna


comuna_router = APIRouter()


@comuna_router.get('/comuna',tags=['Comuna'], response_model=list[Comuna])
def get_comuna()-> List [Comuna]:
        db = Session()
        result = ComunaService(db).get_comuna()
        return JSONResponse(content= jsonable_encoder(result))

