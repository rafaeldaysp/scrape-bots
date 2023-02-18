from fake_useragent import UserAgent
import requests

def get_response(url):
    ua = UserAgent()
    headers = {'User-Agent':str(ua.chrome),
           'Accept-Language': 'en-US, en;q=0.5'}
    response = requests.get(url, headers=headers, timeout=10)
    return response