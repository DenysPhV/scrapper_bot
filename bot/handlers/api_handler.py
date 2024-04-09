import requests

from log.logger import get_logger

logger = get_logger()


def get_numbers(api_key):
    url = "https://api.textchest.com/numbers"
    auth = (api_key, '')

    response = requests.get(url, auth=auth)

    if response.status_code == 200:
        logger.info(f"Got numbers. Status code: {response.status_code}")
        return response.json()
    else:
        print(f"Failed to get numbers. Status code: {response.status_code}")
        logger.error(f"Failed to get numbers. Status code: {response.status_code}")
        return None


def get_sms(api_key, number):
    url = "https://api.textchest.com/sms"
    auth = (api_key, '')

    response = requests.get(url, auth=auth, params={'number': number})

    if response.status_code == 200:
        logger.info(f"Got SMS for number {number}. Status code: {response.status_code}")
        return response.json()
    else:
        logger.error(f"Failed to get SMS for number {number}. Status code: {response.status_code}")
        return None
