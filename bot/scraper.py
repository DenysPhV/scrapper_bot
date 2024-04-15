from seleniumbase import Driver, BaseCase, config as sb_config
from settings.settings import settings


# check_url = "https://intoli.com/blog/not-possible-to-block-chrome-headless/chrome-headless-test.html"

class ScraperEvent(BaseCase):
    def __init__(self):
        self.link = "https://ticketmaster.evyy.net/c/1387536/264167/4272?u=https%3A%2F%2Fwww.ticketmaster.com%2Fevent%2F2200607ADB821FC8&SHAREDID=BxcmJ4dR"

    def get_event_parse(self):
        self.click_link_text("Buy Tickets")


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

        scraper_event = ScraperEvent()
        scraper_event.get_event_parse()
        
      
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()

if __name__ == "__main__":
    scraper()
