from models.empresa import Empresa as EmpresaModel

class EmpresaService():

    def __init__(self,db) -> None:
        self.db = db

    def get_empresas(self):
        result=self.db.query(EmpresaModel).all()
        return result  


