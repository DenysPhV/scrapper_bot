from psycopg import connect, OperationalError

from src.settings.settings import settings


def create_connection(
        dbname: str = settings.DB_NAME,
        user: str = settings.DB_USER,
        password: str = settings.DB_PASSWORD,
        host: str = settings.DB_HOST,
        port: int = settings.DB_PORT,
):
    try:
        print("Connecting to database...")
        connection = connect(dbname=dbname, user=user, password=password, host=host, port=port)
        print("Connected to database!")

    except OperationalError as e:
        print(f"Error connecting to database: {e}")
        connection = None

    return connection


conn = create_connection()
