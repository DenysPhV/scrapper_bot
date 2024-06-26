#bot/db/database_manager.py
from db.connection import create_connection
from db.execute import insert_registration_data, execute_query
from log.logger import get_logger

logger = get_logger()

class DatabaseManager:
    def __init__(self):
        self.conn = create_connection()

    def save_data_to_database(self, data):
        for entry in data:
            if self.is_valid_data(entry):
                try:
                    self.insert_data(entry)
                except Exception as e:
                    logger.error(f"Failed to insert data {entry} into database. Error: {e}")

    def is_valid_data(self, entry):
        if 'email' in entry and 'first_name' in entry and 'last_name' in entry and 'phone_number' in entry:
            # В данном примере просто проверяем наличие необходимых полей, можно добавить другие проверки
            return True
        else:
            logger.error(f"Invalid data: {entry}")
            return False

    def insert_data(self, entry):
        insert_registration_data(entry['email'], entry['first_name'], entry['last_name'], entry['phone_number'])
        logger.info(f"Data inserted successfully: {entry}")

    def save_phone_number_to_database(self, phone_number):

        if not isinstance(phone_number, (str, int)):
           logger.error("Error: phone number is neither a string nor an integer")
           return
        
        if self.conn is None:
            logger.error("Error: Don't to connect with DB")
            return
        
        phone_number = str(phone_number)
        try:
            cursor = self.conn.cursor()
            
            query = """
            INSERT INTO phone_numbers (phone_number)
            VALUES (%s)
            """
            values = (phone_number,)
            cursor.execute(query, values)

            self.conn.commit()
            logger.info(f"Phone number '{phone_number}' inserted successfully into database.")

        except Exception as e:
            self.conn.rollback()
            logger.error(f"Failed to insert phone number '{phone_number}' into database. Error: {e}")

        finally:
            cursor.close()


    def get_phone_numbers_from_database(self):
        try:
            cursor = self.conn.cursor()
            query = "SELECT phone_number FROM phone_numbers"
            cursor.execute(query)
            phone_numbers = [row[0] for row in cursor.fetchall()]
            return phone_numbers
        except Exception as e:
            logger.error(f"Failed to retrieve phone numbers from database: {e}")
            return None
        finally:
            cursor.close()

# ====================================================================
# work to sms 
# ====================================================================
    def save_sms_to_database(self, sms_data):
        
        if not isinstance(sms_data, list):
           logger.error("Error: sms_data должен быть списком")
           return

        if self.conn is None:
            logger.error("Error: Не удалось подключиться к базе данных")
            return

        try:
            cursor = self.conn.cursor()
            for sms in sms_data:
                message = sms.get('msg')
                ts = sms.get('ts')
                sender = sms.get('from')

                query = """
                INSERT INTO sms (message, ts, sender)
                VALUES (%s, %s, %s)
                """
                values = (message, ts, sender)
                cursor.execute(query, values)

            self.conn.commit()
            logger.info("SMS data successfully saved in database")

        except Exception as e:
            self.conn.rollback()
            logger.error(f"Error: {e}")

        finally:
            cursor.close()

            

