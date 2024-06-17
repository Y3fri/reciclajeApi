from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from fastapi import Request, HTTPException

class JWTBearer(HTTPBearer):
    def __init__(self, allowed_roles: list = None, auto_error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_error)
        self.allowed_roles = allowed_roles

    async def __call__(self, request: Request):
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data is None:
            raise HTTPException(status_code=403, detail="Credenciales inválidas")

        user_role = data.get('usu_rol', None)
        if user_role is None or (self.allowed_roles and user_role not in self.allowed_roles):            
            raise HTTPException(status_code=403, detail="No tienes permisos para acceder a esta información")

        return data
