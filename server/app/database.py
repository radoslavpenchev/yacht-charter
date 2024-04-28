from functools import lru_cache
from sqlalchemy import Engine, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

DB_URL = "postgresql://postgres@localhost:5432/yacht-charter"

@lru_cache
def get_engine() -> Engine:
    return create_engine(DB_URL)


@lru_cache
def get_session_maker() -> sessionmaker[Session]:
    engine = get_engine()
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
