from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.comuna import Comuna
from fastapi.encoders import jsonable_encoder
from service.comuna_service import ComunaService
from schemas.comuna import Comuna


comuna_router = APIRouter()


@comuna_router.get('/comuna',tags=['Comuna'], response_model=list[Comuna])
def get_comuna()-> List [Comuna]:
        db = Session()
        try:
                result = ComunaService(db).get_comuna()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener las comunas: {str(e)}"}, status_code=500)
        finally:
                db.close()

