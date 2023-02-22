from requests_html import HTMLSession
from bs4 import BeautifulSoup
import re

def coupon_validation(description, product):
    return True

def scrape(url, params=None):
    price, store = [-1, None]
    while True:
        try:
            session = HTMLSession(browser_args=["--no-sandbox", "--user-agent='Testing'"])
            r = session.get(url)
            r.html.render(sleep = 2)
            break
        except:
            pass
    try:
        site = BeautifulSoup(r.html.raw_html, 'html.parser')
        price = float(site.find('div', class_=re.compile('priceSales')).text[3:].replace('.', '').replace(',', '.'))
        try:
            store = site.find('div', class_=re.compile('offers-box')).find('p').find('a').text
        except:
            store = site.find('div', class_=re.compile('offers-box')).find('p').find('strong').text
        #tore = site.find('div', class_=re.compile('generalInfo')).find('b').text
    except Exception as e:
        pass
    r.close()
    session.close()
    return price, store