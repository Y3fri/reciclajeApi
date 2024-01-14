from config.database import Base
from sqlalchemy import Column,Integer,String,Float
from sqlalchemy.orm import relationship

class Comuna(Base):
    __tablename__="comuna"

    com_id = Column(Integer, primary_key = True)
    com_nombre=Column(String(50))
    recogida = relationship("Recogida", back_populates="comuna")