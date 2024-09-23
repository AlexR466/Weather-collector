from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import (
    POSTGRES_HOST, POSTGRES_DB, POSTGRES_PASSWORD, POSTGRES_USER
)


database_url = 'postgresql://{}:{}@{}/{}'.format(
    POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_DB
)

engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
