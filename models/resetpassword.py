from config.database import Base
from sqlalchemy import Column,Integer,String,Float,DateTime
from sqlalchemy.orm import relationship

class Resetpassword(Base):
    __tablename__="resetpassword"

    res_id = Column(Integer, primary_key = True)
    res_correo=Column(String(80))
    res_code=Column(String(6))
    res_expiration= Column((DateTime))