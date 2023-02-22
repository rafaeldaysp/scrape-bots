from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json
from fake_useragent import UserAgent

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
    price, store = [-1, 'Casas Bahia']
    ua = str(UserAgent().chrome)
    try:
        session = HTMLSession(browser_args=["--no-sandbox", "--user-agent="+ua])
        r = session.get(url)
        r.html.render(sleep=3)
        site = BeautifulSoup(r.html.raw_html, 'html.parser')
        price = site.find('span', class_='product-price-value').text[3:].replace('.', '').replace(',', '.')
    except Exception as e:
        print('Scraping Casas Bahia bad request: ', e)
        print(r.html.html)
        pass
    return price, store

if __name__ == '__main__':
    scrape('https://www.casasbahia.com.br/notebook-lenovo-amd-ryzen-5-5500u-8gb-256gb-ssd-tela-full-hd-15-6-linux-ideapad-3-82mfs00100-55056427/p/55056427?')
