from seleniumbase import Driver
from settings.settings import settings


# check_url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"


def get_chromedriver():
    driver = Driver(uc=True)
    return driver

def register_user():
    pass

def scraper():
    try:
        driver = get_chromedriver()
        # driver.get(check_url)
        driver.get(settings.URL)
        driver.sleep(6)

        driver.click('a[href="/event-reminders/bd3cd050-bda1-4b4f-9ef4-c65dd632b1c1"]')
        driver.sleep(5)
        driver.type('input[data-test-first-name]', "Ваше имя")
        driver.type('input[data-test-last-name]', "Ваша фамилия")
        driver.type('input[data-test-email]', "example@example.com")
       
        driver.click('button[type="submit"]')
     
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    scraper()

