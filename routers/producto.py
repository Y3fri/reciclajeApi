from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.producto import Producto
from fastapi.encoders import jsonable_encoder
from schemas.producto import Producto
from service.producto_service import ProductoService


producto_router = APIRouter()


@producto_router.get('/producto', tags=['Producto'], response_model=list[Producto])
def get_producto() -> List[Producto]:
        db = Session()
        try:
                result = ProductoService(db).get_producto()
                return JSONResponse(content=jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener las productos: {str(e)}"}, status_code=500)
        finally:
                db.close()



@producto_router.get('/productoTodo', tags=['Producto'], response_model=list[Producto],dependencies= [Depends(JWTBearer())])
def get_productoTodo() -> List[Producto]:
        db = Session()
        try:
                result = ProductoService(db).get_productoTodo()
                return JSONResponse(content=jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener las productos: {str(e)}"}, status_code=500)
        finally:
                db.close()


@producto_router.post('/producto', tags=['Producto'], response_model=dict,dependencies= [Depends(JWTBearer())])
def create_producto(producto: Producto) -> dict:
    db = Session()
    try:
        ProductoService(db).create_producto(producto)
        return JSONResponse(content={"message": "Se han insertado los datos correctamente"}, status_code=200)
    except Exception as e:
        print(f"Error: {str(e)}")
        return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@producto_router.put('/producto/{id}', tags=['Producto'], response_model=dict,dependencies= [Depends(JWTBearer())])
def update_producto(id: int, producto: Producto) -> dict:
        db = Session()
        try:             
                ProductoService(db).update_producto(id, producto)
                return JSONResponse(content={"message": "Producto actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el producto: {str(e)}"}, status_code=500)
        finally:
                db.close()

