from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()
DB_URL = "postgresql://fastapi_test:fastapi_test_password@localhost:5432/db"
SQLALCHEMY_DATABASE_URL = (DB_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
)

SessionLocal = sessionmaker(bind=engine)
