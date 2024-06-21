from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from service.sso_recogida_service import Sso_recogidaService
from schemas.sso_recogida import Sso_Recogida  

sso_recogida_router = APIRouter()


@sso_recogida_router.get('/sso_recogida_id/{id}', tags=['Sso_recogidas'], response_model=List[Sso_Recogida])
def get_sso_recogida_id(id: int) -> List[Sso_Recogida]:
    db = Session()
    try:
        result = Sso_recogidaService(db).get_sso_recogida_id(id)
        return JSONResponse(content=jsonable_encoder(result))
    except Exception as e:        
        return JSONResponse(content={"error": f"Error al obtener los datos de la recogida: {str(e)}"}, status_code=500)
    finally:
        db.close()


@sso_recogida_router.get('/sso_recogida', tags=['Sso_recogidas'], response_model=List[Sso_Recogida])
def get_sso_recogida() -> List[Sso_Recogida]:
    db = Session()
    try:
        result = Sso_recogidaService(db).get_sso_recogida()
        return JSONResponse(content=jsonable_encoder(result))
    except Exception as e:        
        return JSONResponse(content={"error": f"Error al obtener los datos de la recogida: {str(e)}"}, status_code=500)
    finally:
        db.close()



@sso_recogida_router.get('/sso_recogida_asignacion', tags=['Sso_recogidas'], response_model=List[Sso_Recogida])
def get_sso_recogida_asignacion() -> List[Sso_Recogida]:
    db = Session()
    try:
        result = Sso_recogidaService(db).get_sso_recogida_asignacion()
        return JSONResponse(content=jsonable_encoder(result))
    except Exception as e:        
        return JSONResponse(content={"error": f"Error al obtener los datos de la recogida: {str(e)}"}, status_code=500)
    finally:
        db.close()

@sso_recogida_router.put('/sso_recogida/puntos/{id}', tags=['Sso_recogidas'], response_model=dict)
def update_sso_recogida(id: int, sso_recogida: Sso_Recogida) -> dict:
        db = Session()
        try:               
                Sso_recogidaService(db).update_sso_recogida(id, sso_recogida)
                return JSONResponse(content={"message": "Asignacion con exito"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar los puntos: {str(e)}"}, status_code=500)
        finally:
                db.close()

@sso_recogida_router.put('/sso_recogida_trabajador/puntos/{id}', tags=['Sso_recogidas'], response_model=dict)
def update_sso_recogida_trabajador(id: int,idtrabajador:int, sso_recogida: Sso_Recogida) -> dict:
        db = Session()
        try:               
                Sso_recogidaService(db).update_sso_recogida_trabajo(id, idtrabajador, sso_recogida)
                return JSONResponse(content={"message": "Puntos actualizados"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar los puntos: {str(e)}"}, status_code=500)
        finally:
                db.close()

