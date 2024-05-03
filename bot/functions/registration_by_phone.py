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
    if len(code) == 4 and code.isdigit():
        for i, digit in enumerate(code, start=1):
            input_field_id = f"ember151-digit{i}"
            driver.type(f"input#{input_field_id}", digit)

        # Добавляем явное ожидание для видимости кнопки подтверждения
        submit_button_selector = 'button[data-test-next][type="submit"]'
        try:
            driver.wait_for_element(submit_button_selector, timeout=30)
            driver.uc_click(submit_button_selector)
        except Exception as e:
            logger.error(f"Проблема с доступностью или кликом по кнопке подтверждения: {e}")
    else:
        logger.error("Предоставленный код подтверждения невалиден или не состоит из четырех цифр.")