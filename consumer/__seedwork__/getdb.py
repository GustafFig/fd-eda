from sqlalchemy import sessionmaker, make_url
from consumer.config import settings


def create_sqlalchemy_conn(session_args):
    engine = make_url(settings.database_conn_str)
    return engine, sessionmaker(**session_args, bind=engine)


# Create a session factory
engine, SessionLocal = create_sqlalchemy_conn(session_args=dict(autocommit=False, autoflush=False))

# create a dependecy function to get the db
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
