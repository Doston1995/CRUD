from passlib.context import CryptContext
import  databases, sqlalchemy
from core.config import POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_SERVER, POSTGRES_PORT, POSTGRES_DB



pwd_context = CryptContext(schemes = ['bcrypt'], deprecated = 'auto')
DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()


engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)
    