"""
This module contains database-related functionality,
including database connection setup,

"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


load_dotenv()

engine = create_engine("postgresql://postgres:15321598753@localhost/GOS")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    """
    Get a database session.
    Returns:
     A database session object.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
