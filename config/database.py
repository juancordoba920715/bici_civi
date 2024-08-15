from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


DATABASE_URL="mysql+pymysql://root:@localhost:3306/bike"#base de datos

engine=create_engine(DATABASE_URL)

base=declarative_base()

SessionLocal=sessionmaker(bind=engine)


def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close() 
        

