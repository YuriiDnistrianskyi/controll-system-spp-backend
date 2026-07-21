from app.database.engine import async_session

def get_async_session():
    with async_session() as session:
        yield session

def get_session_factory():
    return async_session
