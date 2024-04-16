import requests
from log.logger import get_logger

from db.database_manager import DatabaseManager

logger = get_logger()
db_manager = DatabaseManager()

def get_numbers(api_key):
    url = "https://api.textchest.com/numbers"
    auth = (api_key, '')
    phone_number = []

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        logger.info(f"Got numbers. Status code: {response.status_code}")
        data = response.json()

        for entry in data:
            if 'number' in entry:
                phone_number = [entry.get('number') for entry in data]
                return phone_number
            else:
                logger.error("Phone number is missing in entry: %s", entry)
        db_manager.save_phone_number_to_database(data)
        return data
    else:
        logger.error(f"Failed to get numbers. Status code: {response.status_code}")
        return None


def get_sms(api_key, number):
    url = "https://api.textchest.com/sms"
    auth = (api_key, '')

    response = requests.get(url, auth=auth, params={'number': number})

    if response.status_code == 200:
        logger.info(f"Got SMS for number {number}. Status code: {response.status_code}")
        sms_data = response.json()
        db_manager.save_sms_to_database(sms_data)  # Сохраняем SMS в базу данных
        return sms_data
    else:
        logger.error(f"Failed to get SMS for number {number}. Status code: {response.status_code}")
        return None
    

    

