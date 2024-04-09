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