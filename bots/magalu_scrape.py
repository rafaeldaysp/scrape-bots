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
    response = get_response(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    price = soup.find('div', class_= 'p-price').find('strong').text.split(' ')[1][:-1]
    price_value = price.replace('.', '').replace(',', '.')
    print(price_value)

    

if __name__ == '__main__':
    pass