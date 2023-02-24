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

def scrape(url, **kwargs):
    response = get_response(url)
    price = -2
    soup = BeautifulSoup(response.text, 'html.parser')
    try:
        price = soup.find('div', class_= 'p-price').find('strong').text.split(' ')[1][:-1]
        price = float(price.replace('.', '').replace(',', '.'))
    except Exception as e:
        print(e)
    return price, 'Magalu'

if __name__ == '__main__':
    scrape('https://www.magazinevoce.com.br/magazineotcm/monitor-gamer-lg-24-hdmidisplayport-led-full-hd-144hz-1ms-mbr-freesync-ajuste-de-inclinacao/p/edfj76cbh5/IN/MNPC/')