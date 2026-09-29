import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    #"mysql+pymysql://root:omegamkii15@127.0.0.1:3306/todoapplicationdatabase"
    # "postgresql://postgres:omegamkii15@localhost/TodoAplicationDatabase"
    # "sqlite:///./todosapp.db"

engine = create_engine(SQLALCHEMY_DATABASE_URI, connect_args = {"check_same_thread": False})
# engine = create_engine(SQLALCHEMY_DATABASE_URI)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass