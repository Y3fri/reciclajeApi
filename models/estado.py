from config.database import Base
from sqlalchemy import Column,Integer,String,Float

class Estado(Base):
    __tablename__="estado"

    est_id = Column(Integer, primary_key = True)
    est_nombre=Column(String(30))