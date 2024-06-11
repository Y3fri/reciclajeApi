from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.cliente_producto import Cliente_producto
from fastapi.encoders import jsonable_encoder
from service.cliente_producto_service import Cliente_productoService
from schemas.cliente_producto import Cliente_producto
from middlewares.jwt_bearer_cliente import JWTBearerCli


cliente_producto_router = APIRouter()


@cliente_producto_router.get('/cliente_producto', tags=['Cliente_producto'], response_model=list[Cliente_producto])
def get_cliente_producto() -> List[Cliente_producto]:
        db = Session()
        try:
                result = Cliente_productoService(db).get_Cliente_producto()
                return JSONResponse(content=jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener la información: {str(e)}"}, status_code=500)
        finally:
                db.close()

                


@cliente_producto_router.post('/cliente_producto', tags=['Cliente_producto'], response_model=dict, dependencies=[Depends(JWTBearerCli())])
def create_cliente_producto(cliente_producto: Cliente_producto) -> dict:
    db = Session()
    try:
        Cliente_productoService(db).create_cliente_producto(cliente_producto)
        return JSONResponse(content={"message": "Se han insertado los datos correctamente"}, status_code=200)
    except ValueError as e:        
        return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=400)
    except Exception as e:        
        print(f"Error interno del servidor: {str(e)}")
        return JSONResponse(content={"error": "Error interno del servidor"}, status_code=500)
    finally:
        db.close()

@cliente_producto_router.put('/cliente_producto/{id}', tags=['Cliente_producto'], response_model=dict)
def update_cliente_producto(id: int, cliente_producto: Cliente_producto) -> dict:
        db = Session()
        try:             
                Cliente_productoService(db).update_cliente_producto(id, cliente_producto)
                return JSONResponse(content={"message": "Información actualizada"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar la información: {str(e)}"}, status_code=500)
        finally:
                db.close()
