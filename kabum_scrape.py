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
        try:
            if product['id'] not in description['product_id']:
                return False
        except:
            pass
    return True

def scrape(url, **kwargs):
    price = -1
    store = None
    response = get_response(url)
    try:
        site = BeautifulSoup(response.content, 'html.parser')
        price = float(site.find('h4', class_=re.compile('finalPrice')).text[3:].replace('.', '').replace(',', '.'))
        store = site.find('div', class_=re.compile('generalInfo')).find('b').text
    except Exception as e:
       print(e) 
    return price, store
