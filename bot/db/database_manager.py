from db.execute import insert_registration_data
from log.logger import get_logger

logger = get_logger()

class DatabaseManager:
    def __init__(self):
        pass

    def save_data_to_database(self, data):
        for entry in data:
            if self.is_valid_data(entry):
                try:
                    self.insert_data(entry)
                except Exception as e:
                    logger.error(f"Failed to insert data {entry} into database. Error: {e}")

    def is_valid_data(self, entry):
        # Проверка на корректность данных
        if 'email' in entry and 'first_name' in entry and 'last_name' in entry and 'phone_number' in entry:
            # В данном примере просто проверяем наличие необходимых полей, можно добавить другие проверки
            return True
        else:
            logger.error(f"Invalid data: {entry}")
            return False

    def insert_data(self, entry):
        insert_registration_data(entry['email'], entry['first_name'], entry['last_name'], entry['phone_number'])
        logger.info(f"Data inserted successfully: {entry}")
