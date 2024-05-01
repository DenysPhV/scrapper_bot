#bot/handlers/api_handler.py
import re
import requests
from typing import Optional

from log.logger import get_logger

from db.database_manager import DatabaseManager

logger = get_logger()
db_manager = DatabaseManager()

def get_numbers(api_key):
    url = "https://api.textchest.com/numbers"
    auth = (api_key, '')

    try:
       response = requests.get(url, auth=auth)

       if response.status_code == 200:
            logger.info(f"Got numbers. Status code: {response.status_code}")
            data = response.json()
            phone_numbers = [entry['number'] for entry in data if 'number' in entry]
            return phone_numbers
       else:
            logger.error(f"Failed to get numbers. Status code: {response.status_code}")
            return None

    except Exception as e:
        logger.error(f"An error occurred while fetching numbers: {e}")
        return None
    
def extract_verification_code(sms_text):

    numbers = re.findall(r'\b\d+\b', sms_text)
    for number in numbers:
        if len(number) == 4:  
            return number
    return None


def get_sms(api_key, number):
    url = "https://api.textchest.com/sms"
    auth = (api_key, '')
    
    if not number.startswith('1'):
        number = '1' + number

    response = requests.get(url, auth=auth, params={'number': number})

    if response.status_code == 200:
        logger.info(f"Got SMS for number {number}. Status code: {response.status_code}")
        sms_data = response.json()
        logger.info(f"Received SMS data for number {number}: {sms_data}")

        seated_sms = [sms for sms in sms_data if "Your Seated verification number is:" in sms['msg']]
        db_manager.save_sms_to_database(seated_sms)
        return seated_sms
    else:
        logger.error(f"Failed to get SMS for number {number}. Status code: {response.status_code}")
        return None
    

    

 

