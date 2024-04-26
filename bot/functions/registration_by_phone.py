#bot/function/registration_by_phone.py
from seleniumbase import Driver

def get_chromedriver():
    driver = Driver(uc=True)
    return driver

def register_user():
    pass

def register_by_phone(phone_number):
    try:
        driver = get_chromedriver()
        driver.get("https://go.seated.com/notifications/login")
        driver.sleep(6)

        driver.click('input[data-test-phone-number]', timeout=7)
        driver.type('input[placeholder="Phone Number"]', phone_number)
       
        driver.click('button[type="submit"]')
        driver.sleep(5)

        driver.click('button[type="submit"]')
        driver.sleep(5)
        
        
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


