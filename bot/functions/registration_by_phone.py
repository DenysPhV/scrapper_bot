#bot/function/registration_by_phone.py
from seleniumbase import Driver

from log.logger import get_logger

logger = get_logger()

def get_chromedriver():
    driver = Driver(uc=True)
    return driver

def register_user():
    pass


def enter_verification_code(driver, code):
    # Проверяем, что код состоит из четырех цифр
    if len(code) == 4 and code.isdigit():
        for i, digit in enumerate(code, start=1):
            input_field_id = f"ember151-digit{i}"
            driver.type(f"input#{input_field_id}", digit)

        # Предполагаем, что есть кнопка для подтверждения кода после его ввода
        driver.click('button[type="submit"]')
    else:
        logger.error("Invalid verification code provided")