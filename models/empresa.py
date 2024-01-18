from config.database import Base
from sqlalchemy import Column,Integer,String,Float

class Empresa(Base):
    __tablename__="empresa"

    inf_id = Column(Integer, primary_key = True)
    inf_municipio=Column(String(80))
    inf_nit=Column(String(12))
    inf_razon_social=Column(String(80))
    inf_email=Column(String(50))
    inf_direccion=Column(String(50))
    inf_telefono=Column(String(50))
    inf_logo=Column(String(200))
    inf_facebook=Column(String(500))
    inf_instagram=Column(String(500))
    inf_tiktok=Column(String(500))