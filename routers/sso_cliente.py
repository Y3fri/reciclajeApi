from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.sso_cliente import Sso_cliente
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.sso_cliente_service import Sso_clienteService
from schemas.sso_cliente import Sso_cliente


sso_cliente_router = APIRouter()


@sso_cliente_router.get('/sso_cliente',tags=['Cliente'], response_model=list[Sso_cliente])
def get_sso_cliente()-> List [Sso_cliente]:
        db = Session()
        result = Sso_clienteService(db).get_sso_cliente()
        return JSONResponse(content= jsonable_encoder(result))





