from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#DATABASE_URL = "postgresql://user:password@localhost/dbname"
#engine = create_engine(DATABASE_URL)

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5432/flastapi-database"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine,autocommit=False,autoflush=False )
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close    