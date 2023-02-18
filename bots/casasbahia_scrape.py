from bs4 import BeautifulSoup
from requests_html import HTMLSession
import json

def scrape(url):
    price, store = [-1, None]
    session = HTMLSession(browser_args=["--no-sandbox", "--user-agent='Testing'"])
    r = session.get(url)
    r.html.render()
    script = BeautifulSoup(r.html.raw_html, 'html.parser').find('script', {'type': 'application/json'})
    try:
        data = json.loads(script.contents[0])
        sku = data['query']['sku']
        url_data = f'https://pdp-api.casasbahia.com.br/api/v2/sku/{sku}/price/source/CB?utm_source=undefined&take=undefined&device_type=DESKTOP'
        session2 = HTMLSession(browser_args=["--no-sandbox", "--user-agent='Testing'"])
        r2 = session2.get(url_data)
        r2.html.render()
        json_data = json.loads(r2.html.html[r2.html.html.find('{'):r2.html.html.rfind('}')+1])
        price, store = [json_data['paymentMethodDiscount']['sellPriceWithDiscount'], json_data['sellers'][0]['name']]
    except Exception as e:
        print(e)
    print(price, store)

if __name__ == '__main__':
    pass
