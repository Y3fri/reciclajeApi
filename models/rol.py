from config.database import Base
from sqlalchemy import Column,Integer,String,Float

class Sso_rol(Base):
    __tablename__="sso_rol"

    rol_id = Column(Integer, primary_key = True)
    rol_nombre=Column(String(50))