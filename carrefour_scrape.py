from bs4 import BeautifulSoup
from api.scrape_request import get_response
import json

def coupon_validation(description, product):
    return True

def scrape(url, **kwargs):
    price, store = [-1, None]
    r = get_response(url)
    script = BeautifulSoup(r.content, 'html.parser').find('script', {'type': 'application/ld+json'})
    #print(r.content)
    try:
        data = json.loads(script.contents[0])
        price = float(data['offers']['offers'][0]['price'])
        store = data['offers']['offers'][0]['seller']['name']
    except Exception as e:
        print(r.content)
        print(e)
    return price, store
    
if __name__ == '__main__':
    scrape()