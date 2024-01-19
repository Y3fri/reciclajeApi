from fastapi.security import HTTPBearer
from utils.jwt_manager import validate_token
from fastapi import Request, HTTPException

class JWTBearerCli(HTTPBearer):
    async def __call__(self, request: Request):
            auth =await super().__call__(request)
            data = validate_token(auth.credentials)
            cli_nickname = data.get('cli_nickname', None)
            if cli_nickname is None:
                raise HTTPException(status_code=403, detail="No tienes permisos para acceder a esta información")
            return auth
