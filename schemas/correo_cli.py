from pydantic import BaseModel

class CorreoCli(BaseModel):
    correo: str


class CodeCli(BaseModel):
    code: str

class PasswordReset(BaseModel):
    token: str
    new_password: str
