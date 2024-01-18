from fastapi import APIRouter, HTTPException
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
from utils.jwt_manager import create_token
from schemas.user_usu import User_usu


sso_usuario_router = APIRouter()


@sso_usuario_router.get('/sso_usuario',tags=['Usuario'], response_model=list[Sso_usuario])
def get_sso_usuario()-> List [Sso_usuario]:
        db = Session()
        result = Sso_usuarioService(db).get_sso_usuario()
        return JSONResponse(content= jsonable_encoder(result))

@sso_usuario_router.post('/login', tags=['Auth'])
def login(user: User_usu):    
    db = Session()
    try:
        result =Sso_usuarioService(db).authenticate_user(user.usu_nickname, user.usu_clave)
        if result:   
            print(result.usu_nickname)
            print(result.usu_estado)
            token = create_token(user.dict())                  
            return {"token": token, "usu_estado": result.usu_estado, "usu_rol": result.usu_rol}
        else:
            raise HTTPException(status_code=401, detail="Credenciales inválidas")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()








