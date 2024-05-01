from fastapi import APIRouter
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.empresa import Empresa
from fastapi.encoders import jsonable_encoder
from service.empresa_service import EmpresaService
from schemas.empresa import Empresa


empresa_router = APIRouter()


@empresa_router.get('/empresa',tags=['Empresa'], response_model=list[Empresa])
def get_empresas()-> List [Empresa]:
        db = Session()
        try:
                result = EmpresaService(db).get_empresas()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener la empresa: {str(e)}"}, status_code=500)
        finally:
                db.close()


