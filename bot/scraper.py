import time
import requests
from zenrows import ZenRowsClient

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from settings.settings import settings

# use ZenRows
url = settings.URL
api_key = settings.ZR_KEY

params = {
    'url': url,
    'api_key': api_key,
	'js_render': 'true',
	'premium_proxy': 'true',
}
response = requests.get('https://api.zenrows.com/v1/', params=params)
print(response.text)


def register_user(email, password, confirm_password):  # email, password, confirm_password
   """
    Register a user.

    Parameters:
        email (str): User's email.
        password (str): User's password.
        confirm_password (str): Confirmation of user's password.
    """
   
# use selenium

options = webdriver.ChromeOptions()
service = Service(executable_path="/bot/utils/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=service, options=options)

driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    'source': '''
         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Array;
         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Promise;
         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Symbol;
         delete window.cdc_adoQpoasnfa76pfcZLmcfl_JSON;
         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Object;
         delete window.cdc_adoQpoasnfa76pfcZLmcfl_Proxy;
    '''
})

def register_user(email, password, confirm_password): 
    try:
        driver.get("https://go.seated.com/tour-events/ee8effe7-d205-403c-a39f-007a83ac9629")
        # TODO rewrite logical func
        # email_input = driver.find_element(By.NAME, "email")
        # email_input.send_keys(email)

        # password_input = driver.find_element(By.NAME, "password")
        # password_input.send_keys(password)

        # confirm_password_input = driver.find_element(By.NAME, "passwordConfirm")
        # confirm_password_input.send_keys(confirm_password)

        success_message = driver.find_elements(By.XPATH, "//div[contains(text(), 'Successfully registered')]")   
        time.sleep(80)

    except Exception as e:
        print(e)

    finally:
        if success_message:
            driver.quit()
            return True
        else:
            driver.quit()
            return False