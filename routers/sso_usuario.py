from fastapi import APIRouter, Depends, HTTPException
from fastapi.responses import JSONResponse
from typing import List
from config.database import Session
from middlewares.jwt_bearer import JWTBearer
from models.sso_usuario import Sso_usuario
from fastapi.encoders import jsonable_encoder
from service.sso_usuaio_service import Sso_usuarioService
from schemas.sso_usuario import Sso_usuario
from utils.jwt_manager import create_token
from schemas.correo_cli import CorreoCli,PasswordReset,CodeCli
from schemas.user_usu import User_usu


sso_usuario_router = APIRouter()


@sso_usuario_router.get('/sso_usuario',tags=['Usuario'], response_model=list[Sso_usuario],dependencies=[Depends(JWTBearer(allowed_roles=[1]))])
def get_sso_usuario()-> List [Sso_usuario]:
        db = Session()
        try:
                result = Sso_usuarioService(db).get_sso_usuario()
                return JSONResponse(content= jsonable_encoder(result))
        except Exception as e:        
                return JSONResponse(content={"error": f"Error al obtener los usuarios: {str(e)}"}, status_code=500)
        finally:
                db.close()

@sso_usuario_router.post('/sso_usuario',tags=['Usuario'],response_model=dict,dependencies=[Depends(JWTBearer(allowed_roles=[1]))])
def create_usuario(usuario:Sso_usuario)-> dict:
        db = Session()
        try:
                Sso_usuarioService(db).create_sso_usuario(usuario)
                return JSONResponse(content={"message":"Se han insertado los datos correctamente"}, status_code=200)
        except Exception as e:
                return JSONResponse(content={"error": f"Error al insertar los datos: {str(e)}"}, status_code=500)


@sso_usuario_router.put('/sso_usuario/{id}', tags=['Usuario'], response_model=dict,dependencies=[Depends(JWTBearer(allowed_roles=[1]))])
def update_sso_usuario(id: int, sso_usuario: Sso_usuario) -> dict:
        db = Session()
        try:               
                Sso_usuarioService(db).update_sso_usuario(id, sso_usuario)
                return JSONResponse(content={"message": "usuario actualizado"})
        except Exception as e:                
                return JSONResponse(content={"error": f"Error al actualizar el usuario: {str(e)}"}, status_code=500)
        finally:
                db.close()



@sso_usuario_router.post('/login', tags=['Auth'])
def login(user: User_usu):    
        db = Session()
        try:
                result =Sso_usuarioService(db).authenticate_user(user.usu_nickname, user.usu_clave)
                if result:  
                        user_data = {
                            "usu_nickname": result.usu_nickname,
                            "usu_rol": result.usu_rol,
                            "usu_id": result.usu_id
                        }            
                        token = create_token(user_data)   
                        session = Sso_usuarioService(db).create_user_session(result.usu_id, token)                  
                        return {"token": token, "usu_estado": result.usu_estado, "usu_rol": result.usu_rol, "session": session}
                else:
                        raise HTTPException(status_code=401, detail="Credenciales inválidas")
        except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))
        finally:
                db.close()



@sso_usuario_router.put('/deactivate-session/{user_id}', tags=['Auth'])
def deactivate_session(user_id: int):  
    db = Session()  
    try:
        service = Sso_usuarioService(db)
        updated_session = service.deactivate_user_session(user_id)
        return {"message": "Sesión desactivada con éxito", "session": updated_session}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    finally:
        db.close()


@sso_usuario_router.post('/send-emailUsu', tags=['ResetUsu'])
def request_password_reset(correo: CorreoCli):
    db=Session()
    service = Sso_usuarioService(db)
    try:
        expiration,correousu =service.code_password(correo.correo)
        return {"message": "Código de recuperación de contraseña enviado con éxito", 
                "expiration": expiration,
                "correo": correousu}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@sso_usuario_router.post('/valid-codeUsu', tags=['ResetUsu'])
def valid_code(code: CodeCli):
    db=Session()
    service = Sso_usuarioService(db)
    try:
        token = service.valid_code(code.code)
        return {"message": "Código de verificación válido", "token": token}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()        

@sso_usuario_router.post('/reset-passwordUsu', tags=['ResetUsu'])
def reset_password(data: PasswordReset):
    db=Session()
    service = Sso_usuarioService(db)
    try:
        service.reset_password_with_token(data.token, data.new_password)
        return {"message": "Contraseña restablecida con éxito"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        db.close()

@sso_usuario_router.delete('/delete-codeUsu', tags=['ResetUsu'])
def deactivate_session(correo: CorreoCli):  
    db = Session()  
    try:
        service = Sso_usuarioService(db)
        service.delete_code(correo.correo)
        return {"message": "No fue posible cambiar la contraseña"}
    except HTTPException as e:
        raise HTTPException(status_code=e.status_code, detail=e.detail)
    finally:
        db.close()



