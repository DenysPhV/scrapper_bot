from seleniumbase import Driver, BaseCase
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
        driver.sleep(20)
      
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    scraper()

