from models.rol import Sso_rol  as Sso_rolModel

class Sso_rolService():

    def __init__(self,db) -> None:
        self.db = db

    def get_rol(self):
        result=self.db.query(Sso_rolModel).all()
        return result  