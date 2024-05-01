#bot/function/registration_by_phone.py
from seleniumbase import Driver

from log.logger import get_logger

logger = get_logger()

def get_chromedriver():
    driver = Driver(uc=True)
    return driver

def register_user():
    pass

def register_by_phone(phone_number, verification_code):
    try:
        driver = get_chromedriver()
        driver.get("https://go.seated.com/notifications/login")
        # driver.sleep(20)

        driver.type('input[placeholder="Phone Number"]', phone_number)
        driver.click('input[data-test-phone-number]', timeout=5)
        driver.click('button[type="submit"]')
        # driver.sleep(5)

        for i in range(1, 5):
            digit = verification_code[i - 1]
            input_field = f'#ember151-digit{i}'
            driver.type(input_field, digit)

        # driver.click('button[type="submit"]')
        driver.sleep(30)
        
        
    except Exception as ex:
        logger.error(ex)
    finally:
        driver.close()
        driver.quit()


