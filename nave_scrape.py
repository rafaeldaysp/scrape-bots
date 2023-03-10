from bs4 import BeautifulSoup
from api.scrape_request import get_response

def coupon_validation(description, product):
    return True

def scrape(url, **kwargs):
    response = get_response(url)
    site = BeautifulSoup(response.content, 'html.parser')
    price = -1
    try:
        price = float(site.find('span', class_='vtex-product-price-1-x-sellingPriceValue').text[3:].replace('.', '').replace(',', '.'))
        price = price*0.95
    except Exception as e:
        print(e)
        
    return price, 'Nave'

if __name__ == '__main__':
    scrape('https://www.navegamer.com.br/notebook-gamer-nave-estelar-gm5ag0o/p')