from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

from app.env import HOSTNAME, PORT, USERNAME, PASSWORD, CHARSET, DATABASE, engine
import pymysql

SessionLacol = scoped_session(sessionmaker(autocommit=False, autoflush=False, bind=engine))
Base = declarative_base()
Base.query = SessionLacol.query_property()

conn = pymysql.connect(host=HOSTNAME, port=PORT, user=USERNAME, password=PASSWORD, db=DATABASE, charset=CHARSET)

SessionLacol = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)

def get_db():
    db = SessionLacol()
    try:
        yield db
    finally:
        db.close()

async def init_db():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        raise e