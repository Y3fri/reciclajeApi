from fastapi import APIRouter,HTTPException
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from models.sso_cliente import Sso_cliente
from fastapi.encoders import jsonable_encoder
from schemas.user_cli import User_cli
from service.sso_cliente_service import Sso_clienteService
from schemas.sso_cliente import Sso_cliente
from utils.jwt_manager_cliente import create_token_cli

sso_cliente_router = APIRouter()


@sso_cliente_router.get('/sso_cliente',tags=['Cliente'], response_model=list[Sso_cliente])
def get_sso_cliente()-> List [Sso_cliente]:
        db = Session()
        try:
                result = Sso_clienteService(db).get_sso_cliente()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los clientes: {str(e)}"}, status_code=500)
        finally:
                db.close()

@sso_cliente_router.post('/sso_cliente',tags=['Cliente'],response_model=dict)
def create_cliente(cliente:Sso_cliente)-> dict:
        db = Session()
        try:
                Sso_clienteService(db).create_sso_cliente(cliente)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@sso_cliente_router.put('/sso_cliente/{id}', tags=['Cliente'], response_model=dict)
def update_sso_cliente(id: int, sso_cliente: Sso_cliente) -> dict:
        db = Session()
        try:               
                Sso_clienteService(db).update_sso_cliente(id, sso_cliente)
                return JSONResponse(content={"message": "Cliente actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el Cliente: {str(e)}"}, status_code=500)
        finally:
                db.close()


@sso_cliente_router.put('/sso_cliente/puntos/{id}', tags=['Cliente'], response_model=dict)
def update_sso_cliente(id: int, sso_cliente: Sso_cliente) -> dict:
        db = Session()
        try:               
                Sso_clienteService(db).update_sso_cliente_puntos(id, sso_cliente)
                return JSONResponse(content={"message": "Puntos actualizados"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar los puntos: {str(e)}"}, status_code=500)
        finally:
                db.close()

@sso_cliente_router.post('/loginCli', tags=['Auth'])
def login(user: User_cli):    
        db = Session()
        try:
                result =Sso_clienteService(db).authenticate_user(user.cli_nickname, user.cli_clave)
                if result:               
                        token = create_token_cli(user.dict())                  
                        return {"token": token, "cli_estado": result.cli_estado, "cli_id": result.cli_id, "cli_totalpuntos": result.cli_totalpuntos}
                else:
                        raise HTTPException(status_code=401, detail="Credenciales inválidas")
        except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        finally:
                db.close()






