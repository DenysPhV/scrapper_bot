
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

def create_registration_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS registrations (
        id SERIAL PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        first_name VARCHAR(100),
        last_name VARCHAR(100),
        phone_number VARCHAR(20),
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """
    execute_query(create_table_query)

    alter_table_query = """
    ALTER TABLE registrations
    ADD COLUMN IF NOT EXISTS phone_number VARCHAR(20);
    """
    execute_query(alter_table_query)

def create_message_table():
    create_table_query = """
    CREATE TABLE IF NOT EXISTS message (
        id SERIAL PRIMARY KEY,
        message TEXT,
        user_id BIGINT NOT NULL,
        message_time TIMESTAMP WITH TIME ZONE
    )
    """
    execute_query(create_table_query)

create_registration_table()
create_message_table()
