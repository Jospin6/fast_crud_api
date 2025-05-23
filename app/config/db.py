# app/config/db.py
from sqlmodel import SQLModel, create_engine, Session
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session

def init_db():
    from app.models.item_model import Item 
    SQLModel.metadata.create_all(engine)