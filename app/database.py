from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import (
    DB_HOST, DB_NAME, DB_PASS, DB_USER
)


database_url = f'postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}'

engine = create_engine(database_url)

Session = sessionmaker(bind=engine)
