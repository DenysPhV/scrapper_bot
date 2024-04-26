# bot/db/execute.py
from psycopg import OperationalError
from .connection import create_connection
from log.logger import get_logger

logger = get_logger()
conn = create_connection()

def insert_registration_data(email, first_name, last_name, phone_number):
    query = """
    INSERT INTO registrations (email, first_name, last_name, phone_number)
    VALUES (%s, %s, %s, %s)
    """
    values = (email, first_name, last_name, phone_number)

    execute_query(query, values)


def execute_query(query: str, values=None):
    cursor = conn.cursor()

    try:
        cursor.execute(query, values)
        logger.info("Query executed successfully")
        conn.commit()
    except OperationalError as e:
        logger.error(f"Error: '{e}' occurred while executing query: {query}")
        conn.rollback() 
    finally:
        cursor.close()

