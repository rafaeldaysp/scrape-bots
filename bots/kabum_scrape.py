import re
from bs4 import BeautifulSoup
from api.scrape_request import get_response
import json

def coupon_validation(description, product):
    if description:
        description = json.loads(description)
        try:
            if product['category']['name'] not in description['category']:
                return False
        except:
            pass
    return True

def scrape(url, params = None):
    price = -1
    store = None
    response = get_response(url)
    try:
        site = BeautifulSoup(response.content, 'html.parser')
        price = float(site.find('h4', class_=re.compile('finalPrice')).text[3:].replace('.', '').replace(',', '.'))
        store = site.find('div', class_=re.compile('generalInfo')).find('b').text
    except:
        pass
    return price, store
