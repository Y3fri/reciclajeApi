from models.comuna import Comuna  as ComunaModel


class ComunaService():

    def __init__(self,db) -> None:
        self.db = db

    def get_comuna(self):
        result=self.db.query(ComunaModel).all()
        return result  