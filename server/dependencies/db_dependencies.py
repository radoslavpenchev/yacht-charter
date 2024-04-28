
from app.database import get_session_maker


def get_db_session():
    session_local = get_session_maker()
    db_session = session_local()
    try:
        yield db_session
    finally:
        db_session.close()
