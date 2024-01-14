from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.sso_usuario import Sso_usuario
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.sso_usuaio_service import Sso_usuarioService
from schemas.sso_usuario import Sso_usuario


sso_usuario_router = APIRouter()


@sso_usuario_router.get('/sso_usuario',tags=['Usuario'], response_model=list[Sso_usuario])
def get_sso_usuario()-> List [Sso_usuario]:
        db = Session()
        result = Sso_usuarioService(db).get_sso_usuario()
        return JSONResponse(content= jsonable_encoder(result))





