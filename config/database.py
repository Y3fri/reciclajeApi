from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from urllib.parse import quote

password = quote("Y3f3r#@+")
mysql_file_name = f"mysql+mysqlconnector://root:{password}@localhost:3306/reciclarDB"

engine = create_engine(mysql_file_name, echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()
