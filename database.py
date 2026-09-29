import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #"mysql+pymysql://root:omegamkii15@127.0.0.1:3306/todoapplicationdatabase"
    # "postgresql://postgres:omegamkii15@localhost/TodoAplicationDatabase"
    # "sqlite:///./todosapp.db"

if SQLALCHEMY_DATABASE_URI and SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI.replace("postgres://", "postgresql://", 1)

engine = create_engine(SQLALCHEMY_DATABASE_URI)
# engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass