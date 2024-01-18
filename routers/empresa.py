from fastapi import APIRouter
from fastapi import Path, Query, Depends
from fastapi.responses import JSONResponse
from pydantic import BaseModel,Field
from typing import Optional, List
from config.database import Session
from models.empresa import Empresa
from fastapi.encoders import jsonable_encoder
from middlewares.jwt_bearer import JWTBearer
from service.empresa_service import EmpresaService
from schemas.empresa import Empresa


empresa_router = APIRouter()


@empresa_router.get('/empresa',tags=['Empresa'], response_model=list[Empresa])
def get_empresas()-> List [Empresa]:
        db = Session()
        result = EmpresaService(db).get_empresas()
        return JSONResponse(content= jsonable_encoder(result))

