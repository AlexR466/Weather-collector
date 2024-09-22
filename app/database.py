from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import (
    POSTGRES_HOST, POSTGRES_NAME, POSTGRES_PASS, POSTGRES_USER
)


database_url = 'postgresql://{}:{}@{}/{}'.format(
    POSTGRES_USER, POSTGRES_PASS, POSTGRES_HOST, POSTGRES_NAME
)

engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
