import requests
from zenrows import ZenRowsClient

from src.settings.settings import settings

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