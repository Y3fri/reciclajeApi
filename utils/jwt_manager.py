from datetime import datetime, timedelta
from fastapi import HTTPException
from jose import JWTError, jwt
from schemas.sso_usuario import Sso_usuario

SECRET_KEY = "tu_secreto"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_token(data: dict):
    try:
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        print(f"Token generado con éxito: {encoded_jwt}")
        return encoded_jwt
    except JWTError as e:
        # Agrega logs para imprimir detalles sobre la excepción
        print(f"Error al generar el token: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el token")


def validate_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None