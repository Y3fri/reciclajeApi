from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from fastapi.encoders import jsonable_encoder
from service.sso_recogida_service import Sso_recogidaService
from schemas.sso_recogida import Sso_Recogida  

sso_recogida_router = APIRouter()

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



