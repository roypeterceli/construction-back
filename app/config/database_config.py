from venv import logger
from sqlalchemy import create_engine, URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
from sqlalchemy.exc import SQLAlchemyError

from app.config.app_config import db_property

try:
    connection_url = URL.create(
        drivername="postgresql+psycopg",
        host=db_property.host,
        port=db_property.port,
        database=db_property.name,
        username=db_property.user,
        password=db_property.password
    )

    engine = create_engine(
        connection_url,
        connect_args={"options": "-c search_path=public"},
        poolclass=QueuePool,
        pool_size=10,
        max_overflow=20,
        pool_timeout=30,
        pool_recycle=3600
    )

except SQLAlchemyError as e:
    logger.error("Error creating SQLAlchemy engine: %s", e)
    engine = None  

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()
