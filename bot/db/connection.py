import sys
import os
import psycopg
from psycopg import connect, OperationalError

from settings.settings import settings
from log.logger import get_logger

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../../'))

logger = get_logger()

def create_connection(
        dbname: str = settings.DB_NAME,
        user: str = settings.DB_USER,
        password: str = settings.DB_PASSWORD,
        host: str = settings.DB_HOST,
        port: int = settings.DB_PORT,
):
    try:
        logger.info("Connecting to database...")
        connection = psycopg.connect(dbname=dbname, user=user, password=password, host=host, port=port)
        logger.info("Connected to database!")
        return connection

    except OperationalError as e:
        logger.error(f"Error connecting to database: {e}")
        connection = None

    return connection

conn = create_connection()
