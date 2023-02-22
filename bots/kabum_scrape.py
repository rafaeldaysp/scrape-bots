import re
from bs4 import BeautifulSoup
from api.scrape_request import get_response
import json
from requests_html import HTMLSession

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
    session = HTMLSession(browser_args=["--no-sandbox", "--user-agent='Testing'"])
    r = session.get(url)
    r.html.render()
    site = BeautifulSoup(r.html.raw_html, 'html.parser')
    print(site)
    r.close()
    session.close()
    try:
        price = float(site.find('h4', class_=re.compile('finalPrice')).text[3:].replace('.', '').replace(',', '.'))
        store = site.find('div', class_=re.compile('generalInfo')).find('b').text
    except:
        pass
    return price, store
