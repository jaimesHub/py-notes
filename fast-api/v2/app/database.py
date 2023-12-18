from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time

from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}/{settings.database_name}"

# Create the SQLAlchemy `engine`
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a `SessionLocal` class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a `Base` class
Base = declarative_base()

# Dependency
def get_db():
    """Using SQLAlchemy ORM instead of psycopg2 driver"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     """Connecting to our database using the regular Postgres driver::psycopg2"""
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             dbname="fastapi", 
#             user="jaimes", 
#             password="123456",
#             cursor_factory=RealDictCursor
#         )

#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error::", error)
#         time.sleep(2)