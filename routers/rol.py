from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.rol import Sso_rol
from fastapi.encoders import jsonable_encoder
from service.rol_service import Sso_rolService
from schemas.rol import Sso_rol


sso_rol_router = APIRouter()


@sso_rol_router.get('/sso_rol',tags=['Sso_rol'], response_model=list[Sso_rol],dependencies= [Depends(JWTBearer())])
def get_rol()-> List [Sso_rol]:
        db = Session()
        try:
                result = Sso_rolService(db).get_rol()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los roles: {str(e)}"}, status_code=500)
        finally:
                db.close()


