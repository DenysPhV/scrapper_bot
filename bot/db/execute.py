import psycopg
from datetime import datetime

from .connection import conn
# from psycopg import OperationalError

from log.logger import get_logger

logger = get_logger()

# Добавление функции для записи данных регистрации в базу данных
def insert_registration_data(email, first_name, last_name, phone_number):
    query = """
    INSERT INTO registrations (email, first_name, last_name, phone_number)
    VALUES (%s, %s, %s, %s)
    """
    values = (email, first_name, last_name, phone_number, datetime.now())

    execute_query(query, values)


# def execute_query(query: str, connection=conn):
#     connection.autocommit = True
#     cursor = connection.cursor()
#     try:
#         cursor.execute(query)
#         print("Query executed successfully")
#     except OperationalError as e:
#         print(f"Error: '{e}' occurred while executing query: {query}")

def execute_query(query: str, values=None):
    cursor = conn.cursor()

    try:
        cursor.execute(query, values)
        logger.info("Query executed successfully")
        conn.commit()  # Применение изменений
    except psycopg.Error as e:
        logger.error(f"Error: '{e}' occurred while executing query: {query}")
        conn.rollback()  # Откат в случае ошибки
    finally:
        cursor.close()


create_message_table = """
CREATE TABLE IF NOT EXISTS message (
    id SERIAL PRIMARY KEY,
    message TEXT,
    user_id BIGINT NOT NULL,
    message_time TIMESTAMP WITH TIME ZONE
)
"""

execute_query(create_message_table)