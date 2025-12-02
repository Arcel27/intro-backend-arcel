from sqlmodel import SQLModel, create_engine

DB_FILENAME = "backend_activity.db"
DB_URL = f"sqlite:///{DB_FILENAME}"

engine = create_engine(DB_URL, connect_args={"check_same_thread": False})

def init_db():
    SQLModel.metadata.create_all(engine)
