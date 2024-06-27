from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.recogida import Recogida
from fastapi.encoders import jsonable_encoder
from schemas.sso_recogida import Sso_Recogida
from service.recogida_service import RecogidaService
from schemas.recogida import Recogida
from middlewares.jwt_bearer_cliente import JWTBearerCli


recogida_router = APIRouter()


@recogida_router.get('/recogida', tags=['Recogida'], response_model=list[Recogida])
def get_recogida() -> List[Recogida]:
        db = Session()
        try:
                result = RecogidaService(db).get_recogida()
                return JSONResponse(content=jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener las recogidas: {str(e)}"}, status_code=500)
        finally:
                db.close()


@recogida_router.post('/recogida',tags=['Recogida'],response_model=dict, dependencies= [Depends(JWTBearerCli())])
def create_recogida(recogida:Recogida, sso_recogida: Sso_Recogida)-> dict:
        db = Session()
        try:
                RecogidaService(db).create_recogida(recogida,sso_recogida)               
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        finally:
                db.close()


@recogida_router.put('/recogida/{id}', tags=['Recogida'], response_model=dict)
def update_recogida(id: int, recogida: Recogida) -> dict:
        db = Session()
        try:             
                RecogidaService(db).update_recogida(id, recogida)
                return JSONResponse(content={"message": "Recogida actualizada"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar la recogida: {str(e)}"}, status_code=500)
        finally:
                db.close()

