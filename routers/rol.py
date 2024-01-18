from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.rol import Sso_rol
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.rol_service import Sso_rolService
from schemas.rol import Sso_rol


sso_rol_router = APIRouter()


@sso_rol_router.get('/sso_rol',tags=['Sso_rol'], response_model=list[Sso_rol])
def get_rol()-> List [Sso_rol]:
        db = Session()
        result = Sso_rolService(db).get_rol()
        return JSONResponse(content= jsonable_encoder(result))

